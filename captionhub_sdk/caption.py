class Caption:
    def __init__(self, response):
        self.id = response['id']
        self.language = response['language']
        self.file =  response['file']
        self.updated_at = response['updated_at']
