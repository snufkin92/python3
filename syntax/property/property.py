class Human():

    def __init__(self, name='Mike', age=18, sex='M'):
        self.name = name
        self._age = age
        self.__sex = sex

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def __str__(self):
        """
        特殊メソッド
        :return:
        """
        return self.name + "'s sex is " + self.__sex


mike = Human()

# nameプロパティーへのアクセス確認
print(mike.name)
mike.name = "Tom"
print(mike.name)

# ageプロパティーへのアクセス確認
print(mike.age)
print(mike._age)
mike.age = 19
print("### new age = ", mike.age)

# sexプロパティーへのアクセス確認
# print(mike.sex)

# __str__の確認
print(mike)
