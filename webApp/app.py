import json
from flask import Flask, request, render_template, session
import random
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

orderable_sushis = ['マグロ', 'イカ', 'エビ', 'イクラ', 'ウニ', 'たまご']

money_sushis = {
    'マグロ': '300',
    'イカ': '150',
    'エビ': '200',
    'イクラ': '400',
    'ウニ': '500',
    'たまご': '100'
}

sushis = ['マグロ', 'イカ', 'エビ', 'イクラ', 'ウニ', 'たまご', 'ゴミ']
fish_images = {
    'マグロ': 'maguro.png',
    'イカ': 'ika.png',
    'エビ': 'ebi.png',
    'イクラ': 'ikura.png',
    'ウニ': 'uni.png',
    'たまご': 'tamago.png',
    'ゴミ': 'gomi.png'
}

@app.route('/')
def order():
    total_price = session.get('total_price', 0)
    total_bait = session.get('total_bait', 0)
    
    # Pythonのリストや辞書をJSON形式に変換
    fishable_sushis_json = json.dumps(sushis)
    fishable_sushis_img_json = json.dumps(fish_images)

    return render_template('order.html',
                           money_sushis=money_sushis, 
                           orderable_sushis=orderable_sushis, 
                           total_price=total_price, 
                           total_bait=total_bait, 
                           fish_images=fish_images, 
                           sushis=sushis,
                           fishable_sushis_json=fishable_sushis_json, 
                           fishable_sushis_img_json=fishable_sushis_img_json)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='127.0.0.1', port=5000, threads=8)