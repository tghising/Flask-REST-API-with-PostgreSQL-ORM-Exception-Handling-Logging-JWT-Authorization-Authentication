from threading import Thread
from flask_mail import Message

import app
from app import mail


def send_async_email(mail_app, msg):
    with mail_app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise Exception("[MAIL SERVER] not working")
            # raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
