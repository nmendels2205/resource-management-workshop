# Egg Clicker Game

Welcome to the Egg Clicker Game! Your mission is to help get the game up and running successfully on OpenShift. For some reason, the game won't reach the **"You cracked the egg!"** screen. Can you help troubleshoot?

## Objective
The goal is to deploy the Egg Clicker Game on OpenShift and make it work so that you can reach the **"You cracked the egg!"** screen.

## Prerequisites
1. Log in to the OpenShift cluster web console with the provided credentials.
2. Download and configure the OpenShift CLI (`oc`):
   - Log in to the OpenShift web console.
   - In the top-right corner, click on your username and select **Copy Login Command**.
   - In the top-right corner, under the question mark icon, find the **Command Line Tools** section and download the appropriate CLI for your operating system.
   - Add the downloaded CLI to your system's PATH.
   - Use the login command provided to authenticate with your cluster.
3. Familiarity with deploying applications on OpenShift.

## Steps

### 1. Explore the Game Files
Take a moment to explore the files in this repository. The game is containerized and ready to be deployed on OpenShift.

Key files:
- `namespace.yaml`: Defines the namespace in which the game will run.
- `install.yaml`: Contains the game installation configuration.

### 2. Deploy the Application
1. Apply the namespace and game installation configurations:

    ```bash
    oc apply -f namespace.yaml
    oc apply -f install.yaml
    ```

2. Verify that the resources have been created:

    ```bash
    oc get pods
    oc get svc
    ```

3. Get the service's route to access the game:

    ```bash
    oc get route
    ```

### 4. Test the Game
Open the route URL in your browser and try running the game. Your task is to get to the **"You cracked the egg!"** screen. 

### 5. Troubleshoot and Adjust
If the game doesn't work as expected, investigate the issue. Think about what might be preventing it from functioning correctly. Adjust the necessary settings or configurations to ensure the game runs successfully.

### 6. Verify Success
Once you see the **"You cracked the egg!"** screen, you've successfully completed this drill! 🎉

## Tips
- Use the OpenShift web console or CLI to monitor the pod's status.
- Use the OpenShift monitoring stack dashboards by navigating to **Observe** > **Dashboards** in the web console.
- Review the logs and events of the game pod if you encounter issues:

    ```bash
    oc logs <pod-name>
    oc get events
    oc describe pod <pod-name>
    ```

## Next Steps
Once you've completed this drill, **delete the project** by running:

```bash
oc delete -f namespace.yaml
```

Afterwards, you can proceed to the next exercises in the lab.

Good luck, and happy troubleshooting!
