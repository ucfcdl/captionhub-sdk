import requests

from captionhub_sdk.caption import Caption
from captionhub_sdk.exceptions import CaptionNotFound

class Captionhub:
    def __init__(self, api_key, api_url):
        """
        Initialize the API.
        :param api_key: string
        :param api_url: string
        """
        self.api_key = api_key
        self.api_url = api_url

    def get_caption(self, video_id):
        """
        Get a caption for a video.
        :param video_id: string
        :return: Caption or False
        """
        url = self.api_url + 'videos/' + video_id
        headers = {'Authorization': 'Token ' + self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return []
        return Caption(response.json()['captions'][0])
            

    def upload_caption(self, file, video_id, language):
        """
        Upload a caption file to a video.
        :param file: file object (bytes)
        :param video_id: string
        :param language: string
        :return: response
        """
        url = self.api_url + 'captions/'
        files = [('file', file)]
        headers = {'Authorization': 'Token ' + self.api_key}
        data = {'video': video_id, 'language': language}
        return requests.post(url, data=data, headers=headers, files=files)
    

    def delete(self, id):
        """
        Delete a caption.
        :param id: string
        """
        url = self.api_url + 'videos/' + id
        headers = {'Authorization': 'Token ' + self.api_key}
        return requests.delete(url, headers=headers)
