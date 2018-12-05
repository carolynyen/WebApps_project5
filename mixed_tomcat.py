import sys, random
from locust import HttpLocust, TaskSet

def readPost(locust):
    postid = random.randint(1, 500)
    url_string = '/editor/post?action=open&username=cs144&postid=';
    locust.client.get(url_string + str(postid), name='/editor/post?action=open')

def writePost(locust):
    postid = random.randint(1, 500)
    url_pre = '/editor/post?action=save&username=cs144&postid=';
    url_post = '&title=Loading%20Test&body=***Hello%20World!***';
    locust.client.post(url_pre + str(postid) + url_post, name='/editor/post?action=save')

class MyTaskSet(TaskSet):
    """ the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
    tasks = {readPost: 9, writePost: 1}

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
