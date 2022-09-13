from pythonProject1.Helper.RequestsUtility import RequestsUtility


class UserEndPoint(object):


    def __init__(self):

       self.url = "https://petstore.swagger.io/v2/user"

       self.requests=RequestsUtility()

    def create_new_user(self,user_id,user_name,first_name,last_name,):
        data = dict()
        data['id'] = user_id
        data['username']=user_name
        data['firstName'] = first_name
        data['lastName']=last_name
        response = self.requests.post(self.url, payload=data)
        return response
    def get_user_by_username(self,user_name):
        url = self.url + "/{}".format(user_name)
        response=self.requests.get(url,payload=None)
        return response
    def delete_user(self,user_name):
        url = self.url + "/{}".format(user_name)
        response = self.requests.delete(url, payload=None)
        return response




