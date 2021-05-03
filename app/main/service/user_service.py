import uuid
from ..model.user_model import GroupedUsers, UserModel

def groupByGender(users):
    userDict = {}
    userGroups = []
    for user in users:
        if user.gender not in userDict:
            userDict[user.gender] = []
        user.random_value = uuid.uuid4().hex[:13]
        updatedUser = UserModel(user.first_name, user.first_name, user.gender, 
            user.ip_address, user.email, user.id,user.random_value)
        userDict[user.gender].append(updatedUser)
    for key in userDict:
        userGroups.append(GroupedUsers(key,userDict[key]))
    
    return userGroups