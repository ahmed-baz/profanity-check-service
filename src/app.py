from service import clear_text,check_profanity
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# API endpoint 1
@app.route('/api/v1/profanity-check', methods=['POST'])
def check_profanity_api():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if 'text' is in the request data
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    # Extract the text from the request
    text = data['text']
    
    # Check for profanity
    result = check_profanity(text)
    
    # Return the result as a JSON response
    return jsonify({'profanity': result})


# API endpoint 2
@app.route('/api/v1/clear-profanity', methods=['POST'])
def clear_text_api():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if 'text' is in the request data
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    # Extract the text from the request
    text = data['text']
    
    # clear profanity text
    result = clear_text(text)
    
    # Return the result as a JSON response
    return jsonify({'text': result})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
