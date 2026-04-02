#!/usr/bin/env python3
"""
Inference Service for Email Phishing Detection
Orchestrates the complete analysis pipeline using ML models and rule-based checks.
"""

import sys
import os
import importlib.util

# Add ML module to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ml', 'phishingtool'))
# Add backend utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    from preprocess import clean_text, truncate_text
except ImportError:
    from utils.preprocess import clean_text, truncate_text


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
        # Import ML modules with fallback handling
        try:
            from analyzer import analyze_email, load_email
            from infrastructure_analysis import analyze_received_headers
            from score_calculator import calculate_phishing_score, get_risk_level
        except (ImportError, ValueError) as import_err:
            # Try alternative import paths
            import importlib.util
            phishing_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'ml', 'phishingtool')
            
            # Load modules manually if standard imports fail
            spec_analyzer = importlib.util.spec_from_file_location("analyzer", os.path.join(phishing_dir, "analyzer.py"))
            analyzer_module = importlib.util.module_from_spec(spec_analyzer)
            spec_analyzer.loader.exec_module(analyzer_module)
            analyze_email, load_email = analyzer_module.analyze_email, analyzer_module.load_email
            
            spec_infra = importlib.util.spec_from_file_location("infrastructure_analysis", os.path.join(phishing_dir, "infrastructure_analysis.py"))
            infra_module = importlib.util.module_from_spec(spec_infra)
            spec_infra.loader.exec_module(infra_module)
            analyze_received_headers = infra_module.analyze_received_headers
            
            spec_score = importlib.util.spec_from_file_location("score_calculator", os.path.join(phishing_dir, "score_calculator.py"))
            score_module = importlib.util.module_from_spec(spec_score)
            spec_score.loader.exec_module(score_module)
            calculate_phishing_score, get_risk_level = score_module.calculate_phishing_score, score_module.get_risk_level
        
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
        try:
            from huggingface_analyzer import MODEL_NAME, MODEL_LOADED
        except (ImportError, ValueError):
            import importlib.util
            phishing_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'ml', 'phishingtool')
            spec = importlib.util.spec_from_file_location("huggingface_analyzer", os.path.join(phishing_dir, "huggingface_analyzer.py"))
            hf_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(hf_module)
            MODEL_NAME = getattr(hf_module, 'MODEL_NAME', 'unknown')
            MODEL_LOADED = getattr(hf_module, 'MODEL_LOADED', False)
        
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
