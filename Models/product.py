import date
from /Models/user.py import usuario.id

class produto:
    def __init__ (self, nome: str, descriçao: str, add_since: date.today, estado_uso: bool = True, region: str, _quantidade: int):
        self.nome = nome;
        self.descriçao = descriçao;
        self.add_since = add_since;
        self.usuario_id = usuario.id
        self.estado_uso = estado_uso;
        self.region = region;
        self._quantidade = _quantidade;
        self.compras = compras;
        self.avaliaçoes = avaliaçoes;
        self.comentarios = comentarios
