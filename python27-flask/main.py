#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

networkJson = urlfetch.fetch("https://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
# / のリクエスト（例えば http://localhost:8080/ ）をこの関数で処理する。
# ここでメニューを表示をしているだけです。
def root():
  return render_template('hello.html')

@app.route('/pata')
# /pata のリクエスト（例えば http://localhost:8080/pata ）をこの関数で処理する。
# これをパタトクカシーーを処理するようにしています。
def pata():
  # とりあえずAとBをつなぐだけで返事を作っていますけど、パタタコカシーーになるように自分で直してください！
  a = request.args.get('a', '')
  b = request.args.get('b', '')
  pata = ""
  i = 0 # Overall iterator
  j = 0 # a string iterator
  k = 0 # b string iterator
  while i < (len(a) + len(b)):
    if j > len(b) and j < len(a):
      pata += a[j]
      i += 1
      j += 1
    elif k >= len(a) and k < len(b):
      pata += b[k]
      i += 1
      k += 1
    elif i % 2 == 0:
      pata += a[j]
      i += 1
      j += 1
    else:
      pata += b[k]
      i += 1
      k += 1
  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata=pata)

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。
def norikae(self):
  return render_template('norikae.html', network=network)
