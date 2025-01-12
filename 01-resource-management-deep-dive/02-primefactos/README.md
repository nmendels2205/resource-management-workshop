# Prime Factorization

Welcome to the Prime Factorization lab! In this exercise, your task is to ensure that the service performs reliably under load. Currently, the service cannot handle requests effectively when high demand is applied.

Your mission is to adjust the application configuration to ensure it can handle **700 users** with **50 Ramp Up** in Locust testing without any failures (requests above 1 second), while maintaining a response time of around **500ms** for calculating the prime factors of `111111111111111`, even under load.

## Objective

Deploy the Prime Factorization Service on OpenShift and configure it to meet the following requirements:
- Handle **700 concurrent** users with **50 Ramp Up** without any request failures.
- Maintain a response time of approximately 500ms for the given calculation `111111111111111` under load.

## Prerequisites

1. Log in to the OpenShift cluster web console with the provided credentials.
2. Download and configure the OpenShift CLI (`oc`):
   - Log in to the OpenShift web console.
   - In the top-right corner, click on your username and select **Copy Login Command**.
   - In the top-right corner, under the question mark icon, find the **Command Line Tools** section and download the appropriate CLI for your operating system.
   - Add the downloaded CLI to your system's PATH.
   - Use the login command provided to authenticate with your cluster.
3. Familiarity with deploying and configuring applications on OpenShift.

## Steps

### 1. Explore the Files
Take a moment to explore the files in this repository. The service is containerized and includes configurations for deployment and testing.

Key files:
- `namespace.yaml`: Defines the namespace in which the service will run.
- `install.yaml`: Contains the service deployment and configuration.
- `locustfile.py`: A load testing script for generating traffic to the service.
- `99-locust`: The folder in the repository root to deploy the Locust service on OpenShift.

### 2. Deploy the Service
1. Apply the namespace and service deployment configuration:

    ```bash
    oc apply -f namespace.yaml
    oc apply -f install.yaml
    ```

2. Verify that the resources have been created:

    ```bash
    oc get pods
    oc get svc
    ```

3. Get the service's route to access it:

    ```bash
    oc get route
    ```

### 3. Generate Load
**Option 1: Generate Load Locally**  
Use the provided `locustfile.py` to simulate 700 users with Ramp up of 50 users accessing the service:

1. Install Locust on your local machine if not already installed:

    ```bash
    pip install locust
    ```

2. Run Locust with the provided script:

    ```bash
    locust
    ```

3. Open the Locust web interface (by default, at `http://localhost:8089`) and set the number of users to **700**, ramp up to **50**, and set the service's route as the host. Start the test.

**Option 2: Deploy Locust Service on OpenShift**  
Alternatively, deploy the Locust service directly on OpenShift by applying the configuration in the `99-locust` file located in the root of this repository.

1. Apply the Locust deployment configuration:

    ```bash
    oc apply -f 99-locust/namespace.yaml
    oc apply -f 99-locust/install.yaml
    ```

2. Open the Locust web interface by getting the route for the Locust service:

    ```bash
    oc get route locust
    ```

3. Set the number of users to **700**, ramp up to **50**, and set the route of the Prime Factorization Service as the host.
4. Make sure to **only select the `PrimeFactorizationUser`** class in the Locust UI for load testing.

### 4. Monitor and Adjust
1. Observe the service's behavior during the test. If there are request failures or high response times, investigate the issue.
2. Adjust the deployment configuration to ensure the service can handle the load. Update the deployment with:

    ```bash
    oc edit deployment <deployment-name>
    ```

3. Apply the updated configuration and monitor the results.

### 5. Verify Success
- Confirm that the service can handle 700 concurrent users in Locust without failures.
- Verify that the response time for calculating the prime factors of `111111111111111` is approximately 500ms, even under load.

### 6. Clean Up
Once you've completed the drill, stop the locust test
