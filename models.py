class Car:
    """
    Class to represent a car.

    Attributes:
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was made.
    """

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def __str__(self):
        return f"{self.brand} : {self.model} - {self.year}"
