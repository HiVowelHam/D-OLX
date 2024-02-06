import date
from user.py import usuario.id

class produto:
    def __init__ (self, nome: str, descriçao: str, add_since: date.today, estado_uso: bool = True, region: str, _quantidade: int):
        self.nome = nome;
        self.descriçao = descriçao;
        self.add_since = add_since;
        self.usuario_id = usuario.id
        