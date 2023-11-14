from databricks_objs import DB_Catalog, DB_Ext_Loc, DB_Schema, DB_Table

class QueryGenerator:
    _supported_databricks_objects = [
        DB_Catalog, DB_Ext_Loc, 
        DB_Schema, DB_Table
    ]

    @classmethod
    def gen_create(cls, dc_object):
        for db_object in _supported_databricks_objects:
            if db_object.check(dc_object):
                db_object.gen_create(dc_object)

    @classmethod
    def gen_grant(cls, dc_object):
        for db_object in _supported_databricks_objects:
            if db_object.check(dc_object):
                db_object.gen_grant(dc_object)
    
    @classmethod
    def gen_revoke_grant(cls, dc_object):
        for db_object in _supported_databricks_objects:
            if db_object.check(dc_object):
                db_object.gen_revoke_grant(dc_object)

    @classmethod
    def gen_delete(cls, dc_object):
        for db_object in _supported_databricks_objects:
            if db_object.check(dc_object):
                db_object.gen_delete(dc_object)
