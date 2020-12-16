import json
import requests

target              = input("Input your URL target: ")
spam_count          = input("Spam count: ")
parameter           = {}
hacked_parameter    = {}
loop_parameter      = 'yes'

while loop_parameter == 'yes':

    print("")
    print("Wanna insert a new parameter? [yes/no]")

    loop_parameter = input("Your answer: ")
    if loop_parameter == 'yes':
        new_key = input("New key: ")
        new_value = input("New value: ")
        parameter[new_key] = new_value
    else:
        break

print("")

for i in range(int(spam_count)):

    for atribut, nilai in parameter.items():
        hacked_parameter[atribut] = nilai + str(i+1)

    response = requests.post(target, data=hacked_parameter)
    print(response.status_code, response.reason)
    print( json.dumps(hacked_parameter, indent=4, default=str) )

    print("")
