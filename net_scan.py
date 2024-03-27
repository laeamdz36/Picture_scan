"""Modulo para el escaneo de red"""

import nmap
import config
# import config to get all parameters to obtain ip by mac


def scan_config() -> dict:
    """parametros de configuracion para escaneo"""

    ip_range = "192.168.0.1/24"
    args = "-sP"
    scan_cfg = {"ip_range": ip_range, "args": args}

    return scan_cfg


def scan_network():
    """Escaneo de red, obtencion de ip de hosts"""

    # load main configuration of devices to scanned
    data = config.main_config()

    # load configuraction for scanning
    scan_args = scan_config()

    # * Escaneo de puerto con parametros de coniguración
    nm = nmap.PortScanner()
    nm.scan(scan_args["ip_range"], arguments=scan_args["args"])

    for host in nm.all_hosts():

        if "mac" in nm[host]["addresses"]:

            # Construccion de mac de host en iteracion
            mac = nm[host]["addresses"]["mac"]
            for cams in data["cameras"]:
                # * Busquda y almacenamiento de las direcciones ip buscadas por mac
                if data["cameras"][cams]["mac"] == mac:
                    data["cameras"][cams]["ip"] = nm[host]["addresses"]["ipv4"]

    # retorno de diccionario con info de ip agregadas
    return data


def run_program():
    """Testing program fnuction"""

    result = scan_network()

    return result


# * Ejecucion de programa idependiente
if __name__ == "__main__":
    # ejecucion del programa de forma independiente

    info_get = run_program()

    for cam in info_get["cameras"]:
        print(f'{cam} -> {info_get["cameras"][cam]["ip"]}')
