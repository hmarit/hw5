#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import urlfetch

networkJson = urlfetch.fetch("http://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
def pata():
  # とりあえずpataを簡単な操作で設定するけど、少し工夫すればパタトクカシーーができます。
  pata = request.args.get('x', '') + request.args.get('y', '')
  return render_template('pata.html', pata=pata)

app = Flask(__name__)
@app.route('/norikae')
def norikae():
  return render_template('norikae.html', network)
