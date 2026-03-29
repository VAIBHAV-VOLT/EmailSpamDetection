# Email Phishing Analyzer - Project Structure

```
emailphishing/
│
├── backend/                          # Flask Web Server & Backend Services
│   ├── main.py                       # Main Flask application (HTTP server)
│   └── score_backend/                # Alternative/Legacy backend modules
│       ├── analyzer.py
│       ├── huggingface_analyzer.py
│       ├── infrastructure_analysis.py
│       ├── original_ip_analysis.py
│       ├── score_calculator.py
│       ├── security_check.py
│       └── url_analyzer.py
│
├── frontend/                         # React + Vite Frontend Application
│   ├── emailanalyzer/                # Main React app
│   │   ├── src/
│   │   │   ├── App.jsx
│   │   │   ├── main.jsx
│   │   │   ├── index.css
│   │   │   ├── assets/
│   │   │   ├── Components/           # React components
│   │   │   │   ├── CyberBackground.jsx
│   │   │   │   ├── DonutProgress.jsx
│   │   │   │   ├── FileUpload.jsx
│   │   │   │   ├── Header.jsx
│   │   │   │   ├── Loader.jsx
│   │   │   │   └── ResultCard.jsx
│   │   │   ├── Pages/                # Page components
│   │   │   │   ├── EmailAnalyzer.jsx
│   │   │   │   ├── Help.jsx
│   │   │   │   ├── SecurityTips.jsx
│   │   │   │   └── Upgrade.jsx
│   │   │   ├── context/              # React Context for state
│   │   │   │   └── DarkModeContext.jsx
│   │   │   └── mock/                 # Mock data
│   │   ├── public/                   # Static assets
│   │   ├── package.json
│   │   ├── vite.config.js
│   │   ├── eslint.config.js
│   │   ├── postcss.config.cjs
│   │   └── README.md
│   └── tailwind.config.js            # Tailwind CSS configuration
│
├── ml/                               # Machine Learning & Analysis Engine
│   └── phishingtool/                 # Core ML analysis module
│       ├── analyzer.py               # Main analyzer engine
│       ├── parser.py                 # Email parser
│       ├── huggingface_analyzer.py   # HuggingFace RoBERTa integration
│       ├── url_analyzer.py           # URL analysis
│       ├── url_ml_analyzer.py        # ML-based URL analysis
│       ├── url_checks.py             # URL validation checks
│       ├── attachment_checks.py      # Attachment analysis
│       ├── header_checks.py          # Email header validation
│       ├── auth_checks.py            # Authentication checks (SPF/DKIM/DMARC)
│       ├── domain_checks.py          # Domain validation
│       ├── infrastructure_checks.py  # Infrastructure analysis
│       ├── mime_checks.py            # MIME type validation
│       ├── timing_checks.py          # Timing analysis
│       ├── infrastructure_analysis.py
│       ├── original_ip_analysis.py
│       ├── score_calculator.py       # Scoring engine
│       ├── scoring.py                # Alternative scoring module
│       ├── profiler.py               # Performance profiling
│       ├── (demo files)              # Test/demo emails
│       └── phishing_assessment.json  # Assessment template
│
├── utils/                            # Utility Scripts & Tools
│   ├── add.py                        # Simple phishing risk checker
│   └── test_analyzer.py              # Testing utilities
│
├── data/                             # Test Data & Sample Files
│   ├── sample.eml                    # Sample email file
│   ├── email2.eml                    # Additional test email
│   ├── test.txt                      # Test data
│   └── phishing_assessment.json      # Sample assessment output
│
├── docs/                             # Documentation
│   └── README.md                     # Project documentation
│
├── uploads/                          # Runtime file storage
│   └── (uploaded .eml files)
│
├── requirements.txt                  # Python dependencies (root level)
├── .env                              # Environment configuration
├── .git/                             # Git version control
└── __pycache__/                      # Python cache
```

## Folder Descriptions

### **backend/**
Contains the Flask web server and REST API endpoints for email analysis.
- Main entry point: `main.py`
- Handles file uploads and API routing
- Integrates with ML and analysis modules

### **frontend/**
React + Vite based web UI for the email analyzer.
- Located in `emailanalyzer/` subdirectory
- Modern component-based architecture
- Dark mode support with Context API
- Tailwind CSS for styling

### **ml/**
Machine learning and email phishing analysis engine.
- Multiple check modules for comprehensive analysis:
  - Email header and authentication validation
  - URL analysis (static + ML-based)
  - Attachment analysis
  - Domain and infrastructure checks
  - Uses HuggingFace RoBERTa for body analysis

### **utils/**
Helper scripts and testing utilities.
- `add.py`: Basic phishing risk calculator
- `test_analyzer.py`: Testing and validation scripts

### **data/**
Test data, sample emails, and reference files.
- `.eml` files for testing
- JSON assessment samples

### **docs/**
Documentation and guides.
- Project README and usage instructions

### **uploads/**
Runtime directory for temporarily storing uploaded email files.

---

## Technology Stack

- **Backend**: Flask, Flask-CORS
- **Frontend**: React, Vite, Tailwind CSS
- **ML**: HuggingFace Transformers (RoBERTa)
- **Email Processing**: email-lib, email-validator
- **DNS Validation**: dnspython (SPF/DMARC/DKIM checks)
- **Architecture**: Modular microservice-like design

---

## Getting Started

### Backend Setup
```bash
cd backend
pip install -r ../requirements.txt
python main.py
```

### Frontend Setup
```bash
cd frontend/emailanalyzer
npm install
npm run dev
```

### ML Testing
```bash
from ml.phishingtool import analyzer
result = analyzer.analyze_email('sample.eml')
```
