class Car:

    def __init__(self, name, model, construction_year):
        """Constructor"""
        self.name = name
        self.model = model
        self.construction_year = construction_year
         
    def Dict(self):
        """Return object as a Dictionary"""
        dict = { 'Name' : self.name, 'Model' : self.model, 'Contruction Year' : self.construction_year }
        return dict

    def built_in_dict(self):
        """Built-in method __dict__ for creation an dictionary with attributes(keys) and values"""
        return self.__dict__

    def nestedDict(self, other):
        """Return nested dictionary"""
        nested_dict = { 1: self.Dict(), 2 : other.Dict() } 
        return nested_dict
        


mercedez =  Car('Mercedes','EQS', 2007)
VW =  Car('VW','Passat', 2020)

print(mercedez.Dict())  #creation a dictionary of the object
print(mercedez.built_in_dict()) #built-in dictionary method

car_mercedez = mercedez.nestedDict(VW)  #creation a nested dictionary with 2 objects
print('Values from Dictionary Mercedez:')
print(car_mercedez[1].values()) #dictionary method values() 
print('Keys from Dictionary Mercedez:')
print(car_mercedez[1].keys())   #dictionary method keys()
print('Items from Dictionary VW:')
print(car_mercedez[2].items())  #dictionary method items()
