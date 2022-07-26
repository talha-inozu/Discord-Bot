from orm import Model
from orm import Database




class Person(Model):
    
    discord_id = int
    
    
    def __init__(self,discord_id) :
        self.discord_id = discord_id
        
        
def get_user_or_false(discord_id):
    objects = Person.manager(db)     
    users = list(objects.all())
    for user in users:
        if user.discord_id == discord_id:
            return user
        
    return False



db = Database('Person.sqlite')
Person.db = db