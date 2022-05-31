from locust import HttpUser, task


class ServingV2User(HttpUser):
    host = "https://dbc-4b4baebd-ff92.dev.databricks.com"

    @task
    def query_single_model(self):
        headers = {'Authorization': f'Bearer asd'}
        self.client.post('model-endpoint/INFERENCE_INVOCATION_MODEL/1/invocations',
                         headers=headers,
                         json={})
