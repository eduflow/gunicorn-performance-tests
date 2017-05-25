import os
import sys

import locust
from locust import HttpLocust, TaskSet, task


class HitWebsite(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    @task(1)
    def fetch_index(self):
        res = self.client.get(url='/')
        return res


class UserHittingWebsite(HttpLocust):
    task_set = HitWebsite

    # Minimum and maximum waiting time for a response (in ms)
    # http://docs.locust.io/en/latest/writing-a-locustfile.html#the-min-wait-and-max-wait-attributes
    min_wait = 0
    max_wait = 0
