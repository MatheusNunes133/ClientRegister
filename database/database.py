from peewee import *

from classes.Client import Client
from utils.load_env import *

class ConnectDatabase:
    def __init__(self):
        self._connect = PostgresqlDatabase(database_name, user=username, password=password, host=host, port=port)

    def create_table(self):
        try:
            self._connect.connect()
            self._connect.create_tables([Client], safe=True)
            print("Tabela Criada")
        except Exception as e:
            print(f"Falha ao Criar Tabela: {e}")
        finally:
            self.close_connection()

    def check_table_exists(self):
        try:
            self._connect.connect()
            return self._connect.table_exists(Client)
        except Exception as e:
            print(f"Erro ao verificar tabela: {e}")
        finally:
            self.close_connection()

    def save(self, name, lastname, age, email, phone):
        try:
            self._connect.connect()
            new_client = Client.create(name=name, lastname=lastname, age=age, email=email, phone=phone)
            self.close_connection()
            return new_client
        except Exception as e:
            print(f"Não foi possivel salvar usuário: {e}")

    def get_all_clients(self):
        try:
            self._connect.connect()
            return Client.select()
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
        finally:
            self.close_connection()

    def close_connection(self):
        self._connect.commit()
        self._connect.close()
