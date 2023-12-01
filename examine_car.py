from models import Car

import json


print("Examining Car...")
junk_car_object = Car("Nonya", "Sedan", 2019)
junk_car_json_string = json.dumps(junk_car_object.__dict__)
print("junk_car_object:", type(junk_car_object), junk_car_object)
print("junk_car_json_string:", type(junk_car_json_string), junk_car_json_string)
