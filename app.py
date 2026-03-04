import os
import time
import cv2
import argparse
from flask import Flask, request, render_template, jsonify, Response, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO

# Import enhanced chatbot - comprehensive wildlife knowledge
print("📝 Loading Enhanced Wildlife Chatbot...")
from chatbot.enhanced_chat import enhanced_get_response as get_response
CHATBOT_TYPE = "Enhanced"
print("✅ Enhanced Chatbot loaded - 10 species, comprehensive knowledge!")

app = Flask(__name__)
CORS(app)

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')
RUNS_DIR = os.path.join(BASE_DIR, 'runs')

# Ensure directories exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(os.path.join(RUNS_DIR, 'detect'), exist_ok=True)

# Load Model
MODEL_PATH = os.path.join(MODELS_DIR, 'best.pt')
try:
    print(f"Loading model from {MODEL_PATH}...")
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def index():
    return render_template('detect.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get("message") if data else None
        if not text:
            return jsonify({"answer": "Please provide a message."})
        
        response = get_response(text)
        return jsonify({"answer": response})
    except Exception as e:
        print(f"Chatbot error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"answer": f"I'm having trouble processing that. Could you rephrase your question about wildlife?"})

@app.route('/detect', methods=['POST'])
def detect_object():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    f = request.files['file']
    if f.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    filepath = os.path.join(UPLOADS_DIR, f.filename)
    f.save(filepath)
    file_extension = f.filename.rsplit('.', 1)[1].lower()

    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    if file_extension in ['jpg', 'jpeg', 'png', 'bmp']:
        # Image detection
        img = cv2.imread(filepath)
        results = model(img)
        
        # Save result
        detection_folder = os.path.join(RUNS_DIR, 'detect', f.filename.rsplit(".", 1)[0])
        os.makedirs(detection_folder, exist_ok=True)
        detection_path = os.path.join(detection_folder, f.filename)
        
        # Plot and save
        res_plotted = results[0].plot()
        cv2.imwrite(detection_path, res_plotted)
        
        # Return JSON response
        return jsonify({
            "success": True,
            "result_image": f.filename,
            "message": "Detection complete"
        })

    elif file_extension == 'mp4':
        # Video detection
        cap = cv2.VideoCapture(filepath)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        output_path = os.path.join(UPLOADS_DIR, 'output.mp4')
        
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (frame_width, frame_height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            res_plotted = results[0].plot()
            out.write(res_plotted)

        cap.release()
        out.release()
        
        return jsonify({
            "success": True,
            "video": True,
            "message": "Video processing complete"
        })

    return jsonify({"error": "Unsupported file type"}), 400

@app.route('/display/<filename>')
def display_image(filename):
    # This assumes we want to show the result.
    # We need to find where the result is.
    # For now, let's assume it's in runs/detect/<filename_start>/<filename>
    # This logic is a bit brittle. Let's simplify: save results to static/results is better?
    # Or serve from runs/detect...
    
    # Original logic:
    # return send_from_directory(directory, file_name)
    pass 

@app.route('/result/<filename>')
def result_file(filename):
    # Search for the file in runs/detect
    # This is tricky because of the folder structure created by the previous code: runs/detect/{name}/{name}.jpg
    name_only = filename.rsplit('.', 1)[0]
    folder = os.path.join(RUNS_DIR, 'detect', name_only)
    return send_from_directory(folder, filename)

def get_frame():
    output_path = os.path.join(UPLOADS_DIR, 'output.mp4')
    if not os.path.exists(output_path):
        return
    video = cv2.VideoCapture(output_path)
    while True:
        success, image = video.read()
        if not success:
            break
        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        time.sleep(0.01)

@app.route("/video_feed")
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask App")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port, debug=True)
