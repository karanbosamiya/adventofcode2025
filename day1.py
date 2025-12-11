class A():
    def __init__(self, current):
        self.current = current
        self.password = 0
    def rotate(self, direction, clicks):
        if direction == "L":
            for i in range(clicks):
                self.current -= 1
                print("i>>>>>>>>>>", i)
                print("SELF.DIRECTION>>>>", direction)
                print("SELF.CURRENT>>>>>", self.current)
                if self.current == -1:
                    self.current = 99
                if self.current == 0:
                    print("SELF.PASSWORD>>>>>>>>>>>", self.password)
                    self.password += 1
        elif direction == "R":
            for j in range(clicks):
                print("J...........", j)
                self.current += 1
                print("SELF.DIRECTION>>>>>>", direction)
                print("SELF.CURRENT>>>>", self.current)
                if self.current == 100:
                    self.current = 0
                    print("SELF.PASSWORD>>>>>>>>>>>>>>>>>>>>", self.password)
                if self.current == 0:
                    self.password += 1
    def get_password(self):
        return self.password
