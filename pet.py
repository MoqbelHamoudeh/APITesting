from pythonProject1.Helper.RequestsUtility import RequestsUtility


class PetEndPoint(object):


    def __init__(self):

       self.url = "https://petstore.swagger.io/v2/pet"

       self.requests=RequestsUtility()


    def creat_pet(self, pet_name, pet_id, pet_category):
        payload=dict()
        payload['name']=pet_name
        payload['id']=pet_id
        payload['category']=pet_category
        response=self.requests.post(self.url,payload=payload)
        return response
    def get_pet_by_id(self,pet_id):
        url=self.url+"/{}".format(pet_id)
        response=self.requests.get(url,params=None)
        return response

    def delete_pet_by_id(self,pet_id):
        url = self.url + "/{}".format(pet_id)
        payload=dict()
        payload['id']=pet_id
        response=self.requests.delete(url,payload=payload)



    def update_pet_name_by_id(self,pet_id,new_name):

        payload=dict()
        payload['id']=pet_id
        payload['name']=new_name
        response=self.requests.put(self.url,payload=payload)
        return response

    def update_category_by_id(self,pet_id,new_category,):
        payload=dict()
        payload['id']=pet_id
        payload['category']=new_category
        response=self.requests.put(self.url,payload=payload)
        return response




