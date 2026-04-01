# Backend Refactoring Guide

## Summary

The EmailSpamDetection backend has been refactored from a monolithic `main.py` structure into a clean, modular architecture following best practices for Flask applications.

## New Backend Structure

```
backend/
├── app.py                      # ✨ NEW - Flask app factory
├── main.py                     # Updated - Entry point using app.py
├── ARCHITECTURE.md             # ✨ NEW - Architecture documentation
│
├── routes/                     # ✨ NEW - API endpoints
│   ├── __init__.py
│   └── predict.py              # ✨ NEW - Email analysis routes
│
├── services/                   # ✨ NEW - Business logic
│   ├── __init__.py
│   └── inference.py            # ✨ NEW - Phishing detection orchestration
│
├── utils/                      # ✨ NEW - Utility functions
│   ├── __init__.py
│   └── preprocess.py           # ✨ NEW - Text cleaning & preprocessing
│
├── models/                     # ✨ NEW - Model storage directory
│   └── .gitkeep
│
└── score_backend/              # Existing - Keep for compatibility
    └── (legacy modules)
```

## Responsibilities per Module

| Module | Purpose | Contains |
|--------|---------|----------|
| `app.py` | Flask Setup | Factory function, CORS, config |
| `routes/predict.py` | HTTP Layer | Request validation, response serialization |
| `services/inference.py` | Business Logic | Orchestrates analysis pipeline |
| `utils/preprocess.py` | Utilities | Text cleaning, URL/email extraction |
| `models/` | Storage | Trained models, vectorizers, artifacts |

## API Endpoint Changes

### Old Endpoint (Deprecated)
```
POST /analyze_email_route
```

### New Endpoint (Recommended)
```
POST /api/analyze_email
```

### Migration Checklist for Frontend

- [ ] Update API endpoint from `/analyze_email_route` to `/api/analyze_email`
- [ ] Update response parsing if needed (structure is improved but compatible)
- [ ] Test file upload functionality
- [ ] Verify response displays correctly in UI

### Response Comparison

**Old Response Format:**
```json
{
  "overall_score": 7.5,
  "risk_level": "HIGH",
  "from_address": "...",
  ...
}
```

**New Response Format (Enhanced):**
```json
{
  "status": "success",
  "analysis": {
    "overall_score": 7.5,
    "risk_level": "HIGH",
    "email_metadata": {
      "from": "...",
      "to": "...",
      ...
    },
    "security_checks": {
      "spf": true,
      "dkim": false,
      ...
    },
    ...
  }
}
```

## Key Improvements

✅ **Separation of Concerns** - Each module has one responsibility  
✅ **Testability** - Easy to unit test individual components  
✅ **Maintainability** - Clear code organization  
✅ **Scalability** - Easy to add new features  
✅ **Reusability** - Utilities can be used across modules  
✅ **Documentation** - Architecture documented in ARCHITECTURE.md  

## Running the Server

```bash
# Option 1: Using main.py (recommended entry point)
python backend/main.py

# Option 2: Using Flask's app factory
python -m flask --app backend.app run

# Option 3: Using app.py directly
python backend/app.py
```

## Development Workflow

### Adding a New Route

1. Create a new function in `routes/predict.py` or a new file like `routes/other.py`
2. Register with Flask Blueprint in `routes/__init__.py`
3. Register blueprint in `app.py`

### Adding a New Service

1. Create a function in `services/inference.py` or a new file
2. Import and use in routes

### Adding a Utility Function

1. Add function to `utils/preprocess.py`
2. Import where needed: `from utils.preprocess import function_name`

## Integration Points

The new modular structure integrates with existing ML modules:

```
backend/
  ├── app.py
  ├── routes/predict.py         ──┐
  ├── services/inference.py      ──┼──> ml/phishingtool/
  └── utils/preprocess.py        ──┘
      (imports and orchestrates)
```

## Next Steps

1. **Update Frontend**: Change API endpoint references
2. **Add Tests**: Create `tests/` directory with unit tests
3. **Add Logging**: Integrate logging across modules
4. **Add Caching**: Consider caching for model initialization
5. **Add Validation**: Add Pydantic models for request/response validation

## Questions or Issues?

Refer to `backend/ARCHITECTURE.md` for detailed module information.
