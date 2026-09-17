from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Flask!</h1><p>This is my first Flask application.</p>"

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>Learning Flask for Beginners.</p>"

@app.route("/contact")
def contact():
    return "<h2>Contact Page</h2><p>Email: student@example.com</p>"

if __name__ == "__main__":
    app.run(debug=True)