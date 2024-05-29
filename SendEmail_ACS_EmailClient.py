from azure.communication.email import EmailClient
def main():
    try:
        connection_string = "<Connection_String_From_Email_Communication_Service>"
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "<from_address>",
            "recipients":  {
                "to": [{"address": "<recepients_email>" }],
            },
            "content": {
                "subject": "Test Email",
                "plainText": "Hello world via email.",
            }
        }
        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)
main()
