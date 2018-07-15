# Application Name

Website Blocker

# Application Overview

This application blocks given websites for a given amount of time by adding the hostnames of the given websites to block (call this x) and by adding the IP address of the given website to redirect to (call this y) in the system `hosts` file. Each x is mapped to y in the file. So, when users try to access the websites they want blocked, they're redirected to a different website. 

This application handles invalid user requests.

# Application Requirement

Python 3

# Application Usage

## `app.py`

This file offers the most flexibility because of the parametrization of values. However, it comes at a cost. The file needs to be running throughout the duration of the time the users want to block websites.

Run `python <path-to-python_applications>/website_blocker/app.py --os <macOS, Linux, or Windows> --redirect_site <URL> --websites <URL-1> <Optional URL-2> <...> --start_time <Hour: 0 - 23> <Minute: 0 - 59> --end_time <Hour: 0 - 23> <Minute: 0 - 59>`

## `app_mac_linux_schedule.py`

This file can only be used by the macOS or Linux operating systems.

This file doesn't offer any flexibility because values can't be parametrized. So, they have to be hardcoded. But this file doesn't have to be manually run by users. It can be scheduled by the operating system to run automatically. So, the file becomes a process and constantly runs but only blocks websites for the given time duration.

1. Run `sudo crontab -e` (the `hosts` file is protected by the system, so root privileges are required to modify it)
2. Enter your password if prompted
3. At the end of the file that was just opened, type `@reboot python3 <path-to-python_applications>/website_blocker/app_mac_linux_schedule.py`
4. Save and exit the file

## `app_windows_schedule.pyw`

This file can only be used by the Windows operating system.

This file doesn't offer any flexibility because values can't be parametrized. So, they have to be hardcoded. But this file doesn't have to be manually run by users. It can be scheduled by the operating system to run automatically. So, the file becomes a process and constantly runs but only blocks websites for the given time duration.

1. Open `Task Scheduler`
2. Click `Create Task`
3. Click `General`
4. Type in a name for the task
5. Check `Run with highest privileges` (the `hosts` file is protected by the system, so Administrator privileges are required to modify it)
6. Under `Configure for:`, select the version of Windows you're currently using
7. Click `Triggers`
8. Under `Begin the task:`, select `At Startup`
9. Click `OK`
10. Click `Actions`
11. Under `Action:`, select `Start a program`
12. Under `Program/script:`, browse for the `app_windows_schedule.pyw` file
13. Double click the file
14. Click `OK`
15. Click `Conditions`
16. Uncheck `Start the task only if the computer is on AC power`
17. Click `OK`
18. Close the `Task Scheduler`
