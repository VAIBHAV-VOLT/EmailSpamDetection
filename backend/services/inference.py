#!/usr/bin/env python3
"""
Inference Service for Email Phishing Detection
Orchestrates the complete analysis pipeline using ML models and rule-based checks.
"""

import sys
import os
import importlib.util

# Resolve paths
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
utils_dir = os.path.join(backend_dir, 'utils')
ml_phishing_dir = os.path.join(os.path.dirname(backend_dir), 'ml', 'phishingtool')

# Load modules from specific directories
def load_module_from_path(module_name, module_path):
    """Load a Python module from a specific file path"""
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load backend utils module
preprocess_module = load_module_from_path('preprocess', os.path.join(utils_dir, 'preprocess.py'))
clean_text = preprocess_module.clean_text
truncate_text = preprocess_module.truncate_text

# Load ml.phishingtool modules
email_analyzer_module = load_module_from_path('email_analyzer', os.path.join(ml_phishing_dir, 'email_analyzer.py'))
analyze_email = email_analyzer_module.analyze_email
load_email = email_analyzer_module.load_email

infra_module = load_module_from_path('infrastructure_analysis', os.path.join(ml_phishing_dir, 'infrastructure_analysis.py'))
analyze_received_headers = infra_module.analyze_received_headers

score_module = load_module_from_path('score_calculator', os.path.join(ml_phishing_dir, 'score_calculator.py'))
calculate_phishing_score = score_module.calculate_phishing_score
get_risk_level = score_module.get_risk_level

huggingface_module = load_module_from_path('huggingface_analyzer', os.path.join(ml_phishing_dir, 'huggingface_analyzer.py'))
MODEL_NAME = huggingface_module.MODEL_NAME
MODEL_LOADED = huggingface_module.MODEL_LOADED


def predict_phishing(email_file_path):
    """
    Run complete phishing detection analysis on an email file.
    
    This function orchestrates:
    1. Email parsing and metadata extraction
    2. URL and infrastructure analysis
    3. Authentication checks (SPF/DKIM/DMARC)
    4. ML-based text analysis with HuggingFace model
    5. Comprehensive risk scoring
    
    :param email_file_path: Path to .eml email file
    :return: Dictionary with analysis results
    """
    try:
        # Step 1: Load and parse email
        msg = load_email(email_file_path)
        email_analysis = analyze_email(email_file_path)
        
        # Step 2: Get metadata
        metadata = email_analysis.get("metadata", {})
        body = email_analysis.get("body", "")
        
        # Step 3: Analyze infrastructure and IP
        ip_analysis = analyze_received_headers(msg)
        
        # Step 4: Calculate comprehensive phishing score
        phishing_score = calculate_phishing_score(email_analysis, ip_analysis)
        
        # Step 5: Structure response
        response = {
            "status": "success",
            "analysis": {
                "overall_score": phishing_score.get("overall_score"),
                "risk_level": phishing_score.get("risk_level"),
                "email_metadata": {
                    "from": metadata.get("from"),
                    "to": metadata.get("to"),
                    "subject": metadata.get("subject"),
                    "date": metadata.get("date")
                },
                "security_checks": {
                    "spf": phishing_score.get("spf"),
                    "dkim": phishing_score.get("dkim"),
                    "dmarc": phishing_score.get("dmarc"),
                    "originating_ip": phishing_score.get("originating_ip")
                },
                "component_scores": phishing_score.get("component_scores", {}),
                "details": phishing_score.get("details", {})
            }
        }
        
        return response
    
    except Exception as e:
        # Return error response
        return {
            "status": "error",
            "error": str(e)
        }


def preprocess_email_text(text):
    """
    Preprocess email text for ML model input.
    
    :param text: Raw email text
    :return: Cleaned and prepared text
    """
    # Clean text
    cleaned = clean_text(text)
    
    # Truncate to model max length
    processed = truncate_text(cleaned, max_length=512)
    
    return processed


def get_model_info():
    """
    Get information about the loaded ML models.
    
    :return: Dictionary with model details
    """
    try:
        return {
            "transformer_model": MODEL_NAME,
            "transformer_loaded": MODEL_LOADED,
            "status": "ready" if MODEL_LOADED else "warning"
        }
    except:
        return {
            "transformer_model": "unknown",
            "transformer_loaded": False,
            "status": "error"
        }
