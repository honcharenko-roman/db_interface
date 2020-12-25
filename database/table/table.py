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
