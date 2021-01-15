from flask_mail import Mail, Message
from app import app
from random import randint
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "santech1608@gmail.com",
    "MAIL_PASSWORD": "gtashrxhohrabkap"
}

app.config.update(mail_settings)
mail = Mail(app)


def send_mail(gmail):
    try:
        with app.app_context():
            otp = randint(100000, 999999)
            msg = Message(subject="OTP", sender=app.config.get("MAIL_USERNAME"), recipients=[gmail],
                          body="{}".format(otp))
            mail.send(msg)
        return True, otp
    except:
        return False, 0
