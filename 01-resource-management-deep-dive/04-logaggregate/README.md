# Log Aggregation

Welcome to the Log Aggregation lab! In this exercise, we will simulate node memory pressure and observe the eviction of non-optimized pods.

## Objective

Deploy the Log Aggregation service and its associated background services on OpenShift, run a Locust test, and analyze the outcomes under memory pressure conditions.

## Prerequisites

1. Log in to the OpenShift cluster web console with the provided credentials.
2. Download and configure the OpenShift CLI (`oc`):
   - Log in to the OpenShift web console.
   - In the top-right corner, click on your username and select **Copy Login Command**.
   - Under the question mark icon in the top-right corner, locate the **Command Line Tools** section and download the appropriate CLI for your operating system.
   - Add the downloaded CLI to your system's PATH.
   - Use the provided login command to authenticate with your cluster.
3. Familiarity with deploying and configuring applications on OpenShift.

## Steps

### 1. Explore the Files
Take a moment to explore the files in this repository. The service is containerized and includes configurations for deployment and testing.

Key files:
- `namespace.yaml`: Defines the namespace in which the service will run.
- `install.yaml`: Contains the service deployment and configuration.
- `locustfile.py`: A load testing script for generating traffic to the service.
- `background-services.yaml`: Defines the background services, one for each QoS class.

### 2. Deploy the Services
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

3. Retrieve the service's route to access it:

    ```bash
    oc get route
    ```

4. Upload an example log to see the results:

    ```bash
    [{"level":"INFO","timestamp":"2025-01-01T12:00:00","message":"Application started. Initializing system configurations"}]
    ```

### 3. Deploy the Background Services
1. Apply the background services configuration:

    ```bash
    oc apply -f background-services.yaml
    ```

2. Verify the background services deployment:

    ```bash
    oc get pods
    ```

### 4. Generate Load with Locust
Run the Locust tests to simulate 50 users with a ramp-up of 50 users accessing the Log Aggregation service.

1. Open the Locust web interface running in `locust-testing` namespace by retrieving its route:

    ```bash
    oc get route -n locust-testing
    ```

2. In the Locust UI:
   - Set the number of users to **50**.
   - Set the ramp-up time to **50** users.
   - Enter the route of the Log Aggregation service as the host.
   - Ensure that **only the `LogAggregationUser` class** is selected for testing.

3. Start the Locust test.

### 5. Monitor Memory Utilization
1. Observe the pods in the namespace as Locust generates load:

    ```bash
    oc get pods -w
    ```

2. Refresh the Log Aggregation results by clicking **View Results** in the Log Aggregation UI and monitor memory consumption.

3. Use OpenShift's **Observe** > **Dashboards** to analyze memory consumption at the node or namespace level.

4. Investigate:
   - What happens to the background service pods?
   - What changes occur on the node under memory pressure?

5. Use the OpenShift CLI to monitor resource usage:

    ```bash
    oc top pods
    ```

### 6. Verify Success
- Confirm that only the background service pods in the namespace are evicted due to memory pressure.
- Confirm that the affected node enters a memory pressure state.

### 7. Clean Up
Once you have completed the drill, stop the Locust test and delete the project:

```bash
oc delete -f namespace.yaml
```
