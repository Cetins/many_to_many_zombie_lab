from flask import Flask, render_template

from controllers.bitings_controller import bitings_blueprint
from controllers.humans_controller import humans_blueprint
from controllers.zombies_controller import zombies_blueprint
from controllers.zombie_types_controller import zombie_types_blueprint

app = Flask(__name__)

app.register_blueprint(bitings_blueprint)
app.register_blueprint(humans_blueprint)
app.register_blueprint(zombies_blueprint)
app.register_blueprint(zombie_types_blueprint)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
