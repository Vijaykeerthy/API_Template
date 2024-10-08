from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

def convert_to_uppercase(text):
    """
    Converts the input text to uppercase.
    """
    return text.upper()

class UppercaseText(Resource):
    def get(self):
        """
        Convert provided text to uppercase.
        ---
        tags:
          - Text Processing
        parameters:
          - name: text
            in: query
            type: string
            required: true
            description: The text to convert to uppercase
        responses:
          200:
            description: Successfully converted text
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    original_text:
                      type: string
                      description: The original input text
                    uppercase_text:
                      type: string
                      description: The text in uppercase
          400:
            description: Input text is missing
        """
        text = request.args.get('text', '').strip()  # Safely handle empty input

        if not text:
            return jsonify({"error": "Text is required"}), 400

        uppercase_text = convert_to_uppercase(text)

        response = {
            'original_text': text,
            'uppercase_text': uppercase_text
        }

        return jsonify(response)

# Adding the resource to the API
api.add_resource(UppercaseText, "/uppercase")

if __name__ == "__main__":
    app.run(debug=True)
