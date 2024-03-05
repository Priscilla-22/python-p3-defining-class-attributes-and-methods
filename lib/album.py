class Album:
    """    def __init__(self, date):
            self.release_date = date  #instance attribute that can be accessed through the dot notation on the instance itself

    album=Album(1981)
    print(album.release_date)"""


    """ album_count = 0  # class attribute


    def __init__(self, date):
        Album.album_count += 1
        self.release_date = date

joshua_tree=Album(1982)
Album(1982)
Album(1982)
Album(1982)
print(joshua_tree.album_count)
print(Album.album_count)

    @classmethod
    def class_method_name(cls): #entire class itself
        #some code"""

    album_count = 0


    def __init__(self, date):
        self.increase_album_count()
        self.release_date = date


    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment
