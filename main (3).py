#python complex password generator 
import random
upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_letters = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
symbols = "!%*&?@#"
def randomletter():
    randomletter = random.choice(lower_letters)
    return randomletter
randomupperletter = random.choice(upper_letters)
randomnumber = random.choice(numbers)
randomsymbol = random.choice(symbols)
password = randomupperletter+str(randomletter())+str(randomletter())+str(randomletter())+str(randomletter())+str(randomnumber)+randomsymbol
print("Here is a Complex Password for you: " , password)

