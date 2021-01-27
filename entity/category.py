class Category(object):

    def __init__(self, name=None, data_tuple=None):
        self._id = None
        self._name = name
        if data_tuple:
            self.id, self.name = data_tuple

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    def __repr__(self):
        return f'{self.id=}, {self.name=}'
