def main():
    x = dict(a="b",c="d",e="f")
    call(**x)
    call(a="b",c="d",e="f")
def call(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print("key {} says {}".format(k,kwargs[k]))
    else:
        print("No Args Passed")


if __name__ == '__main__' : main()