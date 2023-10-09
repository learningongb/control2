import uuid
from datetime import datetime

class note:

    def __init__(self, caption, text) -> None:
        self.uuid = uuid.uuid4().hex
        self.caption = caption
        self.text = text
        self.modified = datetime.now()

    def update(self, caption = None, text = None) -> None:
        if caption:
            self.caption = caption
        if text:
            self.text = text
        self.modified = datetime.now()

    
    