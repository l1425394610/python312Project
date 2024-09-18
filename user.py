class User:
    def __new__(cls, name, age, sex):
        print("new")
        return super(User, cls).__new__(cls)

    def __init__(self, name, age, sex):
        print("init")
        self._name = name
        self._age = age
        self.__sex = sex

    def __str__(self):
        return self._name + "---" + str(self._age)

    def get_name(self):
        return self._name

    def set_name__(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age__(self, age):
        self._age = age
