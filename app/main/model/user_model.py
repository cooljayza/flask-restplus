import json
class UserModel(dict):
    def __init__(self,fn,ln,g,ip,email,id,rand=''):
        self.first_name = fn
        self.last_name = ln
        self.gender = g
        self.ip_address = ip
        self.email = email
        self.id = id
        self.random_value = rand
        dict.__init__(self,first_name=self.first_name,last_name=self.last_name,email=self.email,
            id=self.id,ip_address=self.ip_address,gender=self.gender,random_value=self.random_value)
    def __repr__(self):
        return str(self.__dict__) 

class GroupedUsers(dict):
    def __init__(self,type,users):
        self.type = type
        self.people = users
        dict.__init__(self,type=type,people=users)

    def __repr__(self):
        return str(self.__dict__)
    
def convertToUserModel(userDict):
    rand = '' 
    if 'random_value' in userDict:
        rand = userDict['random_value']
        
    user = UserModel(userDict['first_name'],
        userDict['last_name'],userDict['gender'],userDict['ip_address'],
        userDict['email'],userDict['id'],rand)

    return user

def convertUsersDictToArray(usersDict):
    users = []
    for userDict in usersDict:
        users.append(convertToUserModel(userDict))

    return users