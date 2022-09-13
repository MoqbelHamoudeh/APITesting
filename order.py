from pythonProject1.Helper.RequestsUtility import RequestsUtility


class OrderEndPoint(object):


    def __init__(self):

       self.url = "https://petstore.swagger.io/v2/store/order"

       self.requests=RequestsUtility()

    def create_order(self,order_id,pet_Id,quantity,order_status):
        data=dict()
        data['id']=order_id
        data['petId']=pet_Id
        data['quantity']=quantity
        data['status']=order_status
        response = self.requests.post(self.url, payload=data)
        return response
    def get_order_details(self,order_id):
        url = self.url + "/{}".format(order_id)
        response=self.requests.get(url,payload=None)
        return response


