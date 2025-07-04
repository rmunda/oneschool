from threading import local

_thread_local = local()


def set_current_school_db(db_alias):
    _thread_local.school_db = db_alias


def get_current_school_db():
    return getattr(_thread_local, 'school_db', None)


def clear_current_school_db():
    if hasattr(_thread_local, 'school_db'):
        del _thread_local.school_db
