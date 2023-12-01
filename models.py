class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def __str__(self):
        return f"{self.name} : {self.model} - {self.year}"
