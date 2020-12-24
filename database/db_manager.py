from database.db_util import Singleton
from database.table.category_table import CategoryTable
from database.table.comment_table import CommentTable
from database.table.favourite_table import FavouriteTable
from database.table.medic_table import MedicTable
from database.table.patient_table import PatientTable


class DatabaseManager(metaclass=Singleton):
    medic_table: MedicTable
    favourite_table: FavouriteTable
    comment_table: CommentTable
    category_table: CategoryTable
    patient_table: PatientTable

    def __init__(self):
        self.medic_table = MedicTable()
        self.favourite_table = FavouriteTable()
        self.comment_table = CommentTable()
        self.category_table = CategoryTable()
        self.patient_table = PatientTable()

    def get_by_table_name(self, table_name):
        for table in vars(self).values():
            if table.table_name == table_name:
                return table
    # @staticmethod
    # def get_medic_table() -> MedicTable:
    #     return MedicTable()
    #
    # @staticmethod
    # def () -> FavouriteTable:
    #     return CameraResolutionTable()
    #
    # @staticmethod
    # def get_camera_table() -> CameraTable:
    #     return CameraTable()
    #
    # @staticmethod
    # def get_codec_table() -> CodecTable:
    #     return CodecTable()
    #
    # @staticmethod
    # def get_resolution_table() -> ResolutionTable:
    #     return ResolutionTable()
