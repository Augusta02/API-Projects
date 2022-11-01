

# #GET
# """Used to retrieve resource from a REST API"""

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response= requests.get(api_url)
# print(response.json())

# # print(response.status_code)

# # POST
# """This is used to create a new resource"""
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {
# 	"userId": 1,
# 	"title": "Buy milk",
# 	"completed": False
# }

# response= requests.post(api_url, json=todo)
# # print(response.json())
# '''The above code, I used the request.post() to create a new todo in the 
# system. First, create a dictionary of my ew todo . Then pass thsi dictionary 
# in the json keyword arguement of the request.post(). This method automatically 
# sets the request's HTTP header to COntent-Type tot application/json. it also 
# serializes todo into a JSON string, which it appends to the body of the request'''






# import  json 
# headers = {"Content-Type": "application/json"}
# response= requests.post(api_url, data=json.dumps(todo), headers= headers)
# print(response.status_code)

# '''In the above code, I added a headers dictionary taht contains a single header Content-Tyoe
# set to application/json. This tells the REST API that I am sending a JSON data with the request
# I go on to call the requests.post(), call json.dmps(todo) to serialize it. Afterits serialized, 
# pass the data keyword arguement. The dtaa arguement tealls requests what data to include in 
# the request.  I also pass the headers dictionary to requests.post() to set the HTTP headers namually

# Calling request.post() like this does the same thing as the previous code, but gives more control over
# the request'''



# '''PUT'''

# api_url = "https://jsonplaceholder.typicode.com/todos/10"

# response = requests.get(api_url)
# print(response.json())

# '''{'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque quia maiores aut', 'completed': True}'''

# """Now lets update the resource. First we create a dictionary with the new data"""

# todo= {
# 	"userID": 1,
# 	"title": "Wash car",
# 	"completed": True
# }
# response= requests.put(api_url, json=todo)
# print(response.status_code)
# print(response.json())


# '''PATCH'''
# '''This is used to partially update a resource'''
# todo= {
# 	"userID": 1,
# 	"title": "Buy groceries",
# 	"completed": False
# }

# response= requests.patch(api_url, json=todo)
# print(response.status_code)
# print(response.json())