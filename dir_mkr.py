"""Modulo para creacion de directorios en directorio parent
    Formato:

    -> Parent dir
        -> Year
            -> Month
                -> date: DD-MM-YYYY
                    -> File: YYYYMMDD_HHMMSS_sss
    request build dir, ignore excepcion if dir exits
    The requested dir is componded by year, month and dir date format
            
"""

import os
import config
import datetime as dt


def run_program():
    """Funcion para debugging, ejecucion independiente"""

    build_dir()

    return None


def user_date_input(req_date) -> list:
    """Funcion para captura de fecha por usuario para crear direcotio"""

    custom_format = "%Y%m%d"
    if req_date:
        user_date = req_date
    else:
        user_date = input("Ingrese fecha formato YYYY-MM-DD: ")

    try:
        date = dt.datetime.strptime(user_date, custom_format)
    except ValueError as err:
        print(f"Fecha invalida {err}")

    date_list = get_date_list(date)

    return date_list


def get_date_list(date: dt.datetime) -> list:
    """Return a list with names for build parent and child direcoties"""

    month_names = {1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
                   7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"}

    year = date.strftime("%Y")
    month_int = int(date.strftime("%m"))
    month = month_names[month_int]
    child = date.strftime("%Y-%m-%d")

    return [year, month, child]


def build_dir(date="", today=True):
    """Construccion de directorios, formato, year, month, format date dir (DD-MM-YYYY)
        for call function with today False, need to pass date string in format DD-MM-YYYY
    """
    if today:
        date = dt.datetime.today()
        control_dir = get_date_list(date)
    else:
        control_dir = user_date_input(date)
    print(control_dir)

    parent_dir = config.parent_dir()

    aux_path = "\\".join(control_dir)

    to_build = os.path.join(parent_dir, aux_path)

    if os.path.exists(to_build):
        print(f"Directorio existente {to_build}")
    else:
        os.makedirs(to_build, exist_ok=True)
        if os.path.isdir(to_build):
            print(f"Direcotrio creado EXITOSAMENTE en {to_build}")
        else:
            print("Fallo en crear direcotrio contacte al admin")


if __name__ == "__main__":

    run_program()
