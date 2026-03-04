# 🚀 Wildlife AI - Deployment Guide

## 📋 Quick Deployment to Render.com

### Why Render?
- ✅ **Free tier available** (perfect for portfolio)
- ✅ **Supports Flask/Python** natively
- ✅ **Easy deployment** from GitHub
- ✅ **Automatic HTTPS** 
- ✅ **Custom domain** support
- ✅ **Better for ML models** than Vercel

---

## 🎯 Step-by-Step Deployment

### 1. Prepare Your Repository

**Push to GitHub:**
```bash
cd d:\projects\yolo_v9
git init
git add .
git commit -m "Wildlife AI - Ready for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/wildlife-ai.git
git push -u origin main
```

### 2. Sign Up on Render

1. Go to [render.com](https://render.com)
2. Sign up with GitHub account
3. Authorize Render to access your repositories

### 3. Create New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Select **"wildlife-ai"** repository

### 4. Configure Service

**Settings:**
- **Name:** `wildlife-ai` (or your preferred name)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`

**Environment Variables:**
- `PYTHON_VERSION`: `3.11.0`
- `PORT`: `10000` (auto-set by Render)

### 5. Deploy!

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. Your app will be live at: `https://wildlife-ai.onrender.com`

---

## 🌐 Alternative: Deploy to Railway.app

### Why Railway?
- ✅ Free $5 credit monthly
- ✅ Very simple deployment
- ✅ Good for Python apps

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Python and deploys!

**Your URL:** `https://wildlife-ai.up.railway.app`

---

## 🎨 Alternative: Heroku (Classic Choice)

### Deploy to Heroku:

```bash
# Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create wildlife-ai-yourname

# Deploy
git push heroku main

# Open app
heroku open
```

**Your URL:** `https://wildlife-ai-yourname.herokuapp.com`

---

## 📝 Files Prepared for Deployment

✅ `requirements.txt` - All Python dependencies
✅ `Procfile` - Deployment configuration
✅ `runtime.txt` - Python version specification
✅ `app.py` - Main Flask application
✅ Enhanced chatbot with no external dependencies

---

## 🔧 Important Notes

### Model File Size
⚠️ **Issue:** YOLO model (`best.pt`) might be large (>100MB)

**Solutions:**

**Option 1: Git LFS (Large File Storage)**
```bash
git lfs install
git lfs track "*.pt"
git add .gitattributes
git add models/best.pt
git commit -m "Add model with LFS"
git push
```

**Option 2: Download model on startup**
Add to `app.py`:
```python
import os
import urllib.request

MODEL_URL = "YOUR_MODEL_URL"  # Upload to Google Drive/Dropbox
MODEL_PATH = os.path.join(MODELS_DIR, 'best.pt')

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
```

**Option 3: Use smaller model**
- Use YOLOv8n (nano) instead of full model
- Reduces size from ~100MB to ~6MB

---

## 🎯 For Your CV/Portfolio

### Your Live Link Will Be:

**Render:** `https://wildlife-ai.onrender.com`
**Railway:** `https://wildlife-ai.up.railway.app`
**Heroku:** `https://wildlife-ai-yourname.herokuapp.com`

### Portfolio Description:

```
🦁 Wildlife AI - Conservation Detection System
Live Demo: https://wildlife-ai.onrender.com

An AI-powered wildlife detection and conservation platform using YOLOv9 
for real-time animal identification with an intelligent chatbot providing 
detailed information about endangered species.

Tech Stack: Python, Flask, YOLOv9, OpenCV, HTML/CSS/JavaScript
Features: Real-time detection, 10+ species database, conservation chatbot
```

---

## 🚀 Quick Start Commands

### Local Development:
```bash
python app.py --port 5000
# Open: http://localhost:5000
```

### Deploy to Render:
```bash
git add .
git commit -m "Update"
git push origin main
# Render auto-deploys!
```

---

## 📊 Free Tier Limits

### Render Free Tier:
- ✅ 750 hours/month
- ✅ 512 MB RAM
- ✅ Sleeps after 15 min inactivity
- ⚠️ First request after sleep takes ~30 seconds

### Railway Free Tier:
- ✅ $5 credit/month
- ✅ ~500 hours runtime
- ✅ Better performance than Render

### Heroku Free Tier:
- ⚠️ No longer free (requires paid plan)

---

## 🎨 Custom Domain (Optional)

### Add Custom Domain on Render:
1. Go to your service settings
2. Click "Custom Domain"
3. Add: `wildlife-ai.yourdomain.com`
4. Update DNS records as shown
5. SSL certificate auto-generated!

---

## 🐛 Troubleshooting

### App won't start?
- Check logs in Render dashboard
- Verify all files are committed
- Ensure `requirements.txt` is correct

### Model not loading?
- Check model file size (<100MB recommended)
- Use Git LFS for large files
- Consider downloading model on startup

### Chatbot not working?
- Enhanced chatbot has no dependencies!
- Should work out of the box
- Check Flask logs for errors

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `requirements.txt` updated
- [ ] `Procfile` created
- [ ] `runtime.txt` specified
- [ ] Model file handled (LFS or download)
- [ ] Render account created
- [ ] Web service configured
- [ ] Environment variables set
- [ ] Deployment successful
- [ ] App tested online
- [ ] Link added to CV/portfolio

---

## 🎉 You're Ready!

Your Wildlife AI application is ready for deployment. Choose your platform and follow the steps above. 

**Recommended:** Start with **Render.com** for easiest deployment!

Good luck with your project! 🦁🌿✨
