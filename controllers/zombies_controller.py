from flask import Blueprint, Flask, redirect, render_template, request

from models.zombie import Zombie
import repositories.zombie_repository as zombie_repository
import repositories.zombie_type_repository as zombie_type_repository

zombies_blueprint = Blueprint("zombies", __name__)

# INDEX
@zombies_blueprint.route("/zombies")
def zombies():
    zombies = zombie_repository.select_all()
    return render_template("zombies/index.html", zombies=zombies)


# NEW
@zombies_blueprint.route("/zombies/new")
def new_zombie():
    zombie_types = zombie_type_repository.select_all()
    return render_template("zombies/new.html", zombie_types=zombie_types)


# CREATE
@zombies_blueprint.route("/zombies", methods=["POST"])
def create_zombie():
    name = request.form["name"]
    zombie_type_id = request.form["zombie_type_id"]
    zombie_type = zombie_type_repository.select(zombie_type_id)
    new_zombie = Zombie(name, zombie_type)
    zombie_repository.save(new_zombie)
    return redirect("/zombies")


# EDIT
@zombies_blueprint.route("/zombies/<id>/edit")
def edit_zombie(id):
    zombie = zombie_repository.select(id)
    zombie_types = zombie_type_repository.select_all()
    return render_template('zombies/edit.html', zombie=zombie, zombie_types=zombie_types)


# UPDATE
@zombies_blueprint.route("/zombies/<id>", methods=["POST"])
def update_zombie(id):
    name = request.form["name"]
    zombie_type_id = request.form["zombie_type_id"]
    zombie_type = zombie_type_repository.select(zombie_type_id)
    zombie = Zombie(name, zombie_type, id)
    zombie_repository.update(zombie)
    return redirect("/zombies")


# DELETE
@zombies_blueprint.route("/zombies/<id>/delete", methods=["POST"])
def delete_zombie(id):
    zombie_repository.delete(id)
    return redirect("/zombies")

#SHOW
@zombies_blueprint.route("/zombies/<id>/")
def show_zombie(id):
    zombie = zombie_repository.select(id)
    victims = zombie_repository.people_bitten_by(zombie)
    return render_template("zombies/show.html", zombie = zombie, victims=victims)
    
