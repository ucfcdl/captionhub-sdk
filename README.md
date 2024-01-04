# README

## Project Overview

This project is a Python API client for Captionhub. It allows you to interact with the Captionhub's API to get, upload, and delete video captions.

### Methods

- `__init__(api_key, api_url)`: Initializes the API client with the provided API key and URL.

- `get_caption(video_id)`: Fetches the caption for a given youtube video using its youtube ID. If the caption does not exist, it returns False.

- `upload_caption(file, video_id, language)`: Uploads a caption file to a video. The file should be a bytes-like object, the youtube video ID should be a string, and the language should be a string representing the language of the caption.

- `delete(id)`: Deletes a caption given its ID.

### Usage

1. Initialize the api using ```captionhub = Captionhub(api_key, api_url)```
2. Use any of the methods described above. For example: ```captionhub.get_caption(video_id)``


### Dependencies

This project uses the following packages:
- requests
