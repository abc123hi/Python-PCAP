class Animal:
    def __init__(self) -> None:
        print('Animal Object Created')
        self.my_animal = ""
    def set_animal(self,myAnim):
        self.set_animal = myAnim
    def get_animal(self):
        return self.my_animal