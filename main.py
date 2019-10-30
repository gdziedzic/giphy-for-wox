from wox import Wox
import subprocess
import requests
import time
import giphy_client
from giphy_client.rest import ApiException
import pyperclip
import os
import json

class Giphy(Wox):
    def query(self, query):
        results = []

        if len(query) < 3 or query[-1] != "/":
            results.append({
                "Title": 'No results',
                "SubTitle": '',
                "IcoPath":"icons/empty.png"
            })
            return results

        phrase = query.replace("/","")

        api = giphy_client.DefaultApi()
        api_key = 'dc6zaTOxFJmzC'

        try:
            translate_result = api.gifs_translate_get(api_key, phrase)
            url_original = translate_result.data.images.original.url
            url_prev = translate_result.data.images.fixed_height.url

            timestr = time.strftime("%Y%m%d-%H%M%S")
            file_name = f"{timestr}.gif"

            response = requests.get(url_prev)

            gifs_location = "c:\\temp"
            if not os.path.exists(gifs_location):
                os.makedirs(gifs_location)
            local_path = f"{gifs_location}\\{file_name}"

            if response.status_code == 200:
                with open(local_path, 'wb') as gif_file:
                    gif_file.write(response.content)

            pyperclip.copy(url_original)

            results.append({
                    "Title": str(url_original),
                    "SubTitle": phrase,
                    "IcoPath":local_path,
                    "JsonRPCAction":{'method': 'open_gif', 'parameters': [local_path], 'dontHideAfterAction': False}
            })
        except Exception as e:
            results.append({
                "Title": 'Issue when getting gif',
                "SubTitle": str(e),
                "IcoPath":"icons/error.png"
            })

        return results

    def open_gif(self, gif_path):
        config_file_name = "config.json"
        with open(os.path.join(os.path.dirname(__file__), config_file_name), "r") as config_file:
            config = json.loads(config_file.read())
        quick_look_path = os.path.expandvars(config["quick_look_path"])
        subprocess.call(f"{quick_look_path} {gif_path}")

if __name__ == "__main__":
    Giphy()