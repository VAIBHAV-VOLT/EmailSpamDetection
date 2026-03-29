# ⚡ Quick Start (5 Minutes)

The fastest way to get the email phishing analyzer running.

## Prerequisites ✓
- Python 3.8+ installed
- Node.js 16+ installed
- This project

---

## Step 1: Setup Backend (2 min)

**Terminal 1:**
```powershell
cd e:\Project\emailphishing\emailphishing\backend

# Create & activate Python environment
python -m venv ..\venv
..\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r ..\requirements.txt

# Run backend
python main.py
```

**Wait for:** `Running on http://127.0.0.1:5000`

---

## Step 2: Setup Frontend (2 min)

**Terminal 2:**
```powershell
cd e:\Project\emailphishing\emailphishing\frontend\emailanalyzer

# Install Node dependencies
npm install

# Start frontend
npm run dev
```

**Wait for:** `Running on http://localhost:5173`

---

## Step 3: Test It! (1 min)

1. Browser automatically opens frontend
2. Click "Upload Email"
3. Select: `..\..\data\sample.eml`
4. View results!

---

## Done! 🎉

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5000/health

For detailed instructions, see [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md)
