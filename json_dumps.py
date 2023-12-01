import json


class PythonToJson:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, "r") as file:
            data = file.read()
            return data

    def convert_to_json(self):
        data = self.read_file()
        json_data = json.loads(data)
        return json_data

    def write_to_json(self, json_data):
        with open("json_file.json", "w") as file:
            json.dump(json_data, file, indent=4)
