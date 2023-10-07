import re
number = "+380545454546 hello 578399 world artemdenkolesnik@gmail.com Artem Denisowich Kolesnik"

result = re.findall(r'[0-9]{6}', number)
print(result)

result = re.findall(r'\+?[0-9]{12}', number)
print(result)

result = re.findall(r'\w+@\w+\.com', number)
print(result)

result = re.findall(r'\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}', number)
print(result)