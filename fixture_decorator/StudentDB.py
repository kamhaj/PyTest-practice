import json

## class mocking a database
class StudentDB:
    def __init__(self):
        self.__data = {} #empty dict
        
        
    ##  connect to db (read file)
    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)
        
        
    ## look for student by his/her name
    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student
                
     
    def close(self):
        pass