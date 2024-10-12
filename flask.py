from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        if not name or not email or not age:
            return "Please complete all fields", 400

        
        return render_template("result.html", name=name, email=email, age=age)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

