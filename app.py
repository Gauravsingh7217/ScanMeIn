from flask import Flask, redirect, url_for, render_template
import subprocess

app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    # Redirect to the main page
    return render_template('index.html')

# Route to launch main.py
@app.route('/main')
def launch_main():
    try:
        # Run main.py using subprocess
        subprocess.Popen(["python", "main.py"])
        return "Main.py is running. Please check the Tkinter window.", 200
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

