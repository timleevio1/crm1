from flask import Flask
from flask_cors import CORS
from routes.leads import leads_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(leads_bp)

if __name__ == '__main__':
    app.run(debug=True)