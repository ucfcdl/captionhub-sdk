class CaptionNotFound(Exception):
    def __init__(self):
        self.message = "Caption not found"
