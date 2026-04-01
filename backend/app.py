#!/usr/bin/env python3
"""
EmailSpamDetection - Flask Application Setup
Initializes Flask app with CORS and configuration.
"""

import os
from flask import Flask
from flask_cors import CORS


def create_app(config=None):
    """
    Application factory for creating Flask app.
    
    :param config: Optional config dict
    :return: Flask app instance
    """
    app = Flask(__name__)
    CORS(app)
    
    # Configuration
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    # Create upload folder
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # Apply custom config if provided
    if config:
        app.config.update(config)
    
    # Register blueprints
    from routes.predict import predict_bp
    app.register_blueprint(predict_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
