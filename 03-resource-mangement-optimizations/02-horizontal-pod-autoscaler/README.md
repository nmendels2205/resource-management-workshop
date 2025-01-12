# Prime Factorization Autoscaling

Welcome to the **Prime Factorization Autoscaling Lab**! In this exercise, your task is to ensure that the service performs reliably under load while utilizing the **Horizontal Pod Autoscaler (HPA)** feature.

Your mission is to create a CPU-based HPA that will scale the application to handle **1500 users** with a **50-user ramp-up** in Locust testing, without any failures (requests exceeding 1 second).

---

## Objective

Deploy a slightly modified Prime Factorization Service on OpenShift and configure a CPU-based HPA to meet the following requirements:
- Handle **1500 concurrent users** with a **50-user ramp-up** without any request failures.
- Maintain a response time of approximately **1000ms** for the given calculation `111111111111111` under load.

---

## Prerequisites

1. Log in to the OpenShift cluster web console using the provided credentials.
2. Download and configure the OpenShift CLI (`oc`):
   - Log in to the OpenShift web console.
   - Click your username in the top-right corner and select **Copy Login Command**.
   - Under the question mark icon in the top-right corner, find the **Command Line Tools** section and download the appropriate CLI for your operating system.
   - Add the downloaded CLI to your system's PATH.
   - Use the login command to authenticate with your cluster.
3. Familiarity with deploying and configuring applications on OpenShift.

---

## Steps

### 1. Explore the Files
Familiarize yourself with the files in this repository. The service is containerized and includes configurations for deployment and testing.

Key files:
- `namespace.yaml`: Defines the namespace where the service will run.
- `install.yaml`: Contains the slightly modified Prime Factorization service deployment.
- `locustfile.py`: A load testing script for generating traffic to the service (same as in the first lab).

---

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

3. Retrieve the service's route for access:

    ```bash
    oc get route
    ```

---

### 3. Create an HPA Object
1. Apply an HPA object using the following structure. Replace placeholders with appropriate values based on your observations:

    ```yaml
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: primefactors
      namespace: hyperburst-application
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: primefactors
      minReplicas: 2
      maxReplicas: # Replace with the maximum number of replicas
      metrics:
        - type: Resource
          resource:
            name: cpu
            target:
              type: Utilization
              averageUtilization: # Replace with the desired CPU utilization percentage
    ```

2. Save and apply the configuration:

    ```bash
    oc apply -f hpa.yaml
    ```

---

### 4. Generate Load Using Locust
1. Open the Locust web interface in the `locust-testing` namespace by retrieving its route:

    ```bash
    oc get route -n locust-testing
    ```

2. Alternatively, run Locust locally if required.

3. In the Locust UI:
   - Set **1500 users** as the total number of users.
   - Configure a **50-user ramp-up**.
   - Enter the service route as the host.
   - Select only the `PrimeFactorizationUser` class for testing.

4. Start the Locust test and monitor the results.

---

### 5. Monitor and Adjust
1. Observe the service's behavior during the test.
2. If request failures or high response times occur:
   - Investigate the issue.
   - Adjust the HPA configuration (e.g., increase max replicas or modify CPU utilization thresholds).
   - Reapply the updated configuration.
3. Monitor the service's performance after adjustments.

---

### 6. Verify Success
- Confirm that the service can handle **1500 concurrent users** in Locust without any request failures.
- Ensure that the response time for calculating the prime factors of `111111111111111` remains approximately **1000ms**, even under load.

---

### 7. Clean Up
After completing the lab, stop the Locust test

---

Congratulations on completing the **Prime Factorization Autoscaling Lab**! 🎉
