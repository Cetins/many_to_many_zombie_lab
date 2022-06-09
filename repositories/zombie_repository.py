from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.zombie_type import ZombieType

import repositories.zombie_type_repository as zombie_type_repository
import repositories.human_repository as human_repository

def save(zombie):
    sql = "INSERT INTO zombies (name, zombie_type_id) VALUES (%s, %s) RETURNING id"
    values = [zombie.name, zombie.zombie_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    zombie.id = id


def select_all():
    zombies = []
    sql = "SELECT * FROM zombies"
    results = run_sql(sql)
    for result in results:
        zombie_type = zombie_type_repository.select(result["zombie_type_id"])
        zombie = Zombie(result["name"], zombie_type, result["id"])
        zombies.append(zombie)
    return zombies


def select(id):
    sql = "SELECT * FROM zombies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    zombie_type = zombie_type_repository.select(result["zombie_type_id"])
    zombie = Zombie(result["name"], zombie_type, result["id"])
    return zombie
    



def delete_all():
    sql = "DELETE FROM zombies"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM zombies WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(zombie):
    sql = "UPDATE zombies SET (name, zombie_type_id) = (%s, %s) WHERE id = %s"
    values = [zombie.name, zombie.zombie_type.id, zombie.id]
    run_sql(sql, values)


def people_bitten_by(zombie):
    bitten_humans = []
    
    sql = """SELECT * FROM humans 
    INNER JOIN bitings 
    ON bitings.human_id = humans.id WHERE bitings.zombie_id = %s"""
    values = [zombie.id]
    results = run_sql(sql, values)
    for result in results:

        victim = Human(result['name'], result['id'])  
        bitten_humans.append(victim) 

    return bitten_humans




