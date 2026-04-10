import sys
import os
from dotenv import load_dotenv

# Add ml/phishingtool to Python path FIRST, before any other imports
ml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ml/phishingtool'))
if ml_path not in sys.path:
    sys.path.insert(0, ml_path)

# Now import google genai
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

# Initialize the client lazily (only when needed)
_client = None


def _get_client():
    """Get or initialize the Gemini AI client"""
    global _client
    if _client is None:
        api_key = os.environ.get("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not found in environment variables. Please check your .env file.")
        _client = genai.Client(api_key=api_key)
    return _client


def analyze_with_ai(originating_ip):
    """
    Analyze an originating IP using Gemini AI to determine if it's related to phishing.

    :param originating_ip: the IP address to analyze
    :return: dict with originating_ip and phishing result (True/False)
    """
    model = "gemini-2.0-flash"
    contents = [
        types.Content(role="user", parts=[types.Part.from_text(text=f"Please tell me if the following ip address is related to phishing through emails.\nip:\n{originating_ip}\n\nAnswer only in yes or no in lower case")]), 
    ]

    generate_content_config = types.GenerateContentConfig()

    response_text = ""
    try:
        for chunk in client.models.generate_content_stream(
            model=model, contents=contents, config=generate_content_config
        ):
            response_text += chunk.text
    except Exception as e:
        return {"error": str(e)}
    
    is_phishing = response_text.lower().strip() == 'yes'

    return {
        "originating_ip": originating_ip,
        'phishing': is_phishing,
        'ai_response': response_text
    }


def analyze(data):
    """
    Analyze email data with IPs using AI.

    :param data: dict with 'ips' and 'originating_ip' keys
    :return: analysis result
    """
    ips = data.get('ips', '')
    original = data.get('originating_ip', '')

    if not original:
        return {"error": "No originating IP provided"}

    return analyze_with_ai(original)
