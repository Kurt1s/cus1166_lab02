from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student>")
def welcome(student):
    return render_template("welcome.html", student = student)
    
@app.route("/roster/<string:grade_view>")
def roster(grade_view):
    class_roster = [("Joe","A", "Junior"),("Jon","B","Junior"),("Moe","C","Senior"),("Max","D","Junior"),("Ron","B","Freshman"),("Lin","C","Sophomore"),("Jil","B","Senior")]    
    
    return render_template("roster.html", class_roster = class_roster, grade_view = grade_view)

if __name__ == '__main__':
    app.run(debug=True)