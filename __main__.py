from sll import SLList
from dll import DLList, Position
import random
random.seed(42)
my_list = DLList()

for i in range(1000):
    a = random.randint(0,1)
    b = random.randint(0,1)
    if a == 0:
        if b == 0:
            my_list.push_back(i)
        else:
            my_list.push_front(i)
    else:
        if not my_list.is_empty():
            if b == 0:
                my_list.pop_back()
            else:
                my_list.pop_front()


print(my_list)
my_list.push_back(12)
my_list.replace(my_list.front_pos(),"a")
print(my_list)
my_list.pop_front()
print(my_list)
my_list.pop_back()
print(my_list)
