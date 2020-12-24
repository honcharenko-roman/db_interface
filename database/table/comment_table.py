from database.db_util import Singleton, execute_statement
from database.table.medic_table import MedicTable
from database.table.table import Table
from entity.comment import Comment


class CommentTable(Table, metaclass=Singleton):
    table_name: str = 'Comment'
    _id_field_name: str = 'id'
    medic_id_field_name: str = 'medic_id'
    _timestamp_field_name = 'date'
    _content_field_name: str = 'content'

    def __init__(self):
        super().__init__(CommentTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {CommentTable.table_name} (
                {CommentTable._id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {CommentTable._timestamp_field_name} timestamp,
                {CommentTable._content_field_name} TEXT,
                {CommentTable.medic_id_field_name} INTEGER
                     REFERENCES {MedicTable.table_name} ({MedicTable.id_field_name})
            )'''
        )

    @staticmethod
    def insert(comment: Comment):
        execute_statement(
            f'''INSERT INTO {CommentTable.table_name} 
                ({CommentTable.medic_id_field_name}, 
                {CommentTable._timestamp_field_name},
                {CommentTable._content_field_name}) 
                VALUES (?,?,?)''',
            (comment.medic_id, comment.timestamp, comment.content)
        )

    @staticmethod
    def drop_table():
        execute_statement(
            f'DROP TABLE if exists {CommentTable.table_name}'
        )

    @staticmethod
    def get_all():
        return execute_statement(
            f'SELECT * FROM {CommentTable.table_name}',
        ) or []
