from sqlalchemy import create_engine


class Config:
    SECRET_KEY = 'luis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@127.0.0.1:3306/tiendadb"


config = {
    'dev': DevelopmentConfig
}
