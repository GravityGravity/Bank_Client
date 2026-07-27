# client_list.py

from client import Client
import json 

class Client_List:
    def __init__(self):
        
        self.clients: dict[int, Client] = {}
        with open("client_info.JSON", "r") as file:
            data = json.load(file)
        for client_data in data:
            client = Client(client_data["f_name"], client_data["l_name"], client_data["user_id"])
            self.clients[client.user_id] = client

    def add_client(self, client):
        self.clients[client.user_id] = client

    def get_client_by_id(self, user_id):
        return self.clients.get(user_id)