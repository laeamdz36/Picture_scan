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
import dir_mkr as dkr
import net_picture as net_p
import functools


def program_info(func):
    """decorator for main ejecicion of program"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_msg = "Comienzo de ejecucion de programa"
        end_msg = "Finaliazcion de ejecucion de programa"
        print(start_msg.center(100, "*"))
        result = func(*args, **kwargs)
        print(end_msg.center(100, "*"))
        return result
    return wrapper


def print_scan_result(data: dict) -> None:
    """Funcion para impresion de resultado de escaneo
        IP - mac address
    """

    user_input = input("Impresion de resultados? (Y/N): ")

    if user_input.lower() == "y":
        for cam in data["cameras"]:
            print(f'{cam} -> {data["cameras"][cam]["ip"]}')
    else:
        print("NO se imprimieron resultados")

    return None


@program_info
def run_program():
    """Lazo de ejecucion principal"""

    # run network scan to found the current ip for registered devices
    data = net_s.scan_network()
    print_scan_result(data)

    # build directry for today and assign to a variable
    path_job = dkr.build_dir()

    net_p.get_pictures(path=path_job, data=data)

    return None


if __name__ == "__main__":

    run_program()
