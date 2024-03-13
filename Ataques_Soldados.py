from abc import ABC, abstractmethod

# Definir interfaces para comportamientos de ataque y movimiento
class IAttackBehavior(ABC):
    @abstractmethod
    def calculate_damage(self):
        pass
    
    @abstractmethod
    def attack_range(self):
        pass

class IMovementBehavior(ABC):
    @abstractmethod
    def determine_speed(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# Implementaciones concretas para comportamientos de ataque
class HeavySwordAttack(IAttackBehavior):
    def calculate_damage(self):
        print("Ataque con espada pesada: 7 puntos de daño causados.")
    
    def attack_range(self):
        print("Rango de ataque: corto. El guerrero se acerca para infligir daño.\n")

class SpearAttack(IAttackBehavior):
    def calculate_damage(self):
        print("Ataque con lanza: 3 puntos de daño causados.")
    
    def attack_range(self):
        print("Rango de ataque: medio. El soldado puede atacar a distancia media.\n")

class ArcherAttack(IAttackBehavior):
    def calculate_damage(self):
        print("Ataque con flechas: 2 puntos de daño causados.")
    
    def attack_range(self):
        print("Rango de ataque: largo. El arquero ataca desde largas distancias.\n")

# Implementaciones concretas para comportamientos de movimiento
class HeavyArmorMovement(IMovementBehavior):
    def determine_speed(self):
        print("Movimiento con armadura pesada: Velocidad de 5. No es muy rápido.")
    
    def move(self):
        print("Movimiento con armadura pesada: Solo puede avanzar, no retrocede ni se aparta de su posición.")

class AgileMovement(IMovementBehavior):
    def determine_speed(self):
        print("Movimiento ágil: Velocidad de 7. Puede moverse rápidamente.")
    
    def move(self):
        print("Movimiento ágil: Puede desplazarse en cualquier dirección, mostrando versatilidad en su movimiento.")

class ArcherMovement(IMovementBehavior):
    def determine_speed(self):
        print("Movimiento ágil (arquero): Velocidad de 6. Se mueve con agilidad para mantener distancia.")
    
    def move(self):
        print("Movimiento ágil (arquero): Puede retroceder y desplazarse lateralmente, aprovechando su destreza para evadir ataques.")

# Clase base para unidades militares
class MilitaryUnit:
    def __init__(self, attack_behavior: IAttackBehavior, movement_behavior: IMovementBehavior):
        self.attack_behavior = attack_behavior
        self.movement_behavior = movement_behavior
    
    def perform_attack(self):
        self.attack_behavior.calculate_damage()
        self.attack_behavior.attack_range()

    def perform_movement(self):
        self.movement_behavior.move()
        self.movement_behavior.determine_speed()

# Clases específicas para cada tipo de unidad militar
class HeavySwordWarrior(MilitaryUnit):
    def __init__(self):
        super().__init__(HeavySwordAttack(), HeavyArmorMovement())

class SpearSoldier(MilitaryUnit):
    def __init__(self):
        super().__init__(SpearAttack(), AgileMovement())

class ArcherUnit(MilitaryUnit):
    def __init__(self):
        super().__init__(ArcherAttack(), ArcherMovement())

if __name__ == "__main__":
    warrior = HeavySwordWarrior()
    soldier = SpearSoldier()
    archer = ArcherUnit()

    warrior.perform_attack()
    warrior.perform_movement()
    print("")
    soldier.perform_attack()
    soldier.perform_movement()
    print("")
    archer.perform_attack()
    archer.perform_movement()