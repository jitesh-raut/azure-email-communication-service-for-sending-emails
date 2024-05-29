import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

from_email = '<From_Address>'
to_email = '<receipients_email>'
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'test email via ACS'
message = 'This email message is sent from Azure Communication Service Email using SMTP.'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('<Host>', '<port>')
mailserver.starttls()
mailserver.login("<Azure Communication Services Resource name>|<Entra Application ID>|<Entra Tenant ID>","<Entra application credential secret>")
mailserver.sendmail(from_email, to_email, msg.as_string())
mailserver.quit()