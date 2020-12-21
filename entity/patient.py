class Patient(object):

    def __init__(self, first_name=None, last_name=None, phone=None, email=None, medic_id=None):
        self._id = None
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        self._medic_id = medic_id

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
    def medic_id(self):
        """I'm the 'x' property."""
        return self._medic_id

    @medic_id.setter
    def medic_id(self, value):
        self._medic_id = value

    @medic_id.deleter
    def medic_id(self):
        del self._medic_id

    def __repr__(self):
        return f'{self.id=}, {self.first_name=}, {self.last_name=}, {self.phone=},  {self.email=},  {self.medic_id=}'
