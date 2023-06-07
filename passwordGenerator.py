import random
k = []
enter_name = input("Please enter yur full name ")
symbol = ['!','@','#','$','&']
numl = [x for x in range(1,9)]
random.shuffle(numl)
random.shuffle(symbol)
n = random.sample(enter_name, 8)
for i in n:
    if i != ' ':
        k.append(i)
password = ''
for i in k:
    password = password+i
password += symbol[0] + str(numl[1])
password.capitalize()
print(password)