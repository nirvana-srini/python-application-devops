from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Hello from your EC2 Python App deployed via AWS SSM!",
        "version": "1.0.0"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Runs the app locally or on the server production port
    app.run(host='0.0.0.0', port=8080)
