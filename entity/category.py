class Category(object):

    def __init__(self, medic_id=None):
        self._id = None
        self._name = medic_id

    @property
    def id(self):
        return self._id

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
