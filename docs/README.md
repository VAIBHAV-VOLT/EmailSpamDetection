# 📧 Email Phishing Analyzer

A comprehensive AI-powered email phishing detection system using machine learning, security analysis, and threat intelligence.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Node.js](https://img.shields.io/badge/node.js-16+-brightgreen)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## 🎯 Quick Start

**New here?** Start with one of these:

### ⚡ Super Fast (30 seconds)
```powershell
cd e:\Project\emailphishing\emailphishing
.\run.bat
```
That's it! The application will start automatically.

### 📖 Detailed Instructions
See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide.

### 🔧 All Options
See [RUNNING_METHODS.md](RUNNING_METHODS.md) for all ways to run the app.

---

## ✨ Features

- 🧠 **AI-Powered Analysis**: HuggingFace RoBERTa model for email body analysis
- 🔐 **Security Verification**: SPF, DMARC, DKIM authentication checks
- 📎 **URL Analysis**: Suspicious link detection with ML assistance
- 📊 **Rich Metadata**: Email header, attachment, and infrastructure analysis
- 🎨 **Modern UI**: React-based web interface with dark mode
- ⚡ **Real-time Results**: Instant phishing risk assessment
- 📱 **Responsive Design**: Works on desktop and mobile

---

## 📋 System Requirements

- **Python**: 3.8 or higher
- **Node.js**: 16 or higher
- **RAM**: 4GB minimum (8GB recommended for ML models)
- **Disk Space**: 2GB free
- **OS**: Windows, macOS, or Linux

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│           Frontend (React + Vite)                   │
│         http://localhost:5173                       │
└──────────────────┬──────────────────────────────────┘
                   │ HTTP
┌──────────────────┴──────────────────────────────────┐
│          Backend (Flask API)                        │
│         http://localhost:5000                       │
└──────────────────┬──────────────────────────────────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
┌────▼────┐  ┌─────▼─────┐  ┌────▼─────┐
│   ML     │  │ Security  │  │ Email    │
│ Module   │  │  Checks   │  │ Parser   │
│(RoBERTa) │  │(SPF/DMARC)│  │          │
└──────────┘  └───────────┘  └──────────┘
```

---

## 📁 Project Structure

| Folder | Purpose |
|--------|---------|
| `backend/` | Flask web server and API endpoints |
| `frontend/` | React UI application |
| `ml/` | Machine learning analysis engine |
| `data/` | Sample test emails and data |
| `utils/` | Helper scripts and utilities |
| `docs/` | Documentation |

**Full structure:** See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

---

## 🚀 Getting Started

### Option 1: Automated Start (Recommended)

**Windows:**
```powershell
cd e:\Project\emailphishing\emailphishing
run.bat
```

**PowerShell:**
```powershell
cd e:\Project\emailphishing\emailphishing
.\run.ps1
```

The application will:
1. Set up Python environment
2. Install dependencies
3. Start backend server
4. Start frontend server
5. Open in your browser

### Option 2: Manual Start

**Terminal 1 - Backend:**
```powershell
cd backend
..\venv\Scripts\Activate.ps1
pip install -r ../requirements.txt
python main.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend/emailanalyzer
npm install
npm run dev
```

### Option 3: Docker
```bash
docker build -t emailphishing:latest .
docker run -p 5000:5000 -p 5173:5173 emailphishing:latest
```

---

## 🧪 Testing the System

After starting the application:

1. **Open Frontend**: http://localhost:5173
2. **Click "Upload Email"**
3. **Select Test File**: Choose `data/sample.eml`
4. **View Results**: Review the phishing analysis

### API Health Check
```powershell
$response = Invoke-WebRequest -Uri "http://localhost:5000/health" -UseBasicParsing
$response.Content
```

Should return:
```json
{"status": "healthy", "service": "Email Phishing Analyzer with RoBERTa Model"}
```

---

## 🔍 How It Works

### Email Analysis Pipeline

1. **Parse Email** → Extract headers, body, attachments
2. **Security Checks** → Verify SPF, DMARC, DKIM
3. **ML Analysis** → RoBERTa model analyzes email body
4. **URL Analysis** → Check all links for threats
5. **Domain Check** → Verify sender domain reputation
6. **Score Calculation** → Combine all signals
7. **Risk Assessment** → Safe / Suspicious / Phishing

### Risk Levels

| Score | Level | Meaning |
|-------|-------|---------|
| 0-30 | 🟢 Safe | Likely legitimate |
| 31-70 | 🟡 Suspicious | Needs attention |
| 71-100 | 🔴 Phishing | Likely malicious |

---

## 🛠️ Development

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 19, Vite, Tailwind CSS |
| **Backend** | Flask 2.3, CORS |
| **ML** | HuggingFace Transformers, RoBERTa |
| **Infrastructure** | Python DNS, email libraries |

### Making Changes

**Backend Changes:**
- Edit files in `backend/` or `ml/phishingtool/`
- Flask auto-reloads on save
- Test with fresh email upload

**Frontend Changes:**
- Edit files in `frontend/emailanalyzer/src/`
- Vite hot-reloads automatically
- See changes immediately in browser

### Running Tests
```powershell
cd utils
python test_analyzer.py
```

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [QUICKSTART.md](QUICKSTART.md) | 5-minute setup guide |
| [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md) | Detailed run instructions |
| [RUNNING_METHODS.md](RUNNING_METHODS.md) | All ways to run the app |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Architecture & folder details |
| [REORGANIZATION_GUIDE.md](REORGANIZATION_GUIDE.md) | Project organization guide |

---

## 🔗 API Reference

### Analyze Email
```http
POST /analyze_email_route
Content-Type: multipart/form-data

Response:
{
  "overall_score": 72,
  "risk_level": "Suspicious",
  "spf": "pass",
  "dmarc": "fail",
  "dkim": "pass",
  "component_scores": {...}
}
```

### Health Check
```http
GET /health

Response:
{
  "status": "healthy",
  "service": "Email Phishing Analyzer with RoBERTa Model"
}
```

---

## ⚠️ Troubleshooting

### Common Issues

**Backend won't start:**
```powershell
# Check Python is installed
python --version

# Reinstall dependencies
pip install -r requirements.txt

# Check port 5000 is not in use
Get-Process | Where-Object {$_ -Match python}
```

**Frontend won't start:**
```powershell
# Check Node.js is installed
node --version

# Reinstall Node modules
rm -r node_modules
npm install
```

**Can't connect backend to frontend:**
- Ensure both servers are running
- Check CORS is enabled in main.py
- Verify URLs are correct (localhost:5000 and localhost:5173)
- Check browser console (F12) for errors

**Dependencies won't install:**
```powershell
# Use cache-free install
pip install --no-cache-dir -r requirements.txt

# For Torch, use CPU version if CUDA fails:
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**Full troubleshooting guide:** [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md#-troubleshooting)

---

## 📊 Performance

### First Run
- Backend setup: 5-10 minutes (ML model download)
- Frontend setup: 2-3 minutes (npm install)
- Total: ~15 minutes

### Subsequent Runs
- Backend startup: 15-30 seconds
- Frontend startup: 5-10 seconds
- Email analysis: 2-5 seconds

### System Requirements
- **Small emails** (<1MB): < 2 seconds
- **Medium emails** (1-5MB): 2-5 seconds
- **Large emails** (5-16MB): 5-30 seconds

---

## 🔐 Security Notes

✅ **File Uploads**
- Only .eml files accepted
- Maximum 16MB per file
- Files auto-deleted after analysis
- No data stored permanently

✅ **API**
- CORS configured for frontend only
- No authentication (local development)
- Add authentication for production use

✅ **Data Privacy**
- Email content analyzed locally
- No external APIs called (except HuggingFace for models)
- Consider running on isolated network in production

---

## 📦 Deployment

### Production Checklist

- [ ] Set `FLASK_DEBUG=False`
- [ ] Use production WSGI server (Gunicorn)
- [ ] Add authentication/authorization
- [ ] Enable HTTPS
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Optimize ML model (quantization)

### Deployment Commands

**Build Frontend:**
```powershell
cd frontend/emailanalyzer
npm run build
```

**Run Production Backend:**
```powershell
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

---

## 🤝 Contributing

Want to improve the analyzer? 

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

**Areas for contribution:**
- Better ML models
- New security checks
- UI improvements
- Documentation
- Performance optimization

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📞 Support & Contact

- 📖 **Documentation**: Check [docs/](.) folder
- 🐛 **Issues**: Create an issue on GitHub
- 💬 **Questions**: Use discussions forum
- 📧 **Email**: [contact info here]

---

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [HuggingFace Models](https://huggingface.co/models)
- [Email Security Best Practices](https://tools.ietf.org/html/rfc7231)

---

## 🚀 What's Next?

1. ✅ Start the application (`run.bat` or `run.ps1`)
2. ✅ Upload a test email from `data/` folder
3. ✅ Review the phishing assessment
4. 📖 Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
5. 🔧 Customize for your needs
6. 🚀 Deploy to production

---

## 📈 Version History

- **v1.0.0** (March 2026)
  - Initial release
  - RoBERTa ML model integration
  - Full security check suite
  - React UI with dark mode
  - Modular project structure

---

**Made with ❤️ for better email security**

---

## Quick Links

- **Start Now**: [run.bat](../run.bat) or [run.ps1](../run.ps1)
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- **Full Instructions**: [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md)
- **All Run Methods**: [RUNNING_METHODS.md](RUNNING_METHODS.md)
- **Project Structure**: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

---

**Last Updated:** March 29, 2026
