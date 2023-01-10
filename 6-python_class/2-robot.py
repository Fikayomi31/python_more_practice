class Robot:
    pass
if __name__ == "__main__":
    x = Robot()
    y = Robot()
    # y is bind into y2
    y2 = y
    #giving the robot name
    x.name = 'C4-Rt4'
    x.built_year = 1940
    y.name = "Ca-H45"
    y.built_year = 1920
    
    # checking true and false
    print(y == y2)
    print(y == x)

    #printing robot name and build year
    print("My name is {} and I was created in {}".format(x.name, x.built_year))
    print("My name is {} and I was creared in {}".format(y.name, y.built_year))
    
    """ Using the function getattr to prevent attribute that is not defined
    which will be used to create new attribute year for year of the robot"""
    year = getattr(x, 'year', 100)
    print(year)
    print("My name is {} and I was created in {} and am {} year old".format(x.name, x.built_year, year))

    # Checking for each attribute
    print(x.__dict__)
    print(y.__dict__)
    print(y2.__dict__)

    # Checking for the attribute of the class Robot
    print(Robot.__dict__)
