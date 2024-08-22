import scrapy
from scrapy.crawler import CrawlerProcess
import pickle

class TJAL(scrapy.Spider):
    name = 'TJAL'
    allowed_domains = ['www2.tjal.jus.br/cpopg/open.do']

    def __init__(self, numero_processo=None, *args, **kwargs):
        super(TJAL, self).__init__(*args, **kwargs)
        if numero_processo:
            self.start_urls = [
                f'https://esaj.tjce.jus.br/cpopg/show.do?processo.codigo=01Z081I9T0000&processo.foro=1&processo.numero={numero_processo}'
            ] 
        else:
            self.start_urls = []
        self.results = []
        self.numero_processo = numero_processo

    def parse(self, response):
        classe = response.css("#classeProcesso::text").extract_first()
        area = response.css("#areaProcesso span::text").extract_first()
        assunto = response.css("#assuntoProcesso::text").extract_first()
        data_distribuicao = response.css("#dataHoraDistribuicaoProcesso::text").extract_first()
        juiz = response.css("#juizProcesso::text").extract_first()
        valor_acao = response.css("#valorAcaoProcesso::text").extract_first()
        
        item = {
            'classe': classe,
            'area': area,
            'assunto': assunto,
            'data_distribuicao': data_distribuicao,
            'juiz':juiz,
            'valor_acao': valor_acao
        }
        self.results.append(item)

        for tr in response.css("#tableTodasPartes tr"):
            parte_e_advogado = tr.css("td.nomeParteEAdvogado::text").extract()
            parte_e_advogado = [text.strip() for text in parte_e_advogado if text.strip()]
            
            item= {'parte_e_advogado': parte_e_advogado }
            self.results.append(item)

        for tr in response.css("#tabelaTodasMovimentacoes tr"):
            data_movimentacao = tr.css("td.dataMovimentacao *::text").extract()
            data_movimentacao = [text.strip() for text in data_movimentacao if text.strip()]
            descricao_movimentacao = tr.css("td.descricaoMovimentacao *::text").extract()
            descricao_movimentacao = [text.strip() for text in descricao_movimentacao if text.strip()]
            
            item = {
                'data_movimentacao': data_movimentacao,
                'descricao_movimentacao': descricao_movimentacao
            }
            self.results.append(item)

        with open(f'data/tjal-{self.numero_processo}.pkl', 'wb') as f:
            pickle.dump(self.results, f)

def run_spider_tjal(numero_processo):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    
    process.crawl(TJAL, numero_processo=numero_processo)
    process.start()
    
