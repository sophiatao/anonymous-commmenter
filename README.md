## Anonymous classroom commenter
Allows students to anonymously ask questions, and instructors to dynamically put up course information throughout lecture

![Alt text](Resources/screenshot.png?raw=true "Screenshot")

### Usage instructions for 2DM3 TAs
1. Clone repository
2. Update Theorems.txt with relevant theorems for the class
3. `python3 app.py`
4. Instruct students to connect to printed IP address and port
5. Refresh page to see new comments or to fetch updated theorems

### Troubleshooting
1. Make sure everybody is connected to the same WiFi network
2. Make sure incoming connections are allowed (check Firewall settings)

### TODO
1. Implement auto polling or webhooks so no refreshing is required
2. Alert when students post new comment
3. Alert when new theorems posted

### Credits
Base app cloned from https://github.com/macloo/flask-forms.git
