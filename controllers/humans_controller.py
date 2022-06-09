from flask import Blueprint, Flask, redirect, render_template, request

from models.human import Human
import repositories.human_repository as human_repository

humans_blueprint = Blueprint("humans", __name__)

# INDEX
@humans_blueprint.route("/humans")
def humans():
    humans = human_repository.select_all()
    return render_template("humans/index.html", humans=humans)


# NEW
@humans_blueprint.route("/humans/new")
def new_human():
    return render_template("humans/new.html")


# CREATE
@humans_blueprint.route("/humans", methods=["POST"])
def create_human():
    name = request.form["name"]
    new_human = Human(name)
    human_repository.save(new_human)
    return redirect("/humans")


# EDIT
@humans_blueprint.route("/humans/<id>/edit")
def edit_human(id):
    human = human_repository.select(id)
    return render_template('humans/edit.html', human=human)


# UPDATE
@humans_blueprint.route("/humans/<id>", methods=["POST"])
def update_human(id):
    name = request.form["name"]
    human = Human(name, id)
    human_repository.update(human)
    return redirect("/humans")


# DELETE
@humans_blueprint.route("/humans/<id>/delete", methods=["POST"])
def delete_human(id):
    human_repository.delete(id)
    return redirect("/humans")
