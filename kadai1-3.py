### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース

import csv

with open('source.csv', 'r') as f:
    dataReader = csv.reader(f)
    for row in dataReader:
      pass

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in row:
        print("{}が見つかりした".format(word))
    else:
        print("{}が見つかりませんでした".format(word))

if __name__ == "__main__":
    search()
