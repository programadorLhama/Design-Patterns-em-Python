from observer import UserEmail
from sujeito import EmailHandler

observer1 = UserEmail("email1@email.com", "Clodoaldo")
observer2 = UserEmail("cleiton@email.com", "Cleiton")
observer3 = UserEmail("josivaldo@email.com", "Josivaldo")
observer4 = UserEmail("arlindo@email.com", "Arlindo")

email_handler = EmailHandler()
email_handler.add_observer(observer1)
email_handler.add_observer(observer2)
email_handler.add_observer(observer3)
email_handler.add_observer(observer4)

msg = ""
email_handler.send_email(msg)
