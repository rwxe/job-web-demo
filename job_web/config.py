import os
from flask_uploads import IMAGES


class BaseConfig(object):
    SECRET_KEY = '123456'
    JOB_INDEX_PER_PAGE = 18
    COMPANY_INDEX_PER_PAGE = 20
    COMPANY_DETAIL_PER_PAGE = 10
    LIST_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # mysql://username:password@server_name/db_name
    # 项目的mysql用户为jw，密码jw
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://jw:jw@localhost:3306/job_web?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_SIZE = 300 * 1024
    UPLOADED_RESUME_ALLOW = IMAGES
    UPLOADED_RESUME_DEST = os.path.join(os.getcwd(), 'static', 'resume')
    UPLOADED_LOGO_ALLOW = IMAGES
    UPLOADED_LOGO_DEST = os.path.join(os.getcwd(), 'static', 'logo')


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


