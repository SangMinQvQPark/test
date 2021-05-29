# import contack2
# import python
# import os
#
# print(contack2.my_print())
# print(python.my_print())
import os

def get_something():
    f = open('d:\\asd.txt', 'rt')
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)
    for i in range(num):
        pass
    return lines, num, i

    # for i in range(num):
    #     name = lines[4*i].rstrip('\n')
    #     phone = lines[4*i+1].rstrip('\n')
    #     email = lines[4*i+2].rstrip('\n')
    #     addr = lines[4*i+3].rstrip('\n')
    #     contact = Contact2(name, phone, email, addr)
    #     contact_list.append(contact)
    # f.close()

print(get_something())