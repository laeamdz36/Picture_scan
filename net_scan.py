"""Modulo para el escaneo de red"""

import nmap
# import config as cfg


def read_config() -> dict:
    """Read config file o obtain camera parameters to get ip address"""

    parameters = cfg.main_config()

    return parameters


def scan_network():
    """Escaneo de red, obtencion de hosts"""

    # Local configurations
    ip_range = "192.168.0.1/24"
    pars = "-sP"

    nm = nmap.PortScanner()
    nm.scan(ip_range, arguments=pars)

    for host in nm.all_hosts():
        if "mac" in nm[host]["addresses"]:
            print(f"{host} - {nm[host]['addresses']['mac']}")


def run_program():
    """Testing program fnuction"""

    scan_network()


if __name__ == "__main__":

    import config

    pars = config.main_config()
    run_program()
