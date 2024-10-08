from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

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
            description: Text to be converted to uppercase
        responses:
          200:
            description: Successfully converted text
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    text:
                      type: string
                      description: Uppercase version of the text
        """
        text = request.args.get('text', '').strip()  # Safely handle empty input
        if not text:
            return jsonify({"error": "Text is required"}), 400

        return jsonify({"text": text.upper()})

api.add_resource(UppercaseText, "/uppercase")

if __name__ == "__main__":
    app.run(debug=True)