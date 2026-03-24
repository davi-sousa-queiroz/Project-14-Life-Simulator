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