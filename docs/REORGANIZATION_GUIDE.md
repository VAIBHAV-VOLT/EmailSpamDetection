# Email Phishing Analyzer

A comprehensive email phishing detection system using Machine Learning and security analysis.

## 🚀 Quick Start

### Project Structure

The project is now organized into clear modules for easy maintenance and scalability:

```
emailphishing/
├── backend/          # Flask API Server
├── frontend/         # React Web Interface
├── ml/              # Machine Learning Engine
├── utils/           # Utility Scripts
├── data/            # Test Data & Samples
├── docs/            # Documentation
└── uploads/         # Uploaded Files
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed folder descriptions.

### Setup Instructions

#### 1. Backend Setup (Flask API)
```bash
cd backend
pip install -r ../requirements.txt
python main.py
```
The API will start on `http://localhost:5000`

#### 2. Frontend Setup (React)
```bash
cd frontend/emailanalyzer
npm install
npm run dev
```
The web UI will open on `http://localhost:5173`

## 📋 Features

- **ML-Based Analysis**: HuggingFace RoBERTa model for email body analysis
- **Security Checks**: SPF, DMARC, DKIM validation
- **URL Analysis**: Suspicious URL detection with ML assistance
- **Metadata Review**: Email header and attachment analysis
- **Infrastructure Analysis**: Originating IP analysis
- **Real-time Scoring**: Comprehensive phishing risk assessment

## 🔧 Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18, Vite, Tailwind CSS |
| **Backend** | Flask, CORS |
| **ML/AI** | HuggingFace Transformers, scikit-learn |
| **Email Processing** | Python email library, dnspython |
| **Database** | JSON-based assessment files |

## 📁 Key Files

- `backend/main.py` - Flask server with email analysis endpoints
- `frontend/emailanalyzer/src/App.jsx` - Main React application
- `ml/phishingtool/analyzer.py` - Core analysis engine
- `requirements.txt` - Python dependencies

## 🧪 Testing

Test files and sample emails are available in the `data/` folder:
- `data/sample.eml` - Sample email for testing
- `data/email2.eml` - Additional test case
- `utils/test_analyzer.py` - Test utilities

## 📚 Documentation

- Full API documentation and architecture details: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- Frontend development guide: [frontend/emailanalyzer/README.md](frontend/emailanalyzer/README.md)

## 🛠️ Development

### Adding New Features

1. **Backend Route**: Add endpoint in `backend/main.py`
2. **Analysis Module**: Extend `ml/phishingtool/` modules
3. **Frontend Component**: Create component in `frontend/emailanalyzer/src/Components/`

### Code Organization

- **Business Logic**: `ml/phishingtool/`
- **API Layer**: `backend/main.py`
- **UI Layer**: `frontend/emailanalyzer/src/`
- **Helpers**: `utils/`

## 📝 Environment Variables

Create a `.env` file in the root directory:
```
FLASK_ENV=development
FLASK_DEBUG=True
```

## 🔐 Security Notes

- The application validates file types (.eml only)
- File uploads are temporary and auto-cleaned
- CORS is configured for frontend communication
- All email files should be treated as sensitive data

## 📞 Support

For issues or questions, refer to the documentation in `docs/` folder.

---

**Last Updated**: March 2026
