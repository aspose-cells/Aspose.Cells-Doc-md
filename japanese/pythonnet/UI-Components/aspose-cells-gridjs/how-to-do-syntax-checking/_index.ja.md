---
title: GridJsの構文チェックとスペル修正のためのシンタックスチェッキング＆スペルコレクション  
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/how-to-do-syntax-checking/
description: この記事は、GridJsに構文チェックとスペル修正を追加する方法について説明しています。
keywords: GridJs,構文チェック,スペル修正,構文,スペル,文法チェッカー,文法
aliases:
  - /python-net/aspose-cells-gridjs/syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-syntax-checking/
  - /python-net/aspose-cells-gridjs/how-to-add-spell-correction/
  - /python-net/aspose-cells-gridjs/spell-correction/
---


# ユーザー入力に対して構文チェック＆スペル修正を行う手順は次のとおりです
## ロードオプションを設定する。
たとえば：
```javascript
 const option = {
     ...
     //set showCheckSyntaxButton to true
    showCheckSyntaxButton:true,
    //set checkSyntax to true
    checkSyntax:true,
 };
  xs = x_spreadsheet('#gridjs-demo', option)
```
## 構文チェック＆スペル修正用のアクションURLを設定する。
たとえば：
```javascript
 const checkurl = "/GridJs2/CheckSyntax";  
 xs.setSyntaxCheckUrl(checkurl);
```
ユーザーがセルにテキスト内容を入力した後、構文チェックの動作はスプレッドシートアプリケーションによって自動的にトリガーされます。 

## サーバー側に構文チェック＆スペル修正を実装します。
たとえば：
```python
# The logic for invoking syntax checking here can be implemented through a third-party library or custom logic.
def correct_syntax(text, locale):  
# replace your logic  here     
    return text  

@app.route('/GridJs2/CheckSyntax', methods=['POST'])  
def check_syntax():  
    text = request.form.get('v')  
    locale = request.form.get('locale')  

    if not text:  
        return jsonify({  
            'Success': False,  
            'v': ''  
        }), 200  

    corrected_content = correct_syntax(text, locale)  

    return jsonify({  
        'Success': True,  
        'v': corrected_content  
    }), 200  
```





