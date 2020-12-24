class Comment(object):

    def __init__(self, medic_id=None, timestamp=None, content=None, data_tuple=None):
        self._id = None
        self._timestamp = timestamp
        self._content = content
        self._medic_id = medic_id
        if data_tuple:
            self.id, self.timestamp, self.content, self.medic_id = data_tuple

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id

    @property
    def medic_id(self):
        return self._medic_id

    @medic_id.setter
    def medic_id(self, value):
        self._medic_id = value

    @medic_id.deleter
    def medic_id(self):
        del self._medic_id

    @property
    def timestamp(self):
        """I'm the 'x' property."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @timestamp.deleter
    def timestamp(self):
        del self._timestamp

    @property
    def content(self):
        """I'm the 'x' property."""
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @content.deleter
    def content(self):
        del self._content

    def __repr__(self):
        return f'{self.id=}, {self.medic_id=}, {self.timestamp=}, {self.content=}'
