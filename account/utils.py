import os

class Util:
  @staticmethod
  def send_email(data):
    """
    Это всего-лишь функция-затычка. Поднимать тут же ещё и SMTP-сервер я не планирую =)
    """
    print(f"Email sent to {data['to_email']} with message: {data['body']}")