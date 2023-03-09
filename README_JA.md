# CUE自動分割器です
[ENGLISH](https://github.com/itoukou1/CueAutoSplit/blob/main/README.md "ENGLISH")	[中文](https://github.com/itoukou1/CueAutoSplit/blob/main/README_CN.md "中文")	[日本语](https://github.com/itoukou1/CueAutoSplit/blob/main/README_JA.md "日本语")

## 機能
cueの迅速な分離(マルチフォルダー)場合によっては、cueを自動的にルックアップすることができます。タグと表紙(あれば)は分割後に自動的に追加されます。このライブラリは通常、いくつかのキュー(例えば日本のアニメシリーズの曲など)を分割するのに使われます。
## 取り付け方法です
https://sourceforge.net/projects/sox/files/sox/
soxをダウンロードして環境変数を設定します

cueを含むフォルダをコードディレクトリに入れます(cueをフォルダから取り出す必要はありません)。

(表紙を追加する場合は、画像ファイルを入れてください。プログラムが自働的に追加処理します。)

実行コードです
```python
python process.py
```

## 感谢
Sox
[Deflacue](https://github.com/idlesign/deflacu/ "Deflacue")
