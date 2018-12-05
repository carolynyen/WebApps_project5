import sys, random
from locust import HttpLocust, TaskSet

def writePost(locust):
    postid = random.randint(1, 500)
    url_pre = '/api/cs144/';
    locust.client.put(url_pre + str(postid), {"title": "Loading Test", "body": "***Hello World!***"}, name='/api/cs144')

def readPost(locust):
    postid = random.randint(1, 500)
    url_string = '/blog/cs144/';
    locust.client.get(url_string + str(postid), name='/blog/cs144' )

class MyTaskSet(TaskSet):
    """ the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
    tasks = {writePost: 1, readPost: 9}
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """
        response = locust.client.post("/login", data={"username":"cs144", "password": "password"})
        if response.status_code != 200:
            print("FAIL to start with posting data to server. Make sure that your server is running.")
            sys.exit();

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
