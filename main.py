

import requests
import json
import logging as logger

from pythonProject1.EndPoints.OrderEndPoint.order import OrderEndPoint
from pythonProject1.EndPoints.PetEndPoint.pet import PetEndPoint
from pythonProject1.EndPoints.UserEndPoint.user import UserEndPoint


def main():
    logger.basicConfig(level=logger.INFO)
    pet_api = PetEndPoint()
    category=dict()
    category['name']='cats'
    category['id']=15
    pet_api.creat_pet("bebes",4,category)
    mypet=pet_api.get_pet_by_id(4)
    assert mypet['name']=='bebes'
    assert mypet['category']['name']=='cats'
    mypet=pet_api.update_pet_name_by_id(4,"basboos")
    mypet=pet_api.delete_pet_by_id(4)
    updated_category=dict()
    updated_category['name']='dogs'
    updated_category['id']=9
    pet_api.update_category_by_id(4,updated_category)
    assert updated_category['name']=='dogs'
    assert updated_category['id']==9
    user_api = UserEndPoint()
    user_api.create_new_user(8,'jacke','jack','ja')
    user_api.create_new_user(10,'danii','dani','dan')
    user_api.get_user_by_username('danii')
    user_api.delete_user('jacke')
    order_api=OrderEndPoint()
    order_api.create_order(5,32,323,'dsa')
    order_api.get_order_details(5)
    cat_category = dict()
    cat_category['name'] = 'cat'
    cat_category['id'] = 1
    pet_api.creat_pet("Meow", 11, cat_category)
    dog_category = dict()
    dog_category['name'] = 'dog'
    dog_category['id'] = 2
    pet_api.creat_pet("doggie", 22, dog_category)
    bird_category = dict()
    bird_category['name'] = 'Bird'
    bird_category['id'] = 3
    pet_api.creat_pet("birdie", 33, bird_category)
    fish_catergory=dict()
    fish_catergory['name']="Fish"
    fish_catergory['id']=4
    pet_api.creat_pet('fishey',44,fish_catergory)
    my_bird=pet_api.get_pet_by_id(33)
    my_cat=pet_api.get_pet_by_id(11)
    assert my_cat['name']=='Meow'
    assert my_bird['name']=='birdie'
    ahmad_user=user_api.create_new_user(1,'samie','sam','sami')
    ali_user=user_api.create_new_user(2,'jackie','jack','jack')
    ahmad_user=user_api.get_user_by_username('samie')
    ali_user = user_api.get_user_by_username('jackie')
    assert ali_user['id']==2
    assert ahmad_user['id']==1
    ali_order=order_api.create_order(111,1,2,'placed')
    ahmad_order=order_api.create_order(222,2,2,'shipped')

    ali_order=order_api.get_order_details(111)
    ahmad_order = order_api.get_order_details(222)
    assert ali_order['id']==111
    assert ahmad_order['id']==222



















if __name__ == '__main__':
    main()
