import os
import unittest

from app.main.service import user_service
from app.main.model import user_model


user = user_model.UserModel()
user.first_name = "first"
user.last_name = "last",
user.gender = "female"


user1 = user_model.UserModel()
user1.gender = "male"
user1.first_name = "last"
user1.last_name = "first"

users = [user,user1]
class UserServiceTests(unittest.TestCase):
    
    def test_group_produce_two_groups(self):
        result = user_service.groupByGender(users)
        self.assertTrue(len(result) == 2)

    def test_group_contains_genders(self):
        result = user_service.groupByGender(users)
        self.assertTrue(len([g for g in result if g.type == 'female']) == 1)
        self.assertTrue(len([g for g in result if g.type == 'male']) == 1)   


if __name__ == '__main__':
   unittest.main()