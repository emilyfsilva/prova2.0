from flask import Flask
app = Flask (__name__)

@app.route("/teste")
def index():
  return 'Hello World'
  
