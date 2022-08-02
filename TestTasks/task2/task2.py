import os
import pathlib
from os.path import exists

import requests
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip

"""
Use this tutorial to download and save video from url using ticktok api.
https://blog.devgenius.io/tiktok-api-python-41d76c67a833
"""


def get_video_file_request(url: str, data_dir="data\\") -> str:
    """
    Download and save video from url.
    ------------------------------------
    Reference: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    ------------------------------------
    :param data_dir: path to data directory.
    :param url: url link to file.
    :return: string filename.
    """
    filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f"{data_dir}filename", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return filename


def get_video_file_api(url: str, data_dir="\\data\\") -> str:
    """
    Download and save video from url using ticktok api.
    :param filename: future name of downloaded file.
    :param data_dir: path to data directory.
    :param url: url link to file.
    :return: string filename.
    """
    querystring = {"link": url}

    headers = {
        "X-RapidAPI-Key": "f5032be1edmsh4da139506ac126ep18d4d0jsnace06501ea56",
        "X-RapidAPI-Host": "tiktok-info.p.rapidapi.com"
    }

    api = "https://tiktok-info.p.rapidapi.com/dl/"
    response = requests.request("GET", api, headers=headers, params=querystring)
    if response.status_code == 200:
        download_url: str = response.json()['videoLinks']['download']
        try:
            video_bytes = requests.get(download_url, headers={"User-Agent": "okhttp"}).content
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        cur = str(pathlib.Path(__file__).parent.resolve())
        path_to_video = cur + data_dir + download_url.split("-")[-1]
        with open(path_to_video, "wb") as f:
            f.write(video_bytes)
        return os.path.abspath(path_to_video)
    else:
        print("An error occurred, bad link.")
        return ""


def convert_to_gif(path_to_file: str, filename: str) -> str:
    """
    Convert given video to gif.
    :param filename: new name of gif file
    :param path_to_file: path to video file
    :return: path to gif video
    """
    cur = str(pathlib.Path(__file__).parent.resolve())
    path_to_gif = cur + f"\\gifs\\{filename}.gif"
    video = VideoFileClip(path_to_file)
    video.write_gif(path_to_gif)
    return os.path.abspath(path_to_gif)


if __name__ == "__main__":
    link = "https://www.tiktok.com/@sidemen/video/6818257229477645573"
    file_path = get_video_file_api(link)
    print(exists(file_path))
    file_path = convert_to_gif(file_path, file_path.split('\\')[-1])
    print(exists(file_path))
