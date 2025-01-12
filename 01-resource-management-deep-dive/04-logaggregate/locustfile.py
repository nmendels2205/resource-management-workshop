from locust import HttpUser, task, between
import random
from datetime import datetime, timedelta

class LogAggregationUser(HttpUser):
    wait_time = between(1, 3)

    # List of predefined log messages
    predefined_messages = [
    "Application started. Initializing system configurations, loading user preferences, and establishing connections to the necessary databases. All services are running on default settings. Startup sequence completed successfully.",
    "User logged in. User ID: 12345. User email: user@example.com. IP Address: 192.168.1.1. Login attempt was successful, and the user has access to the following modules: Dashboard, Reports, and Settings.",
    "Data received from API. API endpoint: /get-user-data. Request parameters: {'user_id': 12345, 'timestamp': 1618938400}. Response payload: {'status': 'success', 'data': {...}}. Processing data for the next step.",
    "Database connection established. Connected to PostgreSQL database at host db.example.com. Database schema: public. Connection pool size: 10. Query execution time: 15ms. Connection established successfully.",
    "File uploaded successfully. File name: report_2023_q1.pdf. File size: 5MB. Upload time: 2025-01-11 12:34:56. File checksum: abc123xyz456. File is now available in the 'Reports' directory.",
    "Error occurred while processing data. Error details: {'message': 'Null reference exception', 'code': 500, 'stack_trace': 'at ProcessData() in /src/data_processor.py:45'. Attempting retry in 3 seconds.",
    "User logged out. User ID: 12345. Session duration: 45 minutes. Last activity timestamp: 2025-01-11 12:19:23. All session data has been saved, and the user has been successfully logged out.",
    "System shutdown initiated. Reason: scheduled maintenance. All services will be stopped in 5 minutes. Database connections will be closed, and logs will be flushed. Expected downtime: 30 minutes.",
    "Connection lost, retrying. Last successful connection was at 2025-01-11 12:32:00. Reconnecting to server at 192.168.1.100:8080. Attempt 1/5. Timeout: 30 seconds.",
    "Data saved to database. Table: users. Rows affected: 1. Query execution time: 120ms. Data: {'user_id': 12345, 'name': 'John Doe', 'email': 'user@example.com'}. Operation completed successfully.",
    "Request timed out. API endpoint: /submit-data. Timeout after 30 seconds. Request parameters: {'data': 'big dataset here'}. Retrying in 10 seconds. Check server status and network connection.",
    "Unexpected error in the application. Error type: 'IndexError', message: 'Index out of range'. Stack trace: 'at process_data() in /src/data_handler.py:34'. Investigating the issue with team lead.",
    "Service is restarting. Service name: DataProcessingService. Reason: configuration update. Current status: shutting down gracefully. Expected restart time: 2025-01-11 12:45:00.",   
    "Memory usage is high. Current memory usage: 4GB. System total memory: 8GB. The application is consuming 50% of system memory. No memory leaks detected. Scaling system resources recommended.",  
    "Disk space running low. Current disk usage: 90%. Total disk space: 100GB. Remaining disk space: 10GB. Alert sent to system administrator. Consider increasing disk allocation or cleaning up old logs."
    ]

    # Function to generate a random timestamp within the past year
    def random_timestamp(self):
        now = datetime.now()
        delta_days = random.randint(0, 365)
        delta_hours = random.randint(0, 24)
        random_date = now - timedelta(days=delta_days, hours=delta_hours)
        return random_date.strftime("%Y-%m-%dT%H:%M:%S")

    @task
    def submit_logs(self):
        # Create random logs for testing
        logs = []
        total_logs = random.randint(500, 5000)
        for _ in range(total_logs):  # Number of logs per request
            log = {
                "level": random.choice(["INFO", "ERROR", "WARN"]),
                "timestamp": self.random_timestamp(),  # Random timestamp
                "message": random.choice(self.predefined_messages)  # Random predefined message
            }
            logs.append(log)

        # Send the logs to the Flask application
        self.client.post("/add-logs", json={"logs": logs})
