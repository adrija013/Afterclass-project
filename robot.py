class Robot:

    def __init__(self, name):
        self.name = name

Tom = Robot("Tom")        
Jerry = Robot("Jerry")     

print("Hi I am {}".format(Tom.name))
print("My name is {}".format(Jerry.name))
