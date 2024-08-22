from flask import Flask, jsonify
from multiprocessing import Process
from tjalCrawler import run_spider_tjal
from tjceCrawler import run_spider_tjce
import pickle

app = Flask(__name__)

def start_crawler(crawler_function, numero_processo):
    crawler_function(numero_processo)

@app.route('/buscar-processo/<string:tribunal>/<string:numero_processo>', methods=['GET'])
def search_number(tribunal, numero_processo):

    if not numero_processo:
        return jsonify({'error': 'É necessário fornecer o número do processo'}), 400
    
    if not tribunal:
        return jsonify({'error': 'É necessário fornecer o tribunal'}), 400

    if tribunal.lower() == 'tjal':
        with open(f'data/tjal-{numero_processo}.pkl', 'rb') as f:
            loaded_dict = pickle.load(f)
            return jsonify(loaded_dict)
    elif tribunal.lower() == 'tjce':
        pass
    else:
        return jsonify({'error': 'Tribunal não reconhecido'}), 400

    return jsonify({'status': f'Crawler do {tribunal.upper()} iniciado com sucesso'}), 200


@app.route('/rodar-crawler/<string:tribunal>/<string:numero_processo>', methods=['GET'])
def run_crawler(tribunal, numero_processo):

    if not numero_processo:
        return jsonify({'error': 'É necessário fornecer o número do processo'}), 400
    
    if not tribunal:
        return jsonify({'error': 'É necessário fornecer o tribunal'}), 400

    if tribunal.lower() == 'tjal':
        process = Process(target=start_crawler, args=(run_spider_tjal, numero_processo))
        process.start()
    elif tribunal.lower() == 'tjce':
        process = Process(target=start_crawler, args=(run_spider_tjce, numero_processo))
        process.start()
    else:
        return jsonify({'error': 'Tribunal não reconhecido'}), 400

    return jsonify({'status': f'Crawler do {tribunal.upper()} iniciado com sucesso'}), 200


if __name__ == '__main__':
    app.run(debug=True)
