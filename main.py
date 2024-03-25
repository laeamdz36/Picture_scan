"""Modulo principal para toma de snapwhoots de camaras de red

    # 1. Scan network for requiered mac address and return the ruquested IP
    # Get and storage current ip address for required mac address
    # Execute routine to get image from required ip address
    # Storage images with timestamps named format and also name insert into tiny DB
    # build email object with attachment, content sent the local hour format
    # Send email to reciver
    # 

"""

from email.message import EmailMessage
from tinydb import TinyDB, Query
import datetime as dt
import ssl
import smtplib
import nmap
import net_scan as net_s


def config():
    """funcion de cofiguracion"""

    return None


def run_program():
    """Lazo de ejecucion principal"""
    config()
    cameras = net_s.get_cameras()
    for cam in cameras:
        print(f"{cam}")
    return None


if __name__ == "__main__":

    run_program()
    print("Fin de programa")
