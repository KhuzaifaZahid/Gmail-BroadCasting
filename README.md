# Gmail-BroadCasting
#Overview: 

  This project allows users to send a single email to multiple recipients at once with just one click. Whether it's for sending company-wide announcements, marketing updates, or group communications, this application simplifies the process of sending emails to a list of recipients through Gmail's SMTP server.

#Features:

**Mass Emailing:** Send a single email to multiple recipients, such as a department or a group of users, with a single click.
Flexible Department Selection: Users can select a specific department (e.g., Sales, Support, HR, IT), and the email will be sent to the corresponding email addresses of that department.

**Real-Time Feedback:** Once the emails are sent, users will receive a popup notification confirming the result of the email-sending process (whether successful or failed for each recipient).

**Simple Interface:** The application provides a clean and user-friendly interface for entering the email subject, body, and selecting the department.

**Customizable:**
You can easily update the department email list by modifying a separate Python file for each department, making the system extensible.

**Technologies Used:**

**Python:** The backend is powered by Flask, a lightweight web framework.

**HTML/CSS:** The frontend is designed with HTML and CSS for a responsive and clean user interface.

**SMTP Protocol:** The email-sending functionality is powered by Gmail’s SMTP server to send messages to recipients.

**How It Works**

**Select Department:** Choose the department you want to send an email to. Each department has a predefined list of email addresses.

**Enter Subject & Body:** Fill in the subject and body of your email.

**Click Send:** Upon submission, the email is sent to all the selected department’s recipients.

**Feedback:** A popup message will inform you about the success or failure of sending the email to each recipient.

**How to Use**

Clone the repository to your local machine.

Install the required dependencies using pip install -r requirements.txt.

Set up your Gmail account and enable Less Secure Apps or use an App Password for better security.

Run the Flask server:python app.py.

Open a browser and navigate to http://127.0.0.1:5000/.

Fill in the subject, body, and select a department.

Click "Send Email" to broadcast the message.

**Customization**

**Email List:** You can update the email lists for each department by modifying the respective Python files (e.g., sales.py, support.py, etc.).

**SMTP Settings:** Update the smtp_server, port, email_address, and app_password variables in the app.py to use your Gmail account and app password for sending emails.
