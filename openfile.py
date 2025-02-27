
with open('example.txt','w') as file:
    file.write('Hello python - using context manager example')

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Existing the context")
        if exc_type:
            print(f'An execution has exectued : {exc_val}')
            return True


with MyContextManager() as cm:
    print("inside the context")

print("outside the context")