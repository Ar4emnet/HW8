import re
number = "hello 578399 world "

result = re.findall(r'[0-9]{6}', number)
print(result)

result = re.findall(r'\+?[0-9]{12}', number)
print(result)