
def main():
    a= {'x':1,'y':2,'z':3,'p':4}
    print(type(a))
    print_dict(a)
    a1=dict(x='1', y=2, z=3, p=5)
    print(type(a1))
    print_dict(a1)
    a.update(a1)
    print(a)
    my_dict = {'apple':1, 'banana':2, 'cherry':3}
    keys_string = ','.join(my_dict.keys())
    print(keys_string)
    my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    values_string = ','.join(str(value) for value in my_dict.values())
    print(values_string)
    my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    items_string = ','.join(f'{key}:{value}' for key,value in my_dict.items())
    print(items_string)

def print_dict(o):
    for i in o:
        print(f"{i}:{o[i]}")
    print(','.join(f'{i}: {o[i]}'))

if __name__=="__main__":main()
