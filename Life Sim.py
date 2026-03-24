class Player:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.age = 16
        self.money = 100
        self.energy = 100

    def show_stats(self):
        stats = {"First Name": self.name,
                 "Last Name": self.last_name,
                 "Age": self.age,
                 "Money": self.money,
                 "Energy": self.energy}

        for key, value in stats.items():
            print(f"{key}: {value}")

    def work(self):
        if self.energy <= 0:
            print(f"\n{self.name} is too tired to work bro..")

        else:
            print(f"{self.name} works all day!")
            print("\nMoney +100$")
            print("Energy -10..")
            self.money += 100
            self.energy -= 10

    def sleep(self):
        if self.energy >= 100:
            print(f"\n{self.name} doesn't want to sleep!")

        else:
            print(f"\n{self.name} takes a well deserved nap!")
            print("\nEnergy +40!")
            self.energy += 40