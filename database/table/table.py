from database.db_util import execute_statement


class Table:
    table_name: str

    def __init__(self, table_name):
        self.table_name = table_name
        self.id_field_name = 'id'

    def drop_table(self):
        execute_statement(
            f'DROP TABLE if exists {self.table_name}'
        )

    def get_all(self):
        return execute_statement(
            f'SELECT * FROM {self.table_name}',
        ) or []

    def get_column_values(self, column):
        return execute_statement(
            f'SELECT ({column}) FROM {self.table_name}',
        ) or []

    def get_dataset(self):
        data = {}

        for item in self.get_all():
            for key in vars(item).keys():
                data[key[1:]] = self.get_column_values(key[1:])

        return data

    def remove_by_id(self, id_to_delete):
        execute_statement(
            f'DELETE FROM {self.table_name} WHERE {self.id_field_name}=?',
            (id_to_delete,)
        )

    def get_fields(self):
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        members.remove('table_name')
        _list = []
        # return [eval(f'self.{member}') for member in members]
        for member in members:
            _list.append(eval(f'self.{member}'))
        return _list

    def insert_dict(self, name_qline_dict):
        request = ''
        request += f'INSERT INTO {self.table_name}('
        for key, value in name_qline_dict.items():
            request += f'{key},'
        request = request[:-1] + ') VALUES (' + ('?,' * len(name_qline_dict.keys()))
        request = request[:-1] + ')'
        execute_statement(
            request,
            tuple([value.text() for value in name_qline_dict.values()])
        )
