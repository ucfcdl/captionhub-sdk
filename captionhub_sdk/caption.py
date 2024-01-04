#'captions': [{'id': 3, 'language': 'en', 'file': 'https://taher-captionhub.s3.amazonaws.com/captions/ece34719-b329-4b9a-95eb-2eea8cb8eedf.srt?AWSAccessKeyId=AKIATIU5EOTJUCVOHT3W&Signature=xSwXuugYcODI48Mp0dT0I0Fsos8%3D&Expires=1704393930', 'updated_at': '2024-01-04T17:31:49.319885Z'}

class Caption:
    def __init__(self, response):
        self.id = response['id']
        self.language = response['language']
        self.file =  response['file']
        self.updated_at = response['updated_at']
