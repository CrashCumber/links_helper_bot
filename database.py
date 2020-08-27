import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Base


class SqlOrmConnection:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.connection = self.get_connection()

        session = sessionmaker(bind=self.connection.engine, autocommit=False)
        self.session = session()
        self.engine = self.connection.engine
        self.create_tables()

    def get_connection(self):
        engine = sqlalchemy.create_engine(
            'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(user=self.user,
                                                                          password=self.password,
                                                                          host=self.host,
                                                                          port=self.port,
                                                                          db=self.db_name)
        )

        return engine.connect()

    def create_tables(self):
        if not self.engine.dialect.has_table(self.engine, 'users'):
            Base.metadata.tables['users'].create(self.engine)

        if not self.engine.dialect.has_table(self.engine, 'links'):
            Base.metadata.tables['links'].create(self.engine)

    def execute_query(self, query):
        res = self.connection.execute(query)
        return res.getchall()
