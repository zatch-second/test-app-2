from flask import Flask
import os

app = Flask(__name__)

# We will change this to 'green' in our next lesson!
BG_COLOR = os.environ.get("BG_COLOR", "blue") 
VERSION = "1.0 - Blue Release"

@app.route('/')
def home():
    return f"""
    <html>
        <body style="background-color: {BG_COLOR}; color: white; text-align: center; padding: 50px; font-family: sans-serif;">
            <h1>DevOps Status Dashboard</h1>
            <h2>Version: {VERSION}</h2>
            <p>Running beautifully on Kubernetes via Jenkins!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)