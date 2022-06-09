import pdb

from models.biting import Biting
import repositories.biting_repository as biting_repository

from models.human import Human
import repositories.human_repository as human_repository

from models.zombie import Zombie
import repositories.zombie_repository as zombie_repository

from models.zombie_type import ZombieType
import repositories.zombie_type_repository as zombie_type_repository

# biting_repository.delete_all()
human_repository.delete_all()
zombie_repository.delete_all()
zombie_type_repository.delete_all()

human_1 = Human("Rochelle")
human_repository.save(human_1)

human_2 = Human("Coach")
human_repository.save(human_2)

human_3 = Human("Nick")
human_repository.save(human_3)

human_4 = Human("Ellis")
human_repository.save(human_4)

zombie_type_1 = ZombieType("Walker")
zombie_type_repository.save(zombie_type_1)

zombie_type_2 = ZombieType("Crawler")
zombie_type_repository.save(zombie_type_2)

zombie_type_3 = ZombieType("Runner")
zombie_type_repository.save(zombie_type_3)

zombie_1 = Zombie("Ed", zombie_type_2)
zombie_repository.save(zombie_1)

zombie_2 = Zombie("Pete", zombie_type_1)
zombie_repository.save(zombie_2)

biting_1 = Biting(human_2, zombie_2)
biting_repository.save(biting_1)

biting_2 = Biting(human_3, zombie_1)
biting_repository.save(biting_2)

biting_3 = Biting(human_3, zombie_2)
biting_repository.save(biting_3)

biting_4 = Biting(human_4, zombie_2)
biting_repository.save(biting_4)

pdb.set_trace()
