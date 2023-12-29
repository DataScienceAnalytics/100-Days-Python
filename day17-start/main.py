# in python programming
# PascalCase use a lot in Class names and snake_case use in everything else

class User:
    def __init__(self, user_id, username): # Constructor, use init function. Every time we construct the object with a class, the init will be triggered
        self.id = user_id
        self.username = username
        self.followers = 0 # setting an default value
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001","angela") # whenever construct an object from a class. We have to specify the attribute within __init__ function
user_2 = User("002","jack")
# # Add attribute (variable associated with an object) to an object
# user_1.id = "001"
# user_1.username = "angela"

user_1.follow(user_2)
print(user_1.username)
print(user_1.id)
print(user_1.followers)
print(user_2.username)
print(user_2.id)
print(user_2.followers)
