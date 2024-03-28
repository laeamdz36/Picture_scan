"""Modulo para lectura y almaceamiento de imagenes desde las camaras ip"""

from pathlib import Path
import datetime as dt
import time
import cv2
import os


def build_url(data):
    """Modulo para contrsuccion de url de conexion
        Construction of url to get pircture from camera
        url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"
        url_480p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
    """
    urls = {}
    PORT = 554
    for cam in data["cameras"]:
        # * url_1080p
        result_urls = f'rtsp://{data["cameras"][cam]["user"]}:{data["cameras"][cam]["psw"]}@{data["cameras"][cam]["ip"]}:{PORT}/stream1'
        urls[cam] = result_urls
    return urls


def build_file_name(cam):
    """Build file name base in time stamp, format YYYYMMDD_HHMMSS_sss.png"""

    today = dt.datetime.today()

    file_name = today.strftime("%Y%m%d_%H%M%S%f")

    return file_name[:-3] + "_" + cam


def build_storage_dir(parent_path="", data=""):
    """Build storage build for each camera"""

    dict_paths = {}
    print(f"PATH SELECTED -> {parent_path}")

    for cam in data["cameras"]:

        aux_path = os.path.join(parent_path, cam)
        print(aux_path)
        os.makedirs(aux_path, exist_ok=True)
        aux_path = os.path.join(aux_path, build_file_name(cam))
        print(aux_path)
        time.sleep(0.8)
        dict_paths[cam] = aux_path

    return dict_paths


def shoot_snap(cam, urls, paths):
    """Modulo para toma de framde  capara ip"""
    cam_name_file = paths[cam] + ".png"
    print(cam_name_file)
    cap = cv2.VideoCapture(urls[cam])
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(cam_name_file, frame)
    cap.release()
    time.sleep(2)

    return None


def take_pictures(paths, data):
    """Main execution for take picture from ip camera"""

    for cam in data["cameras"]:
        print(f'{cam} -> {data["cameras"][cam]["ip"]}')
        print(f"Camara -> {cam} - {paths}")

    urls = build_url(data)

    for cam in data["cameras"]:

        shoot_snap(cam, urls, paths)
        time.sleep(1.5)

    return


def get_pictures(path="", data=""):
    """Obtiene imagenes de las camaras contenidas en el parametro data"""

    paths = build_storage_dir(path, data)

    for path_dir in paths.values():
        print(path_dir)
    take_pictures(paths, data)

    return None


def run_main():
    """Main program execution"""
    get_pictures(path="", data="")
    print(f"{__name__} func -> {run_main.__name__}execution")


if __name__ == "__main__":

    print("Carga de modulo exitosa...")
    run_main()
