class Character:
    def __init__(self, name, health, damage):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(health, int):
            raise TypeError("Health must be an integer")
        if not isinstance(damage, int):
            raise TypeError("Damage must be an integer")

        self.name = name
        self.health = health
        self.damage = damage

    @classmethod
    def attack(cls,attacker,target):
        if attacker.damage < target.health:
            target.health = target.health - attacker.damage
            print(f'''player {attacker.name} attacks played {target.name}
he deals {attacker.damage} damage
player {target.name} is left with {attacker.damage - target.health} health
                            ''')
        elif attacker.damage > target.health:
            target.health = 0
            print(f'player {attacker.name} kills player {target.name}!')

a = Character('alex',10,10)
b = Character('beta',9,10)
Character.attack(a,b)
c = Character('gamma',15,15)
Character.attack(a,c)