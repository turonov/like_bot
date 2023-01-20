import json
#Create Like counting class
class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    """def add_user(self,user_id):
        self.db[user_id]={"like":0,"dizlike":1}
        self.save()"""
    def all_likes(self):
        """Counts all users likes
        returns
            all users likes
        """
        pass
        """for all_likes (like):
            like+=1"""
            
            

        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        pass
        
        
    #Add a like to the database
    def add_like(self, user_id:str)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
        returns:
            The number of likes and dislikes for the post
        '''
        self.db[user_id]={"like":1}
        
        self.save("user_id")

  
    #Add a dislike to the database
    def add_dislike(self, user_id:str)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        pass
        self.db[user_id]={"dizlike":1}
        self.save()

db = LikeDB("db.json")
print(db.add_like("user_id"))   