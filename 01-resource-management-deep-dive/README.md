# Resource Management Deep Dive Lab

Welcome to the Resource Management Deep Dive Lab! In this exercise, you will troubleshoot and fix several applications that are not optimized. Each application is located in its respective folder, numbered **eggclicker**, **primefactors**, **primefactorsv2**, and **logaggregate**. Your objective is to identify and resolve the issues in each application, ensuring they are running correctly. The applications should be addressed in the order of the folders.

## Objective

- Identify the root causes for the failure of each application
- Learn the effects of overutlization and underutilization 
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

## Explore the Folders

Start by reviewing the contents of each folder. Each folder demonstrate a resource management issue. Here are the folders you will work with:

- **01-eggclicker**: A fun game
- **02-primefactors**: An important function in the cryptogrhpay field
- **03-primefactorsv2**: A cluster issue
- **04-logaggregate**: An important function in the data scince field
