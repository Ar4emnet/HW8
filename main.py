import re
number = "+380545454546 hello 578399 world artemdenkolesnik@gmail.com Artem Denisowich Kolesnik"

result = re.findall(r'[0-9]{6}', number)
print(result)

result = re.findall(r'\+?[0-9]{12}', number)
print(result)

result = re.findall(r'\w+@\w+\.com', number)
print(result)
