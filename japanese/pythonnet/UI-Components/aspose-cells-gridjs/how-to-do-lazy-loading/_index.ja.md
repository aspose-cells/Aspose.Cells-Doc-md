---
title: GridJsで遅延読み込みを行う方法  
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: この記事は、GridJsで遅延読み込みを実装する方法について説明しています。
keywords: GridJs,遅延読み込み,オンデマンド読み込み,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

---

## 遅延読み込みについて 
多数のワークシートを含むスプレッドシートファイルを扱う場合、最初にアクティブなワークシートのみを読み込むことでロードプロセスを最適化できます。

この戦略により、サーバー側のJSONレスポンスには最初に選択されたワークシートのデータのみが含まれるようになります。  

結果として、初期のウェブトラフィックが大幅に削減され、読み込み時間を短縮し、ユーザーエクスペリエンスが向上します。  

さらに、GridJsはユーザーの操作に動的に対応するように設計されています。具体的には、ユーザーが別のワークシートをクリックすると、

GridJsは、そのワークシートのデータを取得するためにサーバーへのリクエストをインテリジェントにトリガーします。  

このオンデマンド読み込みメカニズムは、不必要なデータの転送をさらに削減するだけでなく、作業中のワークシートの最新情報へ常にアクセスできる保証もします。  

このアプローチを採用することで、初期の読み込み時間を最適化するとともに、応答性が良く効率的なアプリケーションを維持し、スプレッドシートファイル内のワークシート数の増加に対応します。

# GridJsで遅延読み込みを実装するには、手順は次のとおりです
## 遅延読み込み用の設定オプションを設定する。
たとえば：
```python 
       Config.set_lazy_loading(True)
```
## 遅延読み込みのアクションURLを設定する。
たとえば：
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
ユーザーがアクティブでないワークシートをクリックした後、クエリデータの動作はスプレッドシートアプリケーションによって自動的にトリガーされます。 

## サーバーサイドのコントローラーで遅延読み込みアクションを実装する。
たとえば：
```python
@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
             wbj.lazy_loading_stream(gzip_stream,uid, sheet_name)


        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)
```





