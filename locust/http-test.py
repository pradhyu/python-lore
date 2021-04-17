from locust import HttpUser, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpUser
from locust.user.task import tag


class WebsiteUser(FastHttpUser):
    """
    User class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """

    host = "http://127.0.0.1:8089"
    wait_time = between(2, 5)
    # some things you can configure on FastHttpUser
    # connection_timeout = 60.0
    # insecure = True
    # max_redirects = 5
    # max_retries = 1
    # network_timeout = 60.0

    @task
    def index(self):
        self.client.get("/")

    @task
    def readme(self):
        self.client.get("/locust/README.md")
    @task
    def stats(self):
        self.client.get("/README.md")

    @task
    @tag("mymy")
    def post1(self):
        self.client.post("/", json="{}")

    @task
    @tag("yours")
    def post1(self):
        self.client.post("/", json='{"one"":1}')

