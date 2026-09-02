# my application.log file data
'''
31-08-2026 18:01:12:PM | INFO | application | Application started successfully
31-08-2026 18:02:05:PM | INFO | user | User login successful | UserID: 102
31-08-2026 18:03:18:PM | WARNING | system | Memory usage high | Usage: 85%
31-08-2026 18:04:42:PM | ERROR | database | Database connection failed
31-08-2026 18:05:10:PM | INFO | database | Retry successful | Connection restored
31-08-2026 18:06:25:PM | ERROR | payment | Payment service unavailable
31-08-2026 18:07:33:PM | INFO | student | Student added successfully | Name: Arjun, ID: 501
31-08-2026 18:08:14:PM | INFO | course | New course created | CourseID: PY101
31-08-2026 18:09:27:PM | WARNING | server | High CPU usage detected | Usage: 92%
31-08-2026 18:10:05:PM | INFO | user | Password updated successfully | UserID: 215
31-08-2026 18:11:48:PM | ERROR | authentication | Invalid login attempt | UserID: 309
31-08-2026 18:12:30:PM | INFO | session | User session created successfully
31-08-2026 18:13:22:PM | WARNING | storage | Disk space running low | Available: 10GB
31-08-2026 18:14:15:PM | ERROR | api | API request timed out | Endpoint: /students
31-08-2026 18:15:40:PM | INFO | api | API request completed successfully | Status: 200
31-08-2026 18:16:12:PM | INFO | student | Student profile updated | ID: 444
31-08-2026 18:17:55:PM | WARNING | network | Network latency increased | Latency: 450ms
31-08-2026 18:18:21:PM | ERROR | file | File upload failed | File: assignment.pdf
31-08-2026 18:19:34:PM | INFO | file | File uploaded successfully | File: report.csv
31-08-2026 18:20:16:PM | INFO | email | Welcome email sent successfully | UserID: 501
31-08-2026 18:21:08:PM | ERROR | email | Email delivery failed | Reason: Invalid address
31-08-2026 18:22:45:PM | WARNING | application | Slow response detected | ResponseTime: 3.5s
31-08-2026 18:23:19:PM | INFO | backup | Database backup completed successfully
31-08-2026 18:24:37:PM | ERROR | backup | Backup process failed | Reason: Insufficient storage
31-08-2026 18:25:11:PM | INFO | payment | Payment processed successfully | TransactionID: TXN789
31-08-2026 18:26:29:PM | WARNING | security | Multiple failed login attempts detected | IP: 192.168.1.10
31-08-2026 18:27:43:PM | INFO | course | Student enrolled successfully | StudentID: 444, CourseID: ML202
31-08-2026 18:28:56:PM | ERROR | system | Unexpected application error occurred
31-08-2026 18:29:18:PM | INFO | system | Error recovery completed successfully
31-08-2026 18:30:45:PM | INFO | application | Application shutdown completed successfully
'''

error_occurrences=0
warning_occurrences=0
info_occurrences=0
with open("application.log","r") as file:
    with open("errors.txt","a") as errorfile:
        with open("warings.txt","a") as waringfile:
            datafile =file.readlines()
            print(f"The total log is {len(datafile)}")
            for line in datafile:
                # print(line)
                if "INFO" in line:
                    info_occurrences+=1
                if "ERROR" in line:
                    error_occurrences+=1
                    errorfile.write(line)
                if "WARNING" in line:
                    warning_occurrences+=1
                    waringfile.write(line)

print(f"Count of info  occurrences: {info_occurrences},Count of error  occurrences: {error_occurrences}, Count of warning  occurrences: {warning_occurrences}")
