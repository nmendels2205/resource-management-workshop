import random
from locust import HttpUser, task, between

# Define a custom Locust User
class PrimeFactorizationUser(HttpUser):
    # Simulate a wait time between tasks (in this case, 1 second)
    wait_time = between(0.1, 1)  # Random wait time between 1 and 2 seconds
    
    # Define a task that will hit the Flask API endpoint
    @task
    def get_prime_factors(self):

        number = random.randint(2, 1111111111)
        
        # Make the request to the Flask API
        with self.client.post("/api/prime_factors", json={"number": number}, catch_response=True) as response:
            if response.elapsed.total_seconds() * 1000 > 1000:
                response.failure(f"Request took too long: {response.elapsed.total_seconds() * 1000:.2f} ms")
            else:
                response.success()
    
    # Define the number of users to simulate
    @task
    def index(self):
        self.client.get("/")  # Open the home page of the app
