"""Modulo para lectura y almaceamiento de imagenes desde las camaras ip"""

import cv2


def build_url(camera, ip):
    """Modulo para contrsuccion de url de conexion
        Construction of url to get pircture from camera
        url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"
        url_480p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
    """
    PORT = 554
    # * url_1080p
    result_url = f"rtsp://{camera[camera]['user']}:{camera[camera]['psw']}@{ip}:{PORT}/stream1"
    return result_url

    return None


def get_cameras():
    """Retorna las credenciales de las camaras registradas para ser monitoreadas"""

    return None


def run_main():
    """Main program execution"""

    print(f"{__name__} func -> {run_main.__name__}execution")


if __name__ == "__main__":

    print("Carga de modulo exitosa...")
    run_main()
