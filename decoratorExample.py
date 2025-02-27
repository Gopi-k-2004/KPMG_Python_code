
class FoodItems:
    all_food_item_names=[]

    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
        self.__class__.all_food_item_names.append(name)

    @classmethod
    def get_all_food_item_names(cls):
        return cls.all_food_item_names

    @staticmethod
    def add(x,y):
        return x+y

pasta=FoodItems('pasta',300)
pizza=FoodItems('pizza',1)
bread=FoodItems('bread',2)

print(FoodItems.get_all_food_item_names())
print(FoodItems.add(3,4))

