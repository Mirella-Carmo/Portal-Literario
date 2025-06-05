class Book:
    def __init__(self):
        self.id = 0
        self.title = ''
        self.year = 0
        self.img = ''
        self.about = ''
        self.author = ''
        self.genre = ''
        self.about_author = ''
        self.photo_author = ''
    
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

    def set_title(self, name):
        self.title = name
    
    def get_title(self):
        return self.title
    
    def set_year(self, year):
        self.year = year
    
    def get_year(self):
        return self.year
    
    def set_img(self, img):
        self.img = img
    
    def get_img(self):
        return self.img
    
    def set_about(self, about):
        self.about = about
    
    def get_about(self):
        return self.about
    
    def set_author(self, name):
        self.author = name
    
    def get_author(self):
        return self.author
    
    def set_genre(self, genre):
        self.genre = genre
    
    def get_genre(self):
        return self.genre
    
    def set_about_author(self, about):
        self.about_author = about
    
    def get_about_author(self):
        return self.about_author
    
    def set_photo_author(self, img):
        self.photo_author = img
    
    def get_photo_author(self):
        return self.photo_author