from flask import Flask, render_template
from users import users
app = Flask(__name__)


class Worker:
    def __init__(self, name, age, developmentExperience, image, education):
        self.name = name
        self.age = age
        self.developmentExperience = developmentExperience
        self.image = image
        self.education = education


"""
    All IDs are in users.py
    If can't find user with such an ID, renders cantFindUser.html
"""

@app.route("/users/<string:id>")
def show_user_info(id):
    try:
        user = Worker(users[id]["name"],
                      users[id]["age"],
                      users[id]["developmentExperience"],
                      users[id]["image"],
                      users[id]["education"])
        return render_template("index.html", user=user)
    
    except:
        return render_template("cantFindUser.html")

if __name__ == "__main__":
    app.run()