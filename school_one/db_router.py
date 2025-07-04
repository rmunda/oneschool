from .utils import get_current_school_db


class SchoolDBRouter:
    def db_for_read(self, model, **hints):
        db = get_current_school_db()
        return db if db else 'default'

    def db_for_write(self, model, **hints):
        db = get_current_school_db()
        return db if db else 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db1 = obj1._state.db
        db2 = obj2._state.db
        return db1 == db2

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # You can refine this if some apps are platform-wide
        return True
