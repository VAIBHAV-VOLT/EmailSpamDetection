# Running the Email Phishing Analyzer

Multiple ways to start the application - choose what works best for you!

---

## 🚀 Method 1: Automated Scripts (Easiest)

### Option A: Windows Command Prompt (CMD)

**Double-click this file:**
```
run.bat
```

Or from command prompt:
```cmd
cd e:\Project\emailphishing\emailphishing
run.bat
```

**What it does:**
- ✅ Creates Python virtual environment (first run only)
- ✅ Installs dependencies
- ✅ Starts backend in new terminal window
- ✅ Starts frontend in new terminal window
- ✅ Opens browser to frontend

**Duration:** ~1-2 minutes (first run), ~20 seconds (subsequent runs)

---

### Option B: PowerShell

From PowerShell:
```powershell
cd e:\Project\emailphishing\emailphishing
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\run.ps1
```

**Same benefits as run.bat with better terminal formatting**

---

## 🔧 Method 2: Manual Setup (More Control)

For users who want to see what's happening at each step.

### Terminal 1: Backend Server

```powershell
# Navigate to project
cd e:\Project\emailphishing\emailphishing

# Create virtual environment (first time only)
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies (first time only)
pip install -r requirements.txt

# Navigate to backend
cd backend

# Run the server
python main.py
```

**Expected output:**
```
 * Serving Flask app 'main'
 * Debug mode: off
 * Running on http://127.0.0.1:5000
```

### Terminal 2: Frontend Server

**In a new PowerShell window:**

```powershell
# Navigate to frontend
cd e:\Project\emailphishing\emailphishing\frontend\emailanalyzer

# Install Node modules (first time only)
npm install

# Start development server
npm run dev
```

**Expected output:**
```
VITE v7.3.1
➜ local:   http://localhost:5173/
```

### Open in Browser
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000/health

---

## 🎯 Method 3: Docker (Production)

For containerized deployment:

```powershell
# Build image
docker build -t emailphishing:latest .

# Run container
docker run -p 5000:5000 -p 5173:5173 emailphishing:latest
```

---

## 📋 Comparison Table

| Method | Speed | Setup | Best For |
|--------|-------|-------|----------|
| **run.bat** | ⚡⚡⚡ | Auto | First-time users, quick start |
| **run.ps1** | ⚡⚡⚡ | Auto | PowerShell users |
| **Manual** | ⚡⚡ | Manual | Debugging, understanding flow |
| **Docker** | ⚡⚡⚡ | Manual | Production deployment |

---

## ✓ Verification Checklist

After starting the application, verify everything works:

### ✓ Backend Health Check
```powershell
# In PowerShell
$response = Invoke-WebRequest -Uri "http://localhost:5000/health" -UseBasicParsing
$response.Content
```

Should show:
```json
{"status": "healthy", "service": "Email Phishing Analyzer with RoBERTa Model"}
```

### ✓ Frontend Accessible
Open browser: http://localhost:5173

Should show the Email Analyzer UI

### ✓ API Connection
Upload a test email file and see results

---

## ⚠️ Troubleshooting Quick Fix

### Issue: "Module not found"
```powershell
# Ensure venv is activated
.\venv\Scripts\Activate.ps1
# Reinstall requirements
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
```powershell
# Kill Python process
Get-Process python | Stop-Process -Force
# Run again
python main.py
```

### Issue: "npm command not found"
```powershell
# Reinstall Node.js from https://nodejs.org/
# Or add to PATH in System Environment Variables
```

### Issue: Dependencies won't install
```powershell
# Clear pip cache and retry
pip install --no-cache-dir -r requirements.txt
```

---

## 🔄 Development Workflow

### Making Code Changes

**Backend:**
1. Edit files in `backend/` or `ml/phishingtool/`
2. Flask auto-reloads (development mode)
3. Test with fresh upload

**Frontend:**
1. Edit files in `frontend/emailanalyzer/src/`
2. Vite hot-reloads
3. Changes visible immediately in browser

### Testing Changes
```powershell
# Upload test file
# Use: data/sample.eml or data/email2.eml
# View results in browser
```

---

## 🛑 Stopping the Servers

### Method 1: Close Terminal Windows
Simply close the terminal windows for backend and frontend.

### Method 2: Ctrl+C
In each terminal window, press **Ctrl+C** to stop the server.

### Method 3: Kill Processes
```powershell
# Kill all Python processes
Get-Process python | Stop-Process -Force

# Kill all Node processes
Get-Process node | Stop-Process -Force
```

---

## 📦 Production Deployment

To build for production:

### Frontend Build
```powershell
cd frontend/emailanalyzer
npm run build
```

Creates optimized files in `dist/` folder.

### Backend in Production
Modify `backend/main.py`:
```python
# Change from:
if __name__ == '__main__':
    app.run(debug=True)

# To:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Use a production WSGI server:
```powershell
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

---

## 🎓 Learning Paths

### Just Want to Use It?
👉 **Use Method 1** (run.bat or run.ps1)

### Want to Understand the Code?
👉 **Use Method 2** (Manual) and read logs carefully

### Want to Deploy?
👉 **Use Method 3** (Docker) or setup production WSGI

---

## 📞 Common Questions

**Q: Do I need to reinstall dependencies every time?**
A: No, only on first run. After that, just activate venv and run.

**Q: Can I run just the backend or frontend?**
A: Yes, they're independent. Frontend still needs the API running.

**Q: How do I update the application?**
A: Update code, then restart the servers (Ctrl+C and run again).

**Q: Is it safe to ctrl+C the servers?**
A: Yes, it's safe. No data loss. Your files are still there.

**Q: How do I know if it's working?**
A: Visit http://localhost:5173 - if you see the UI, it's working!

---

**Next Steps:**
1. ✅ Choose a startup method
2. ✅ Run the application
3. ✅ Upload a test email
4. ✅ View the results
5. 📖 Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for details

**Happy analyzing! 🔍🚀**
