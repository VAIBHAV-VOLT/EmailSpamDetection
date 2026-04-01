# Backend Architecture

## New Modular Structure

The backend has been refactored into a clean, maintainable modular architecture:

```
backend/
├── app.py                    # Flask application factory
├── routes/
│   ├── __init__.py
│   └── predict.py           # Email analysis API endpoints
├── services/
│   ├── __init__.py
│   └── inference.py         # Phishing detection orchestration
├── utils/
│   ├── __init__.py
│   └── preprocess.py        # Text cleaning & preprocessing
├── models/                  # Model storage directory
│   └── .gitkeep
└── main.py                  # Entry point (updated to use app.py)
```

## Module Responsibilities

### `app.py`
- Flask application factory (`create_app()`)
- CORS configuration
- Error handling setup
- Blueprint registration
- **Zero business logic**

### `routes/predict.py`
- HTTP request/response handling
- File upload validation
- Request parsing
- Response serialization
- Calls `services.inference.predict_phishing()`

### `services/inference.py`
- Orchestrates the complete analysis pipeline
- Coordinates with ML modules (`ml/phishingtool`)
- Integrates score calculation
- Data transformation and aggregation
- **Core business logic**

### `utils/preprocess.py`
- Text cleaning functions
- URL extraction
- Email address extraction
- Domain extraction
- Keyword detection
- Text tokenization and truncation
- **Reusable utility functions**

### `models/`
- Directory for storing trained models
- Serialized model artifacts
- Vectorizers and encoders

## API Endpoints

### `POST /api/analyze_email`
Analyze an uploaded email file for phishing risk.

**Request:**
```
Content-Type: multipart/form-data
Body: file (binary .eml file)
```

**Response:**
```json
{
  "status": "success",
  "analysis": {
    "overall_score": 7.5,
    "risk_level": "HIGH",
    "email_metadata": {
      "from": "example@domain.com",
      "to": "user@example.com",
      "subject": "Important Update",
      "date": "2024-01-15T10:30:00Z"
    },
    "security_checks": {
      "spf": true,
      "dkim": false,
      "dmarc": true,
      "originating_ip": "192.168.1.1"
    },
    "component_scores": {
      "url_security_score": 8.0,
      "transformer_score": 6.5,
      "metadata_score": 7.0,
      "ip_score": 5.0
    },
    "details": {
      "header_mismatch": false,
      "domain_mismatch": false,
      "total_ips_found": 3
    }
  }
}
```

### `GET /api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Running the Backend

```bash
# Option 1: Using app.py factory
python -m flask --app backend.app run

# Option 2: Using main.py (entry point)
python backend/main.py

# Option 3: Using app.py directly
python backend/app.py
```

## Integration with ML Modules

The `services/inference.py` file integrates with the existing ML modules:
- `ml/phishingtool/analyzer.py` - Email parsing
- `ml/phishingtool/score_calculator.py` - Comprehensive scoring
- `ml/phishingtool/huggingface_analyzer.py` - Transformer model
- `ml/phishingtool/infrastructure_analysis.py` - IP analysis

## Key Features

✅ **Clean Separation of Concerns** - Each module has a single responsibility  
✅ **Testable** - Easy to write unit tests for each component  
✅ **Maintainable** - Clear code organization and documentation  
✅ **Scalable** - Easy to add new routes, services, or preprocessing steps  
✅ **Reusable** - Utility functions can be used across different modules  
