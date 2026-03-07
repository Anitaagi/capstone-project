from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Capstone project backend is running!"

@app.route('/api/status')
def status():
    return {
        "status": "Backend working",
        "service": "capstone project"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)