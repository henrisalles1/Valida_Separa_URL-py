import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL não é valida')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URL não é valida')

    def get_url_base(self):
        index_interrogacao = self.url.find('?')
        url_base = self.url[:index_interrogacao]
        return url_base

    def get_url_parametros(self):
        index_parametros = self.url.find('?')
        url_parametros = self.url[index_parametros:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        index_parametro = self.get_url_parametros().find(parametro_busca)
        index_valor = index_parametro + len(parametro_busca) + 1
        index_e_comercial = self.get_url_parametros().find('&',index_valor)
        if index_e_comercial == -1:
            valor = self.get_url_parametros()[index_valor:]
            return valor
        else:
            valor = self.get_url_parametros()[index_valor:index_e_comercial]
            return valor

extrator_url = ExtratorURL('http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100')