from src.base_db_class import DB_Base

class DB_Schema(DB_Base):
    @staticmethod
    def check(schema_dc_object):
        """ Check if the dataclass object should be processed by this """
        pass

    @staticmethod
    def gen_create(schema_dc_object):
        """ Use this dataclass object to create this in databricks """
        pass

    @staticmethod
    def gen_grant(grants_dc_object):
        """ This generates grant statement for schema """
        pass

    @staticmethod
    def gen_revoke_grant(grants_dc_object):
        """ This generates revoke grant statement for schema """
        pass
    
    @staticmethod
    def gen_delete(schema_dc_object):
        """ delets this databricks object """
        pass


class DB_Catalog(DB_Base):
    @staticmethod
    def check(catalog_dc_object):
        """ Check if the dataclass object should be processed by this """
        pass

    @staticmethod
    def gen_create(catalog_dc_object):
        """ Use this dataclass object to create this in databricks """
        pass

    @staticmethod
    def gen_grant(grants_dc_object):
        """ This generates grant statement for catalog """
        pass

    @staticmethod
    def gen_revoke_grant(grants_dc_object):
        """ This generates revoke grant statement for schema """
        pass
    
    @staticmethod
    def gen_delete(schema_dc_object):
        """ delets this databricks object """
        pass


class DB_Table(DB_Base):
    @staticmethod
    def check(table_dc_object):
        """ Check if the dataclass object should be processed by this """
        pass

    @staticmethod
    def gen_create(table_dc_object):
        """ Use this dataclass object to create this in databricks """
        pass

    @staticmethod
    def gen_grant(grants_dc_object):
        """ This generates grant statement for table """
        pass

    @staticmethod
    def gen_revoke_grant(grants_dc_object):
        """ This generates revoke grant statement for schema """
        pass
    
    @staticmethod
    def gen_delete(schema_dc_object):
        """ delets this databricks object """
        pass


class DB_Ext_Loc(DB_Base):
    @staticmethod
    def check(ext_loc_dc_object):
        """ Check if the dataclass object should be processed by this """
        pass

    @staticmethod
    def gen_create(ext_loc_dc_object):
        """ Use this dataclass object to create this in databricks """
        pass

    @staticmethod
    def gen_grant(grants_dc_object):
        """ This generates grant statement for ext_loc """
        pass

    @staticmethod
    def gen_revoke_grant(grants_dc_object):
        """ This generates revoke grant statement for schema """
        pass
    
    @staticmethod
    def gen_delete(schema_dc_object):
        """ delets this databricks object """
        pass