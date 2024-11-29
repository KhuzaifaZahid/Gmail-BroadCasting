from flask import Flask, request, jsonify, render_template
import smtplib
from departments import DEPARTMENT_EMAILS  # Import department data

app = Flask(__name__, template_folder='html')  # 'html' is the new folder name

# Gmail SMTP Configuration
smtp_server = "smtp.gmail.com"
port = 587
email_address = "one.empire121@gmail.com"
app_password = "eyig dktn gnsx zyyj"  # Replace with your app password

# General function to send emails to multiple recipients
def send_email_to_multiple(recipients, subject, body):
    """
    Send email to multiple recipients individually using SMTP and return status.
    """
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(email_address, app_password)
            for recipient in recipients:
                try:
                    server.sendmail(email_address, recipient, message)
                except Exception as e:
                    return False, f"Failed to send email to {recipient}: {str(e)}"
        return True, "Emails sent successfully!"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Department-specific functions
def send_sales_email(subject, body):
    return send_email_to_multiple(DEPARTMENT_EMAILS["Sales"], subject, body)

def send_support_email(subject, body):
    return send_email_to_multiple(DEPARTMENT_EMAILS["Support"], subject, body)

def send_hr_email(subject, body):
    return send_email_to_multiple(DEPARTMENT_EMAILS["HR"], subject, body)

def send_it_email(subject, body):
    return send_email_to_multiple(DEPARTMENT_EMAILS["IT"], subject, body)

@app.route('/')
def index():
    """
    Render the main page with the form to send emails to departments.
    """
    return render_template('web.html', departments=list(DEPARTMENT_EMAILS.keys()))

@app.route('/send_email', methods=['POST'])
def send_email_route():
    """
    Handle the email-sending request and return response for popup message.
    """
    subject = request.form.get('subject')
    body = request.form.get('body')
    department = request.form.get('department')

    if not subject or not body or not department:
        return jsonify({"success": False, "message": "All fields are required!"})

    if department not in DEPARTMENT_EMAILS:
        return jsonify({"success": False, "message": "Invalid department!"})

    # Call department-specific functions
    if department == "Sales":
        success, message = send_sales_email(subject, body)
    elif department == "Support":
        success, message = send_support_email(subject, body)
    elif department == "HR":
        success, message = send_hr_email(subject, body)
    elif department == "IT":
        success, message = send_it_email(subject, body)

    return jsonify({"success": success, "message": message})

if __name__ == '__main__':
    app.run(debug=True)
