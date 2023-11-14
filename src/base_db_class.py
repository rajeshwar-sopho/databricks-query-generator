from abc import ABC, abstractmethod

class DB_Base(ABC):
    @staticmethod
    @abstractmethod
    def check(dc_object):
        pass

    @staticmethod
    @abstractmethod
    def gen_create(dc_object):
        pass

    @staticmethod
    @abstractmethod
    def gen_grant(dc_object):
        pass

    @staticmethod
    @abstractmethod
    def gen_revoke_grant(dc_object):
        pass

    @staticmethod
    @abstractmethod
    def gen_delete(dc_object):
        pass