class Warrior:
    def __init__(self, name, maximum_health):
        self.name = str(name) if name is not None else ""
        self.maximum_health = maximum_health if maximum_health is not None and type(maximum_health) is int else 0
        self._is_alive = True if maximum_health is not None and type is int and maximum_health > 0 else False

    @property
    def is_alive(self):
        self._is_alive = self.maximum_health > 0
        return self._is_alive

    def __add__(self, other):
        if self is not None and other is not None and self.is_alive and other.is_alive:
            new_name = f"{self.name} {other.name}"
            new_maximum_health = self.maximum_health + other.maximum_health
            return Warrior(name=new_name, maximum_health=new_maximum_health)
        return None

    def __sub__(self, other):
        if self is not None and other is not None and self.is_alive and other.is_alive:
            self.maximum_health -= 1
            other.maximum_health -= 1

    def __str__(self):
        return f'Warrior(name="{self.name}", maximum_health={self.maximum_health}, is_alive={self.is_alive})'


# Test the class

# create warriors and print objects
xena = Warrior(name="Xena", maximum_health=1)
conan = Warrior(name="Barbar Conan", maximum_health=2)

print("\nWarriors initialized")
print(str(xena))
print(str(conan))

# add warriors (and print it)
child = xena + conan
weirdo = xena + xena + xena
none_test = xena + xena + None

print("\nChildren tests")
print(str(child))
print(str(weirdo))
print(str(none_test))


# subtract warriors (and print them)
fight = xena - conan

print("\nFighters after a fight")
print(str(xena))
print(str(conan))

# add warrior that´s not alive (and print it)
child2 = xena + conan

print("\nAdding dead warrior")
print(str(child2))
