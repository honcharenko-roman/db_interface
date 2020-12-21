class Medic(object):

    def __init__(self, medic_id=None, timestamp=None, content=None):
        self._id = None
        self._first_name = medic_id
        self._last_name = timestamp
        self._phone = content
        self._email = content
        self._category_id = content

    @property
    def id(self):
        return self._id

    @id.deleter
    def id(self):
        del self._id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        del self._first_name

    @property
    def last_name(self):
        """I'm the 'x' property."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @last_name.deleter
    def last_name(self):
        del self._last_name

    @property
    def phone(self):
        """I'm the 'x' property."""
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @phone.deleter
    def phone(self):
        del self._phone

    @property
    def email(self):
        """I'm the 'x' property."""
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email

    @property
    def category_id(self):
        """I'm the 'x' property."""
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value

    @category_id.deleter
    def category_id(self):
        del self._category_id

    def __repr__(self):
        return f'{self.id=}, {self.first_name=}, {self.last_name=}, {self.phone=},  {self.email=},  {self.category_id=}'

    def data(self):
        return self._first_name, self.last_name, self.phone, self.email

    def update(self, data):
        _, self.medic_id, self.timestamp, self.content = data
