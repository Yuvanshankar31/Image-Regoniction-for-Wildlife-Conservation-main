# 🦁 Wildlife AI - Conservation Detection System

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![YOLOv9](https://img.shields.io/badge/YOLOv9-latest-red.svg)](https://github.com/ultralytics/ultralytics)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An AI-powered wildlife detection and conservation platform using YOLOv9 for real-time animal identification with an intelligent chatbot providing detailed information about endangered species.

![Wildlife AI Banner](https://via.placeholder.com/1200x400/0f172a/10b981?text=Wildlife+AI+-+Conservation+Detection+System)

---

## 🌟 Features

### 🔍 **Wildlife Detection**
- Real-time animal detection using YOLOv9
- Support for images (JPG, PNG) and videos (MP4)
- High-accuracy bounding box visualization
- Instant results with detailed analysis

### 💬 **Intelligent Chatbot**
- Comprehensive knowledge base of 10+ endangered species
- Natural language understanding
- Detailed conservation information
- Fun facts and educational content

### 📊 **Animal Information Cards**
- Conservation status (Endangered/Vulnerable/Safe)
- Scientific names and taxonomy
- Habitat and distribution
- Population trends and statistics
- Conservation efforts

### 🎨 **Modern UI/UX**
- Clean, professional dark theme
- Responsive design (mobile-friendly)
- Smooth animations and transitions
- Drag-and-drop file upload
- Real-time loading indicators

---

## 🦁 Supported Animals

| Animal | Scientific Name | Status |
|--------|----------------|--------|
| 🦁 African Lion | *Panthera leo* | Vulnerable |
| 🐯 Bengal Tiger | *Panthera tigris* | Endangered |
| 🐘 African Elephant | *Loxodonta africana* | Endangered |
| 🦏 Rhinoceros | *Rhinocerotidae* | Critically Endangered |
| 🐼 Giant Panda | *Ailuropoda melanoleuca* | Vulnerable |
| 🦍 Mountain Gorilla | *Gorilla beringei* | Endangered |
| 🐆 Snow Leopard | *Panthera uncia* | Vulnerable |
| 🐻 Polar Bear | *Ursus maritimus* | Vulnerable |
| 🐆 Cheetah | *Acinonyx jubatus* | Vulnerable |
| 🦧 Orangutan | *Pongo* | Critically Endangered |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/wildlife-ai.git
cd wildlife-ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py --port 5000
```

### Access the Application
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📁 Project Structure

```
wildlife-ai/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment configuration
├── runtime.txt                 # Python version
│
├── chatbot/                    # Chatbot module
│   ├── enhanced_chat.py        # Enhanced chatbot (10 species)
│   ├── simple_chat.py          # Fallback chatbot
│   ├── chat.py                 # ML chatbot (optional)
│   ├── model.py                # Neural network model
│   ├── nltk_utils.py           # NLP utilities
│   └── intents.json            # Chatbot intents
│
├── models/                     # YOLO models
│   └── best.pt                 # Trained YOLOv9 model
│
├── templates/                  # HTML templates
│   ├── detect.html             # Main detection page
│   ├── index.html              # Dashboard (legacy)
│   └── ...
│
├── static/                     # Static assets
│   ├── images/
│   ├── css/
│   └── js/
│
├── uploads/                    # User uploads (temporary)
└── runs/                       # Detection results
```

---

## 💻 Tech Stack

### Backend
- **Flask** - Web framework
- **YOLOv9** (Ultralytics) - Object detection
- **OpenCV** - Image processing
- **PyTorch** - Deep learning framework

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (custom, no frameworks)
- **JavaScript** - Interactivity
- **Fetch API** - Async requests

### Deployment
- **Gunicorn** - WSGI server
- **Render/Railway** - Cloud hosting
- **Git** - Version control

---

## 🎯 Usage

### 1. Upload Media
- Click the upload area or drag & drop
- Supported formats: JPG, PNG, MP4
- Maximum file size: 50MB

### 2. Detect Wildlife
- Click "Detect Wildlife" button
- Wait for AI analysis (5-30 seconds)
- View results with bounding boxes

### 3. View Animal Information
- Automatic display below detection results
- Conservation status, habitat, population
- Scientific name and interesting facts

### 4. Chat with AI Assistant
- Click the chat button (💬) in bottom-right
- Ask about endangered species
- Get instant, detailed responses

### Example Questions:
```
"Tell me about tigers"
"Are rhinos endangered?"
"Where do elephants live?"
"How many pandas are left?"
"Fun facts about lions"
"How can I help conservation?"
```

---

## 🌐 Deployment

### Deploy to Render (Recommended)

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Create Render Account**
- Go to [render.com](https://render.com)
- Sign up with GitHub

3. **Deploy**
- New → Web Service
- Connect repository
- Auto-deploy enabled!

**Your live URL:** `https://wildlife-ai.onrender.com`

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

---

## 📊 API Endpoints

### POST `/detect`
Upload and detect wildlife in images/videos

**Request:**
```javascript
FormData {
  file: <image/video file>
}
```

**Response:**
```json
{
  "success": true,
  "result_image": "filename.jpg",
  "message": "Detection complete"
}
```

### POST `/predict`
Chat with the wildlife assistant

**Request:**
```json
{
  "message": "tell me about tigers"
}
```

**Response:**
```json
{
  "answer": "🦁 Bengal Tiger (Panthera tigris)..."
}
```

---

## 🎨 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x500/0f172a/10b981?text=Wildlife+Detection+Interface)

### Detection Results
![Detection Results](https://via.placeholder.com/800x500/0f172a/10b981?text=Detection+Results+with+Animal+Info)

### Chatbot
![Chatbot](https://via.placeholder.com/400x600/0f172a/10b981?text=Wildlife+Conservation+Chatbot)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Ultralytics** - YOLOv9 implementation
- **Flask** - Web framework
- **Wildlife Conservation Organizations** - Data and inspiration
- **Open Source Community** - Various tools and libraries

---

## 📧 Contact

**Your Name** - [@yourtwitter](https://twitter.com/yourtwitter)

**Project Link:** [https://github.com/YOUR_USERNAME/wildlife-ai](https://github.com/YOUR_USERNAME/wildlife-ai)

**Live Demo:** [https://wildlife-ai.onrender.com](https://wildlife-ai.onrender.com)

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/wildlife-ai&type=Date)](https://star-history.com/#YOUR_USERNAME/wildlife-ai&Date)

---

## 📈 Future Enhancements

- [ ] Real-time camera detection
- [ ] Mobile app (React Native)
- [ ] Multi-language support
- [ ] User accounts and history
- [ ] Social media sharing
- [ ] Advanced analytics dashboard
- [ ] API for third-party integration
- [ ] Offline mode support

---

<div align="center">

**Made with ❤️ for Wildlife Conservation**

[Report Bug](https://github.com/YOUR_USERNAME/wildlife-ai/issues) · [Request Feature](https://github.com/YOUR_USERNAME/wildlife-ai/issues)

</div>
"# Image-Regoniction-for-Wildlife-Conservation-main" 
