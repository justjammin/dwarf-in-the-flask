from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")
  
@app.route("/John")
def John():
  return "Hello John."

@app.route("/<name>") # at the endpoint /<name>
def only_name(name): # call method Welcome_name
  return "I see you " + name + "!" # which returns "I see you + name + !

@app.route("/Welcome/<name>") # at the endpoint /<name>
def Welcome_name(name): # call method Welcome_name
  return "Yo what's up " + name + "!" # which returns "Welcome + name + !

if __name__ == "__main__":
  app.run(debug=True)