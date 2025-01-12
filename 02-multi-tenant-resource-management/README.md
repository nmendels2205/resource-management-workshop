# ScaleSurfers Troubleshooting Lab

Welcome to the ScaleSurfers Troubleshooting Lab! In this exercise, you will troubleshoot and fix several applications that are not able to run properly. Each application is located in its respective folder **silentrunner**, **horizonhopper**, **zerohero**, and **cloudchaser**. Your objective is to identify and resolve the issues in each application, ensuring they are running correctly. The applications should be fixed in the order of the folders.

## Objective

- Identify the root causes for the failure of each application.
- Please, Do **not modify namespaces or objects outside the scope of this lab**.

---

## Prerequisites

1. **Login to OpenShift Console**: Use the provided credentials to log in to the OpenShift web console.
2. **Download and Configure the OpenShift CLI (`oc`)**:
   - Log in to the OpenShift web console.
   - In the top-right corner, click on your username and select **Copy Login Command**.
   - Under the question mark icon, find the **Command Line Tools** section and download the appropriate CLI for your operating system.
   - Add the CLI to your system’s PATH.
   - Use the login command to authenticate with your cluster.
3. Familiarity with troubleshooting applications in OpenShift/Kubernetes environments.

---

## Steps

### 1. Explore the Folders

Start by reviewing the contents of each folder. Each folder contains an application that is currently not running. Here are the folders you will work with:

- **01-silentrunner**: Pods are not being created
- **02-horizonhopper**: One of the pods in not being created
- **03-zerohero**: The application is crashing
- **04-cloudchaser**: Pods are not being created

Each folder contains the `install.yaml` file to install the application. You may need to investigate deployment configurations, logs, events, or any other resources in the folder/cluster.

---

### 2. Troubleshoot and Fix Application in Each Folder

1. **Check events**: Ensure that there are enough resources for the application to run by checking CPU and memory limits.

    ```bash
    oc get events
    ```

2. **Inspect Deployment/Pod Status**: Check the deployment and pod status for errors or issues related to deployment.

    ```bash
    oc describe deployment <deployment-name>
    ```
    ```bash
    oc describe pod <pod-name>
    ```
    ```bash
    oc describe replicaset <replicaset-name>
    ```

3. **Apply Fixes**: After identifying the issue, implement the required fix.

---

## Conclusion

By the end of this lab, you should have successfully fixed all the applications, ensuring that they are running correctly.

Good luck, and happy troubleshooting!

