# 📚 Documentation Index

Complete guide to all documentation for the Email Phishing Analyzer project.

---

## 🚀 Getting Started (Pick One)

### For Beginners - Start Here!
👉 **[QUICKSTART.md](QUICKSTART.md)** - 5 minutes
- Super fast setup
- Copy-paste commands
- Minimal explanation
- Perfect for first-time users

### For Detailed Setup
👉 **[RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md)** - 10-15 minutes
- Step-by-step walkthrough
- Troubleshooting built-in
- Explanation of each step
- Prerequisites checklist

### For All Options
👉 **[RUNNING_METHODS.md](RUNNING_METHODS.md)** - Reference
- 4 different ways to run
- Docker support
- Production deployment
- Development workflow

---

## 📖 Understanding the Project

### Project Overview
👉 **[README.md](README.md)** - Main documentation
- Features & capabilities
- Technology stack
- Architecture diagram
- Quick links to everything

### Project Structure
👉 **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Deep dive
- Detailed folder breakdown
- File descriptions
- Module purposes
- Technology explanations

### Organization Guide
👉 **[REORGANIZATION_GUIDE.md](REORGANIZATION_GUIDE.md)** - Background
- Original vs new structure
- Why files were moved
- Folder organization logic

---

## ⚡ Quick Reference

| Need | Document | Time |
|------|----------|------|
| **Just start it** | [QUICKSTART.md](QUICKSTART.md) | 5 min |
| **Understand how** | [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md) | 15 min |
| **See all options** | [RUNNING_METHODS.md](RUNNING_METHODS.md) | 5 min |
| **Know the structure** | [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | 10 min |
| **Full context** | [README.md](README.md) | 20 min |

---

## 📋 Documentation Breakdown

### QUICKSTART.md ⚡
**5-minute quick start**

Contents:
- ✅ Prerequisites check
- ✅ Backend setup (copy-paste)
- ✅ Frontend setup (copy-paste)
- ✅ Test it
- ✅ Done!

**Best for**: First-time users, quick launch

---

### RUNNING_INSTRUCTIONS.md 📖
**Comprehensive detailed guide**

Contents:
- Prerequisites with links
- Python virtual environment setup
- Node.js installation
- Terminal 1: Backend setup & run
- Terminal 2: Frontend setup & run
- Health checks
- API testing
- **Complete troubleshooting section**
- Common tasks (restart, clear cache, etc.)
- Development workflow
- Production build

**Best for**: Understanding every step, fixing issues

---

### RUNNING_METHODS.md 🔄
**All ways to run the application**

Contents:
- **Method 1**: Automated scripts (run.bat / run.ps1)
- **Method 2**: Manual setup (terminal commands)
- **Method 3**: Docker (containerized)
- Comparison table
- Verification checklist
- Development workflow
- FAQ section
- Learning paths

**Best for**: Choosing the right setup method, reference

---

### PROJECT_STRUCTURE.md 🏗️
**Deep dive into project architecture**

Contents:
- Detailed folder structure (ASCII tree)
- Each folder explained
- File descriptions
- Technology stack
- Getting started per component
- Architecture overview

**Best for**: Understanding the codebase, code contributions

---

### README.md 📚
**Main project documentation**

Contents:
- Feature overview
- System requirements
- Architecture diagram
- Project structure summary
- All 3 startup options
- Testing instructions
- How it works (pipeline)
- Technology stack
- API reference
- Troubleshooting
- Deployment info
- Learning resources

**Best for**: Complete overview, reference document

---

### REORGANIZATION_GUIDE.md 📋
**Project reorganization explanation**

Contents:
- Reason for reorganization
- Setup instructions
- Module descriptions
- Technology stack
- Getting started for each module
- Development guide

**Best for**: Understanding why structure changed, background

---

## 🗂️ File Structure

```
docs/
├── README.md                      # ← Start here (main docs)
├── QUICKSTART.md                  # ← Super fast setup (5 min)
├── RUNNING_INSTRUCTIONS.md        # ← Detailed guide (15 min)
├── RUNNING_METHODS.md             # ← All options + comparison
├── PROJECT_STRUCTURE.md           # ← Code organization
├── REORGANIZATION_GUIDE.md        # ← Why files moved
└── DOCUMENTATION_INDEX.md         # ← This file
```

---

## 🎯 Usage Flows

### "I'm New - Just Start It"
1. Read: [QUICKSTART.md](QUICKSTART.md) (5 min)
2. Run: `run.bat` or `run.ps1`
3. Test: Upload `data/sample.eml`
4. ✅ Done!

### "I Want to Understand Everything"
1. Read: [README.md](README.md) (20 min)
2. Read: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) (10 min)
3. Run: [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md) (follow steps)
4. Explore: Browse code in each folder
5. ✅ Ready to contribute!

### "I Know What I'm Doing"
1. Skim: [RUNNING_METHODS.md](RUNNING_METHODS.md) (find your method)
2. Run: Use preferred method
3. ✅ Let's go!

### "I Need Production Setup"
1. Read: [README.md](README.md) → Deployment section
2. Read: [RUNNING_METHODS.md](RUNNING_METHODS.md) → Production Deployment
3. Follow: Deployment checklist
4. ✅ Ready to deploy!

### "Something's Broken"
1. Check: [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md) → Troubleshooting
2. Try: Common fixes
3. If not fixed: Check [RUNNING_METHODS.md](RUNNING_METHODS.md) → Verify Checklist
4. ✅ Issue resolved!

---

## 🔗 Quick Links

### To Run the Application
- **Automated**: Double-click `run.bat` or `.\run.ps1`
- **Backend only**: `cd backend && python main.py`
- **Frontend only**: `cd frontend/emailanalyzer && npm run dev`
- **Docker**: `docker run -p 5000:5000 -p 5173:5173 emailphishing:latest`

### To Test
- Upload: `data/sample.eml`
- API: `http://localhost:5000/health`
- UI: `http://localhost:5173`

### To Develop
- Backend files: `backend/` and `ml/phishingtool/`
- Frontend files: `frontend/emailanalyzer/src/`
- Test files: `utils/test_analyzer.py`
- Sample data: `data/`

---

## 📚 Learning Path

### Beginner
1. **Quickstart** (5 min) → Get it running
2. **README** (20 min) → Understand features
3. **Run Methods** (5 min) → Know your options

### Intermediate
1. **Project Structure** (10 min) → Know the code layout
2. **Running Instructions** (15 min) → Fix any issues
3. **Explore code** (30 min) → Navigate the files

### Advanced
1. **Source code** → Deep dive into implementation
2. **API code** → Understand backend logic
3. **ML modules** → Learn analysis pipeline
4. **Frontend** → React components

---

## 🆘 Troubleshooting Quick Links

**Problem** → **Read This**

- Backend won't start → [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md#backend-issues)
- Frontend won't start → [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md#frontend-issues)
- API communication fails → [RUNNING_INSTRUCTIONS.md](RUNNING_INSTRUCTIONS.md#api-communication-issues)
- Dependencies won't install → [RUNNING_METHODS.md](RUNNING_METHODS.md#issue-dependencies-wont-install)
- Port already in use → [RUNNING_METHODS.md](RUNNING_METHODS.md#issue-port-5000-already-in-use)

---

## 📊 Documentation Statistics

| Document | Size | Read Time | Best For |
|----------|------|-----------|----------|
| QUICKSTART.md | Short | 5 min | First launch |
| RUNNING_INSTRUCTIONS.md | Long | 15 min | Detailed setup |
| RUNNING_METHODS.md | Long | 10 min | Choosing method |
| PROJECT_STRUCTURE.md | Medium | 10 min | Code nav |
| README.md | Medium | 20 min | Full overview |
| REORGANIZATION_GUIDE.md | Short | 5 min | Background |

---

## ✨ Pro Tips

💡 **Read QUICKSTART.md first** - Gets you running fastest

💡 **Bookmark RUNNING_INSTRUCTIONS.md** - Best for troubleshooting

💡 **Reference PROJECT_STRUCTURE.md** - When exploring code

💡 **Share README.md** - Great for onboarding others

💡 **Use RUNNING_METHODS.md** - When choosing setup method

---

## 🎓 Key Concepts

### Startup Methods
- **Automated** (run.bat/run.ps1) - Fastest, sets everything up
- **Manual** - More control, see what's happening
- **Docker** - Containerized, production-ready

### Project Areas
- **Backend** (Flask API) - Port 5000
- **Frontend** (React UI) - Port 5173
- **ML** (Analysis Engine) - Python modules
- **Data** (Test Files) - Sample emails

### Key Files
- `run.bat` / `run.ps1` - Startup scripts
- `backend/main.py` - Flask server
- `ml/phishingtool/analyzer.py` - Core analysis
- `frontend/emailanalyzer/src/App.jsx` - React app

---

## 📞 Getting Help

1. **Check documentation** - You're here! 📚
2. **Search your issue** - Likely covered
3. **Check troubleshooting section** - Common fixes
4. **Try recommended fixes** - Usually works
5. **Review project structure** - Understand the setup

---

**Last Updated:** March 29, 2026

**Start here:** [QUICKSTART.md](QUICKSTART.md) ⚡
