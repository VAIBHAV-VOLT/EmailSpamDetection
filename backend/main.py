#!/usr/bin/env python3
"""
EmailSpamDetection - Entry Point
Uses the modular Flask application factory from app.py
"""

from app import create_app


if __name__ == "__main__":
    print("🚀 Starting EmailSpamDetection Web Server")
    print("📊 Modular Architecture:")
    print("   ├── app.py: Flask application setup")
    print("   ├── routes/predict.py: API endpoints")
    print("   ├── services/inference.py: Phishing detection logic")
    print("   └── utils/preprocess.py: Text preprocessing")
    print("📱 Analyze emails: POST http://localhost:5000/api/analyze_email")
    print("💚 Health check: GET http://localhost:5000/api/health")
    print("Press CTRL+C to stop the server\n")
    
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)