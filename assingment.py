class FourCal:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university
        self.add_num = 0
        self.min_num = 0
        self.mul_num = 0
        self.div_num = 0

    def add(self, num1, num2):
        result = num1+num2
        return result

    def sub(self, num1, num2):
        result num1-num2
        return result

    def mul(self, num1, num2):
        result num1*num2
        return result

    def div(self, num1, num2):
        if(num2 == 0):
            print('0으로 나눌 수 없습니다')
            return None
        result num1/num2
        return result

    def showcount(self):
        return self.add_num, self.sub_num, self.mul_num, self.div_num 


#main code
calculator1 = FourCal("강연우", 24, "고려대학교")
print(calculator1.name, calculator1.age)

print()
calculator1.showcount()

