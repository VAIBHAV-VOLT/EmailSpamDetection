# How to Run Email Phishing Analyzer

Complete step-by-step guide to set up and run the entire email phishing analysis system.

## 📋 Prerequisites

Before you start, ensure you have installed:

1. **Python 3.8+** (Check: `python --version`)
2. **Node.js 16+** (Check: `node --version` and `npm --version`)
3. **Git** (optional, for version control)

### Windows Setup Check
```powershell
# Open PowerShell and verify installations
python --version
npm --version
```

If any are missing, download from:
- Python: https://www.python.org/downloads/
- Node.js: https://nodejs.org/

---

## 🚀 Installation & Setup

### Step 1: Navigate to Project Root

```powershell
cd e:\Project\emailphishing\emailphishing
```

### Step 2: Backend Setup (Flask API Server)

#### 2a. Create Python Virtual Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

**Note:** If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 2b. Install Python Dependencies
```powershell
# Make sure virtual environment is activated (you should see (venv) in terminal)
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected Output:**
```
Successfully installed flask-2.3.3 flask-cors-4.0.0 dnspython-2.4.2 transformers-4.34.1 ...
```

**Note:** First installation may take 5-10 minutes as it downloads ML models.

### Step 3: Frontend Setup (React + Vite)

#### 3a. Navigate to Frontend Directory
```powershell
cd frontend\emailanalyzer
```

#### 3b. Install Node Dependencies
```powershell
npm install
```

**Expected Output:**
```
added XXX packages in X.XXs
```

---

## ▶️ Running the Application

### Option A: Run in Two Terminal Windows (Recommended)

#### Terminal 1: Backend Server

```powershell
# From project root: e:\Project\emailphishing\emailphishing
cd backend

# Make sure Python venv is activated
..\venv\Scripts\Activate.ps1

# Run Flask server
python main.py
```

**Expected Output:**
```
 * Serving Flask app 'main'
 * Debug mode: off
 * WARNING: This is a development server. Do not use it in production deployment.
 * Running on http://127.0.0.1:5000
```

✅ **Backend is ready** when you see the Flask server running message.

#### Terminal 2: Frontend Development Server

```powershell
# From project root: e:\Project\emailphishing\emailphishing
cd frontend\emailanalyzer

# Install Node modules if not already done
npm install

# Start Vite dev server
npm run dev
```

**Expected Output:**
```
VITE v7.3.1
➜  local:   http://localhost:5173/
➜  press h + enter to show help
```

✅ **Frontend is ready** when you see the Vite server running message.

#### Open in Browser

1. The frontend should auto-open at: `http://localhost:5173`
   - If not, manually open your browser and navigate to this URL
2. Backend API is running at: `http://localhost:5000`

---

### Option B: Quick Sequential Run

If you only have one terminal:

```powershell
# Terminal 1: Start backend (runs in background)
cd backend
..\venv\Scripts\Activate.ps1
python main.py

# Open a new PowerShell window or tab (Ctrl+Shift+N)

# Terminal 2: Start frontend
cd frontend\emailanalyzer
npm run dev
```

---

## 🧪 Testing the Application

### 1. Health Check (Backend Verification)

Open your browser and visit:
```
http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "service": "Email Phishing Analyzer with RoBERTa Model"
}
```

### 2. Upload Test Email

1. **Open Frontend:** http://localhost:5173
2. **Click "Upload Email"** button
3. **Select Test File:** Use one from `data/` folder:
   - `data/sample.eml`
   - `data/email2.eml`
4. **View Results:** The app will display:
   - Overall phishing score (0-100)
   - Risk level (Safe / Suspicious / Phishing)
   - SPF, DMARC, DKIM status
   - URL analysis
   - Component scores

### 3. Test with curl (Optional)

```powershell
# Make sure you have a test .eml file
# Test the API endpoint

$filePath = ".\data\sample.eml"
$url = "http://localhost:5000/analyze_email_route"

curl.exe -X POST -F "file=@$filePath" $url
```

---

## 📊 Application Features

Once running, you can:

- ✅ Upload .eml email files
- ✅ Get real-time phishing risk analysis
- ✅ View detailed security checks (SPF/DMARC/DKIM)
- ✅ See URL analysis and suspicious links
- ✅ Access security tips and help
- ✅ Toggle dark mode

---

## 🛠️ Troubleshooting

### Backend Issues

#### Error: "Module not found: analyzer"
**Solution:** Make sure you're in `backend/` folder and the ML module path is correct.
```powershell
# Verify file structure
Get-ChildItem ..\ml\phishingtool\
```

#### Error: "Flask is not recognized"
**Solution:** Virtual environment isn't activated.
```powershell
# Activate venv
..\venv\Scripts\Activate.ps1
```

#### Error: "Port 5000 already in use"
**Solution:** Kill the process using port 5000 or use different port:
```powershell
# Find and kill process
Get-Process | Where-Object {$_.Name -like "*python*"} | Stop-Process -Force

# Or specify different port in main.py:
# app.run(host='127.0.0.1', port=5001)
```

#### Error: "Torch/Transformers installation fails"
**Solution:** Install size is large (~2GB for CUDA). Use CPU-only version:
```powershell
pip uninstall torch -y
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Frontend Issues

#### Error: "npm command not found"
**Solution:** Node.js not installed or not in PATH.
```powershell
# Check if npm is installed
npm --version

# If not, install from https://nodejs.org/
```

#### Error: "Port 5173 already in use"
**Solution:** Kill Vite process or use different port:
```powershell
Get-Process | Where-Object {$_.Name -like "*node*"} | Stop-Process -Force

# Or modify vite.config.js port
```

#### Dependencies installation is slow
**Solution:** Use alternative npm registry:
```powershell
npm install --registry https://registry.npmjs.org/
```

### Api Communication Issues

#### Frontend shows "Cannot reach server" error
**Solution:** Make sure:
1. ✅ Backend is running on `http://localhost:5000`
2. ✅ CORS is enabled (should be in main.py)
3. ✅ Check browser console (F12) for network errors

**In main.py, ensure CORS is initialized:**
```python
from flask_cors import CORS
CORS(app)
```

---

## 📁 Project File Structure Reminder

```
emailphishing/
├── backend/               # Flask API Server (port 5000)
│   ├── main.py           # Main Flask app
│   └── score_backend/
├── frontend/             # React UI (port 5173)
│   └── emailanalyzer/
│       ├── src/
│       ├── package.json
│       └── vite.config.js
├── ml/                   # Analysis engine
│   └── phishingtool/     # Core analyzers
├── data/                 # Test files
│   ├── sample.eml
│   └── email2.eml
├── utils/                # Utilities
├── uploads/              # Temp file storage
├── requirements.txt      # Python dependencies
└── venv/                 # Virtual environment (created by you)
```

---

## 🔄 Development Workflow

### Making Changes to Backend

1. Edit files in `backend/` or `ml/phishingtool/`
2. Flask auto-reloads on save (development mode)
3. Test with fresh email upload

### Making Changes to Frontend

1. Edit files in `frontend/emailanalyzer/src/`
2. Vite auto-refreshes on save
3. Changes visible immediately in browser

### Testing New Features

```powershell
# Run tests (if test_analyzer.py is configured)
cd utils
python test_analyzer.py
```

---

## 📝 Common Tasks

### Restart Backend
```powershell
# Ctrl+C to stop current process
# Then:
python main.py
```

### Restart Frontend
```powershell
# Ctrl+C to stop Vite server
# Then:
npm run dev
```

### Build Frontend for Production
```powershell
cd frontend\emailanalyzer
npm run build
# Creates dist/ folder with optimized files
```

### Clear Cache & Reinstall
```powershell
# Python
rm -r venv/
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Node
rm -r frontend/emailanalyzer/node_modules
cd frontend/emailanalyzer
npm install
```

---

## 🎯 Next Steps

1. ✅ Backend and frontend running
2. ✅ Test with sample .eml file
3. 📖 Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for architecture details
4. 🔧 Modify, test, and deploy as needed

---

## 📚 API Reference

### Available Endpoints

#### POST /analyze_email_route
Analyze an uploaded email file.

**Request:**
```
POST http://localhost:5000/analyze_email_route
Content-Type: multipart/form-data
file: <email.eml>
```

**Response:**
```json
{
  "overall_score": 72,
  "risk_level": "Suspicious",
  "from_address": "example@example.com",
  "to_address": "user@company.com",
  "spf": "pass",
  "dmarc": "fail",
  "dkim": "pass",
  "originating_ip": "192.168.1.1",
  "component_scores": {
    "body_analysis": 65,
    "url_analysis": 80,
    "header_analysis": 70
  }
}
```

#### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Email Phishing Analyzer with RoBERTa Model"
}
```

---

## 💡 Tips for Success

✅ **Always activate Python venv before running backend**
✅ **Keep both servers running simultaneously**
✅ **Test with provided sample .eml files first**
✅ **Check browser console (F12) for frontend errors**
✅ **Check PowerShell output for backend errors**
✅ **Clear browser cache if UI doesn't update**
✅ **Use different ports if defaults are busy**

---

**Now you're ready to run the Email Phishing Analyzer!** 🎉
