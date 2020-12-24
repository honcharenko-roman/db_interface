from database.db_util import Singleton, execute_statement
from database.table.medic_table import MedicTable
from database.table.table import Table
from entity.comment import Comment


class CommentTable(Table, metaclass=Singleton):
    table_name: str = 'Comment'
    id_field_name: str = 'id'
    timestamp_field_name = 'timestamp'
    content_field_name: str = 'content'
    medic_id_field_name: str = 'medic_id'

    def __init__(self):
        super().__init__(CommentTable.table_name)
        execute_statement(
            f'''CREATE TABLE if not exists {CommentTable.table_name} (
                {CommentTable.id_field_name} INTEGER PRIMARY KEY AUTOINCREMENT,
                {CommentTable.timestamp_field_name} timestamp,
                {CommentTable.content_field_name} TEXT,
                {CommentTable.medic_id_field_name} INTEGER
                     REFERENCES {MedicTable.table_name} ({MedicTable.id_field_name})
            )'''
        )

    @staticmethod
    def insert(comment: Comment):
        execute_statement(
            f'''INSERT INTO {CommentTable.table_name} 
                ({CommentTable.medic_id_field_name}, 
                {CommentTable.timestamp_field_name},
                {CommentTable.content_field_name}) 
                VALUES (?,?,?)''',
            (comment.medic_id, comment.timestamp, comment.content)
        )

    def get_all(self):
        comments = []
        for comment in super().get_all():
            comments.append(Comment(data_tuple=comment))
        return comments
