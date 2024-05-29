# azure-email-communication-service-for-sending-emails
This repository offers resources and sample code for Azure Email Communication Services, including setup guides, domain provisioning, and email sending via Azure Email client and SMTP. It features Python scripts and authentication setup instructions for developers and IT professionals.

## Create and Manage Email Communication Service Resources

### Create the Email Communications Service Resource Using the Portal

1. Open the [Azure portal](https://portal.azure.com/) to create a new resource.
2. Search for Email Communication Services.

   ![Screenshot showing how to search Email Communication Service in marketplace](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-communication-search.png)
   
3. Select Email Communication Services and press **Create**.

   ![Screenshot showing Create link to create Email Communication Service](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-communication-create.png)

4. Enter the required information in the Basics tab:
   - Select an existing Azure subscription.
   - Select an existing resource group, or create a new one by clicking the **Create new** link.
   - Provide a valid name for the resource.
   - Select the region where the resource needs to be available.
   - Select the data location.
   - To add tags, click **Next: Tags** and add any name/value pairs.

   ![Screenshot showing the summary for review and create Email Communication Service](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-communication-create-review.png)

5. Click **Next: Review + create**.
6. Wait for the validation to pass, then click **Create**.
7. Wait for the deployment to complete, then click **Go to Resource** to open the Email Communication Service overview.

   ![Screenshot showing the overview of Email Communication Service resource](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-communication-overview.png)

---

## Provision Azure Managed Domain

1. Open the Overview page of the Email Communications Service resource created in the above steps.
2. Create an Azure Managed Domain using one of the following options:

   **Option 1:** Click the 1-click add button under Add a free Azure subdomain. Continue to step 3.

   ![Screenshot showing 1-click add button for Azure subdomain](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-add-azure-domain.png)

   **Option 2:** Click **Provision Domains** on the left navigation panel.

   ![Screenshot showing Provision Domains in the left navigation panel](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-add-azure-domain-navigation.png)

   Click **Add domain** on the upper navigation bar. Select Azure domain from the dropdown.

3. Wait for the deployment to complete.

   ![Screenshot showing domain deployment progress](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-add-azure-domain-progress.png)

4. Once the domain is created, you see a list view with the new domain.

   ![Screenshot showing the created domain](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-add-azure-domain-created.png)

5. Click the name of the provisioned domain to open the overview page for the domain resource type.

   ![Screenshot showing the domain overview page](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-azure-domain-overview-expanded.png#lightbox)

Azure Communication Services automatically configures the required email authentication protocols. The email domain is now ready to send emails.

---

## Create and Manage Communication Services Resources

To create an Azure Communication Services resource:

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. In the upper-left corner of the page, select **+ Create a resource**.
3. Search for and select **Communication Service**, then select **Create**.
4. Configure your Communication Services resource by specifying the following details:
   - Subscription
   - [Resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) (create a new one or choose an existing resource group)
   - Name of the Communication Services resource
   - Geography associated with the resource

Review the configuration, add tags in the next step if required, and click **Create**.

---

## Connect a Verified Email Domain

1. In the Azure Communication Service Resource overview page, click **Domains** on the left navigation panel under Email.

   ![Screenshot showing the left navigation panel for linking Email Domains](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-domains.png)

2. Select one of the options below:
   - Click **Connect domain** in the upper navigation bar.
   - Click **Connect domain** in the splash screen.

3. Filter and select one of the verified domains by:
   - Subscription
   - Resource Group
   - Email Service
   - Verified Domain

   ![Screenshot showing how to filter and select one of the verified email domains to connect](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-domains-connect-select.png)

4. Click **Connect**.

---

## Sending an Email Using Python Code (Connection String Authentication)

Below is the sample code:

```python
# send-email.py

from azure.communication.email import EmailClient

def main():
    try:
        connection_string = "<ACS_CONNECTION_STRING>"
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "<SENDER_EMAIL_ADDRESS>",
            "recipients":  {
                "to": [{"address": "<recepient1email>" },{"address": "<recepient2email>" }],
            },
            "content": {
                "subject": "<Subject>",
                "plainText": "<Body Text>",
            }
        }
        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)

main()
```

### Before Running the Sample for the First Time

1. Open an instance of PowerShell, Windows Terminal, Command Prompt, or equivalent program and navigate to the directory where you'd like to clone the sample.
2. `git clone https://github.com/Azure-Samples/communication-services-python-quickstarts.git`

### Create a Virtual Environment

Navigate to the `send-email` directory in the console. Create a virtual environment and activate it using the following commands:

```cmd
python -m venv venv
.\venv\Scripts\activate
```

### Install the Packages

Execute the following command to install the SDK:

```cmd
pip install azure-communication-email
```

### Locally Configure the Application

Open the `send-email.py` file and configure the following settings:
- `connection_string`: Replace `<ACS_CONNECTION_STRING>` with the connection string found within the 'Keys' blade of the Azure Communication Service resource.
- `sender_address`: Replace `<SENDER_EMAIL_ADDRESS>` with the sender email address obtained from the linked domain resource.
- `recipient_address`: Replace `<recepientemail>` with the recipient email address.

### Run Locally

Execute the following command to run the app:

```cmd
python ./send-email.py
```

---

## Sending an Email Using Python Code (SMTP)

### Create Authentication Credentials for Sending Emails Using SMTP

#### Prerequisites:

- An Entra application with access to the Azure Communication Services Resource. [Register an application with Microsoft Entra ID and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#register-an-application-with-microsoft-entra-id-and-create-a-service-principal)
- A client secret for the Entra application with access to the Azure Communication Service Resource. [Create a new client secret](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret)

### Register an Application with Microsoft Entra ID and Create a Service Principal

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) as at least a [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator).
2. Browse to **Identity** > **Applications** > **App registrations**, then select **New registration**.
3. Name the application, for example "example-app".
4. Select a supported account type, which determines who can use the application.
5. Under **Redirect URI**, select **Web** for the type of application you want to create. Enter the URI where the access token is sent to.
6. Select **Register**.

   ![Screenshot showing how to create an application](https://learn.microsoft.com/en-us/entra/identity-platform/media/howto-create-service-principal-portal/create-app.png)

### Create a Custom Email Role for the Entra Application

The Entra application must be assigned a role with both the **Microsoft.Communication/CommunicationServices/Read** and the **Microsoft.Communication/EmailServices/write** permissions on the Azure Communication Service Resource. This can be done either by using the **Contributor** role or by creating a **custom role**. Follow these steps to create a custom role by cloning an existing role:

1. Navigate to the subscription, resource group, or Azure Communication Service Resource where you want the custom role to be assignable and then open **Access control (IAM)**.

   ![Screenshot showing Access control](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-iam.png)

2. Click the **Roles** tab to see a list of all the built-in and custom roles.
3. Search for a role you want to clone, such as the Reader role.
4. At the end of the row, click the ellipsis (...) and then click **Clone**.

   ![Screenshot showing cloning a role](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-clone.png)

5. Click the **Basics** tab and give a name to the new role.

   ![Screenshot showing creating a name for a new custom role](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-basics.png)

6. Click the **Permissions** tab and click **Add permissions**. Search for **Microsoft.Communication** and select **Azure Communication Services**.

   ![Screenshot showing adding permissions for a new custom role](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-permissions.png)

7. Select the **Microsoft.Communication/CommunicationServices** **Read** and the **Microsoft.Communication/EmailServices** **Write** permissions. Click **Add**.

   ![Screenshot showing adding Azure Communication Services' permissions](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-add-permissions.png)

8. Review the permissions for the new role. Click **Review + create** and then **Create** on the next page.

   ![Screenshot showing reviewing the new custom role](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-review.png)

### Assign the Custom Email Role to the Entra Application

1. Navigate to the subscription, resource group, or Azure Communication Service Resource where you want the custom role to be assignable and then open **Access control (IAM)**.

   ![Screenshot showing Access control](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/smtp-custom-role-iam.png)

2. Click **+Add** and then select **Add role assignment**.

   ![Screenshot showing selecting Add role assignment](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-add-role-assignment.png)

3. On the **Role** tab, select the custom role created for sending emails using SMTP and click **Next**.

   ![Screenshot showing selecting the custom role](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-select-custom-role.png)

4. On the **Members** tab, choose **User, group, or service principal** and then click **+Select members**.

   ![Screenshot showing choosing select members](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-select-members.png)

5. Use the search box to find the **Entra** application that you'll use for authentication and select it. Then click **Select**.

   ![Screenshot showing selecting the Entra application](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-select-entra.png)

6. After confirming the selection, click **Next**.

   ![Screenshot showing reviewing the assignment](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-select-review.png)

7. After confirming the scope and members, click **Review + assign**.

   ![Screenshot showing assigning the custom role](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-select-assign.png)

### Create the SMTP Credentials from the Entra Application Information

#### SMTP Authentication Username

Azure Communication Services allows the credentials for an Entra application to be used as the SMTP username and password. The username consists of the following three parts and can be pipe or dot delimited:

1. The Azure Communication Service Resource name.
   
   ![Screenshot showing finding the resource name](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-resource-name.png)

2. The Entra Application ID.
   
   ![Screenshot showing finding the Entra Application ID](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-entra-details.png)

3. The Entra Tenant ID.
   
   ![Screenshot showing finding the Entra Tenant ID](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-entra-tenant.png)

**Dot-delimited Format:**

```plaintext
username: <Azure Communication Services Resource name>.<Entra Application ID>.<Entra Tenant ID>
```

**Pipe-delimited Format:**

```plaintext
username: <Azure Communication Services Resource name>|<Entra Application ID>|<Entra Tenant ID>
```

#### SMTP Authentication Password

The password is one of the Entra application's client secrets.

   ![Screenshot showing finding the Entra client secret](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/media/email-smtp-entra-secret.png)

- **Authentication**: Username and password authentication is supported using Entra application details as the credentials. The Azure Communication Services SMTP service will use the Entra application details to get an access token on behalf of the user and use that to submit the email. Because the Entra token isn't cached, access can be revoked immediately by either changing the Entra application client secret or by changing the access controls for the Azure Communication Services Resource.
- **Azure Communication Service**: An Azure Communication Services Resource with a connected Azure Communication Email Resource and domain is required.
- **Transport Layer Security (TLS)**: Your device must be able to use TLS version 1.2 and above.
- **Port**: Port 587 is required and must be unblocked on your network. Some network firewalls or ISPs block ports because that's the port that email servers use to send mail.
- **DNS**: Use the DNS name `smtp.azurecomm.net`. Don't use an IP address for the Microsoft 365 or Office 365 server, as IP Addresses aren't supported.

### How to Set Up SMTP AUTH Client Submission

Enter the following settings directly on your device or in the application as their guide instructs (it might use different terminology than this article). Provided your scenario aligns with the prerequisites for SMTP AUTH client submission, these settings allow you to send emails from your device or application using SMTP commands.

| Device or Application Setting | Value                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Server / smart host            | smtp.azurecomm.net                                                                                                   |
| Port                           | Port 587                                                                                                             |
| TLS / StartTLS                 | Enabled                                                                                                              |
| Username and password          | Enter the Entra application credentials from an application with access to the Azure Communication Services Resource |

#### Sample Code

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = '<SENDER_EMAIL_ADDRESS>'
to_email = '<recipients_email_address>'
user_name = '<Azure Communication Services Resource name>.<Entra Application ID>.<Entra Tenant ID>'
password = '<Entra application credential secret>'
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = '<subject_text>'
message = '<content_body>'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('<host>', <port>)
mailserver.starttls()
mailserver.login(user_name, password)
mailserver.sendmail(from_email, to_email, msg.as_string())
mailserver.quit()
```

# Azure Communication Service Costing

## Email Communication Service:

Sending Emails: The cost is based on the number of emails sent and the amount of data transferred. The pricing is $0.00025 per email sent and $0.00012 per MB of data transferred​ ​.
Example Calculation: If you send 1000 emails, each of 1 MB, the cost would be:
Email cost: 1000 emails x $0.00025 = $0.25
Data transfer cost: 1000 MB x $0.00012 = $0.12
Total cost for 1000 emails: $0.25 + $0.12 = $0.37

ref: [GitHub](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/communication-services/concepts/email-pricing.md)

## Communication Services:

SMS, Voice, and Video: If you use additional features like SMS, voice, or video calls, the costs will depend on the specific services and usage volumes. Pricing details for these services can be found on the Azure Communication Services pricing page.

ref:
[Communication-services-pricing](https://azure.microsoft.com/en-us/pricing/details/communication-services/)

[Communication-services-pricing](https://azure.microsoft.com/en-us/pricing/details/communication-services/)

[Microsoft-Learn](https://learn.microsoft.com/en-us/azure/communication-services/concepts/email/email-overview)

## App Registration:

App Registrations themselves do not incur direct costs, but the resources and services accessed through the registered apps might incur charges depending on their usage.
