import base64
import urllib.parse
from os import environ

from chatterbot import ChatBot  # type: ignore
from chatterbot.trainers import ListTrainer  # type: ignore
from twilio.request_validator import RequestValidator  # type: ignore
from twilio.rest import Client  # type: ignore

client = Client(environ["TWILIO_ACCOUNT_SID"], environ["TWILIO_AUTH_TOKEN"])


DB_FOLDER = "/tmp"
DB_FILE = "jareth.sqlite3"
DB_PATH = f"sqlite:///{DB_FOLDER}/{DB_FILE}"
TWILIO_NUMBER = environ["TWILIO_NUMBER"]

c = [
    "You remind me of the babe.",
    "What babe?",
    "The babe with the power.",
    "What power?",
    "The power of voodoo.",
    "Who do?",
    "You do.",
    "Do what?",
    "Remind me of the babe.",
]
chatbot = ChatBot("Jareth", database_uri="sqlite:////tmp/db.sqlite3")
trainer = ListTrainer(chatbot)
trainer.train(c)


def send_message(to, message):
    print(f"Sending: '{message}' to {to}")
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=to,
        )
        return message.sid
    except Exception as ex:
        print("ERROR: ", ex)
        return


def lambda_handler(event, context):
    print("Event: ", event)

    if event.get("isBase64Encoded", False):
        dec = base64.b64decode(event.get("body"))
        decstr = str(dec, "utf-8")
        formdata = {k: v[0] for k, v in urllib.parse.parse_qs(decstr).items()}
        validator = RequestValidator(environ["TWILIO_AUTH_TOKEN"])
        uri = f"{event['headers']['X-Forwarded-Proto']}://{event['headers']['Host']}{event['path']}"
        signature = event["headers"]["X-Twilio-Signature"]
        print(f"uri: {uri}")
        print(f"formdata: {formdata}")
        print(f"signature: {signature}")
        request_valid = validator.validate(
            uri=uri,
            params=formdata,
            signature=signature,
        )
        print(f"Request valid: {request_valid}")

        response = chatbot.get_response(formdata["Body"])
        print("From: ", formdata["From"])
        print("Response: ", response)
        send_message(formdata["From"], response)
        return {"statusCode": 200, "body": response}
    return {"statusCode": 500, "body": "error"}
