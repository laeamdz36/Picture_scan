"""Modulo para gestion para el envi de coreo electronico de notificacion"""

from email.message import EmailMessage
import ssl
import smtplib


def email_params() -> dict:
    """Configuracion de parametros para enio de email"""

    pws = "polqnpilozmwnrcw"
    origin_email = "luis3mendez6@gmail.com"

    email = {"pass": pws, "email": origin_email}

    return email