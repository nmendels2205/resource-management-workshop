# Prime Factorization V2

Welcome to the Prime Factorization V2 lab! In this exercise, the next version of Prime Factorization introduces new background services, which are currently unable to run. Your task is to ensure that the background services are running and that the Prime Factorization service still performs reliably under load.

Your mission is to adjust the background services configuration to ensure they can run, and later run the Locust testing and analyze all the service resource consumption.

## Objective

Deploy the Prime Factorization V2 Service and its associated background services on OpenShift, and adjust the configuration to ensure that:
- The background services are divided to one in each of the three QoS classes: Guaranteed, Burstable, and BestEffort.
- The Prime Factorization service continues to perform reliably under load (as per the previous lab).
- After adjusting the background services, run the Locust testing again and observe the CPU utilization across the services.

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
- `background-services.yaml`: Defines the background services, one for each QoS class.

### 2. Deploy the Services
1. Deploy Prime Factorization first, if not already deployed.
2. Apply background services deployment:

    ```bash
    oc apply -f background-services.yaml
    ```
3. Verify the background services deployment:

    ```bash
    oc get pods
    ```

### 3. Adjust the Background Services
1. Adjust the **Guaranteed background service** to be able to run in Guaranteed QoS.
2. After adjusting the Guaranteed service, verify that it is running:

    ```bash
    oc get pods -l app=guaranteed
    ```
### 4. Monitor and Analyze Resource Utilization Before Running Locust
1. Before running the Locust test, monitor the CPU utilization of both the background services and the Prime Factorization service.
2. Use OpenShift's **Observe** > **Dashboards** to analyze the resource consumption
3. What is the CPU consumption of each service, is it consistent with the QoS definition?


### 4. Generate Load with Locust
After configuring the background services, run the Locust tests to simulate 700 users with a ramp-up of 50 users, as in the previous Prime Factorization lab.

1. Set the number of users to **700**, ramp-up to **50**, and set the route of the Prime Factorization service as the host.
2. Make sure to **only select the `PrimeFactorizationUser`** class in the Locust UI for load testing.

### 5. Monitor and Analyze Resource Utilization After Running Locust
1. During the Locust test, monitor the CPU and memory utilization of both the background services and the Prime Factorization service.
2. Use OpenShift's **Observe** > **Dashboards** to analyze the resource consumption of all the services
3. As the load on Prime Factorization increases, is the CPU consumption consistent with the QoS definition?
   - For **Guaranteed** services, check if the resource usage is getting throttled or the service is not receving the requested amount of CPU.
   - For **Burstable** services, observe how the service responds when the lacking CPU resources.
   - For **BestEffort** service, check if resource usage is still the same.

4. You can also use the OpenShift CLI to monitor the resource usage:

    ```bash
    oc top pods
    ```

### 6. Verify Success
- Confirm that all services are running under their respective QoS classes.
- Verify that the Prime Factorization service can handle the load without failures or degraded performance.
- Ensure that the background services are running correctly, and that resource consumption is as expected based on their QoS class.

### 7. Clean Up
Once you've completed the drill, stop the locust test and delete the project by running:

```bash
oc delete -f namespace.yaml
```
