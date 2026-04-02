#!/usr/bin/env python3
"""
Email Analysis Route Handler
Handles POST requests for email file upload and analysis.
"""

import os
import json
from datetime import datetime
from flask import Blueprint, request, jsonify, current_app
from services.inference import predict_phishing

# Create blueprint
predict_bp = Blueprint('predict', __name__, url_prefix='/api')


@predict_bp.route('/analyze_email', methods=['POST'])
def analyze_email():
    """
    Analyze uploaded email file for phishing risk.
    
    Request:
        - file: .eml format email file
    
    Response:
        - JSON with phishing analysis results
    """
    try:
        # Validate file upload
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.eml'):
            return jsonify({
                'error': 'Invalid file format. Please upload a .eml file'
            }), 400
        
        # Save uploaded file temporarily
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        temp_filename = f"temp_{timestamp}_{file.filename}"
        temp_path = os.path.join(
            current_app.config['UPLOAD_FOLDER'], 
            temp_filename
        )
        file.save(temp_path)
        
        try:
            # Run inference
            analysis_result = predict_phishing(temp_path)
            
            if analysis_result:
                # Save analysis result to JSON file
                output_filename = f"analysis_{timestamp}_{file.filename.replace('.eml', '')}.json"
                output_path = os.path.join(
                    current_app.config['UPLOAD_FOLDER'], 
                    output_filename
                )
                
                try:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(analysis_result, f, indent=2, ensure_ascii=False)
                    
                    # Add file path to response
                    analysis_result['output_file'] = output_filename
                    analysis_result['output_path'] = output_path
                except Exception as write_err:
                    print(f"Warning: Failed to save JSON output file: {str(write_err)}")
                
                return jsonify(analysis_result), 200
            else:
                return jsonify({
                    'error': 'Failed to analyze email'
                }), 500
        
        except Exception as e:
            return jsonify({
                'error': f'Analysis error: {str(e)}'
            }), 500
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except:
                    pass
    
    except Exception as e:
        return jsonify({
            'error': f'Request error: {str(e)}'
        }), 500


@predict_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    Response:
        - JSON with status
    """
    return jsonify({'status': 'healthy'}), 200
