from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)

# Enable CORS for all domains
CORS(app)

# Configure the Gemini API key
genai.configure(api_key='AIzaSyBVm7TTYQULz20ljckXk7xKaB8CUi1NjLw')

def get_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_input)

        if hasattr(response, 'candidates') and len(response.candidates) > 0:
            # Returning a more detailed and user-friendly response
            return f"Here's the detailed answer:\n\n{response.candidates[0].content.parts[0].text.strip()}"

        return f"I couldn't find the exact answer, but here's something that might help:\n\n{response.text.strip()}"
    except Exception as e:
        return f"Sorry, something went wrong. Error: {e}"

@app.route('/chat', methods=['POST'])
def chat():
    # Get message from frontend
    user_message = request.json.get('message')

    # Get response from Gemini AI
    response = get_response(user_message)

    # Return the response as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Ensure Flask listens on the correct host and port
