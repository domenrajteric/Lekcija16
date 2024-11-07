from flask import Flask, render_template

# create new Flask object
app = Flask(__name__)

# controller - HANDLER
# ROOT
@app.route("/")
def index():
    return render_template("index.html")

# controller - HANDLER
@app.route("/galerie")
def galerie():
    return render_template("galerie.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(use_reloader=True)



