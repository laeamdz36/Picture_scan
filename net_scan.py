"""Modulo para el escaneo de red"""

import nmap
import config as cfg


def read_config() -> dict:
    """Read config file o obtain camera parameters to get ip address"""

    parameters = cfg.main_config()

    return parameters


def scan_network():
    """Escaneo de red, obtencion de hosts"""
