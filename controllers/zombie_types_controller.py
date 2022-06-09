from flask import Blueprint, Flask, redirect, render_template, request

from models.zombie_type import ZombieType
import repositories.zombie_type_repository as zombie_type_repository

zombie_types_blueprint = Blueprint("zombie_types", __name__)

# INDEX
@zombie_types_blueprint.route("/zombietypes")
def zombie_types():
    zombie_types = zombie_type_repository.select_all()
    return render_template("zombie_types/index.html", zombie_types=zombie_types)


# NEW
@zombie_types_blueprint.route("/zombietypes/new")
def new_zombie_type():
    return render_template("zombie_types/new.html")


# CREATE
@zombie_types_blueprint.route("/zombietypes", methods=["POST"])
def create_zombie_type():
    name = request.form["name"]
    new_zombie_type = ZombieType(name)
    zombie_type_repository.save(new_zombie_type)
    return redirect("/zombietypes")


# EDIT
@zombie_types_blueprint.route("/zombietypes/<id>/edit")
def edit_zombie_type(id):
    zombie_type = zombie_type_repository.select(id)
    return render_template('zombie_types/edit.html', zombie_type=zombie_type)


# UPDATE
@zombie_types_blueprint.route("/zombietypes/<id>", methods=["POST"])
def update_zombie(id):
    name = request.form["name"]
    zombie_type = ZombieType(name, id)
    zombie_type_repository.update(zombie_type)


# DELETE
@zombie_types_blueprint.route("/zombietypes/<id>/delete", methods=["POST"])
def delete_zombie(id):
    zombie_type_repository.delete(id)
    return redirect("/zombietypes")
