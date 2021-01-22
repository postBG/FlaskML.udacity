from locust import HttpUser, task, between
import json

nb_user = 10


class flask_sklearn(HttpUser):

    host = "https://flask-ml-udacity.azurewebsites.net:443"

    wait_time = between(0.5, 10)

    @task(nb_user)
    def predict(self):
        json_request = {
            "CHAS": {
                "0": 0
            },
            "RM": {
                "0": 6.575
            },
            "TAX": {
                "0": 296.0
            },
            "PTRATIO": {
                "0": 15.3
            },
            "B": {
                "0": 396.9
            },
            "LSTAT": {
                "0": 4.98
            }
        }

        myheaders = {'Content-Type': 'application/json'}

        response = self.client.post(
            "/predict", json=json_request, headers=myheaders)

        assert response.status_code == 200