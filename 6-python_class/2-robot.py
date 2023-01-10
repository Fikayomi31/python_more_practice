class Robot:
    pass
if __name__ == "__main__":
    x = Robot()
    y = Robot()
    # y is bind into y2
    y2 = y
    print(y == y2)
    print(y == x)
