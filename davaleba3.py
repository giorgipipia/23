#N1
class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature
    def get_temp(self):
        return self.__temperature
    def set_temp(self):
        self.__temperature = "new_temperature"
    def del_temp(self):
        self.__temperature
    temperature_property = property(get_temp, set_temp, del_temp)
name1 = Celsius(4)
name2 = Celsius(23)
print(name1.temperature_property)
print(name2.temperature_property)

#N2
class Bank_account:
    def __init__(self, account_name, balance = 0):
        self.__account_name = account_name
        self.__balance = balance
    def get_accountname(self):
        return self.__account_name
    def set_accountname(selfself, accountname):
        self.__account_name = accountname
    def __str__(self):
        return f"გამარჯობა:{self.__account_name}, თქვენ ანგარიშზე გაქვთ:{self.__balance}ლარი"
    def deposit(self,amount):
        self.__balance += amount
        print(f"ანხის შეტანა შესრულდა თქვენ ანგარიშზე გაქვთ:{self.__balance}ლარი")
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"თანხის განოტანა შესრულებულია ამჟად თქვენ ანგარიშზე გაქვთ:{self.__balance}ლარი")
name = Bank_account("გიორგი ფიფია")
name.deposite(input())
print(name.deposite)
name.withdraw(input())
print(name.withdra)
print(name)