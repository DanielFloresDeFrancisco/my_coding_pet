class Pet:
    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.level = 0

    def get_name(self):
        return self.name
    
    def get_experience(self):
        return self.experience
    
    def get_level(self):
        return self.level

    def set_name(self, name):
        self.name = name

    def set_experience(self, experience):
        self.experience = experience

    def set_level(self, level):
        self.level = level

