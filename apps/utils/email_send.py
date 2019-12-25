from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from sms.settings import EMAIL_FROM


def random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)

    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = '注册激活连接'
        email_body = f'请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{code}'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    if send_type == 'forget':
        email_title = '找回密码'
        email_body = f'请点击下面的链接找回你的密码：http://127.0.0.1:8000/reset/{code}'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    if send_type == "update_email":
        email_title = '修改邮箱'
        email_body = f'你的邮箱验证码为{code}'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
