---
title: GridJsで遅延読み込みを行う方法  
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: この記事は、GridJsで遅延読み込みを実装する方法について説明しています。
keywords: GridJs,遅延読み込み,オンデマンド読み込み,
aliases:
  - /net/aspose-cells-gridjs/lazy-loading/
  - /net/aspose-cells-gridjs/loading-on-demand/

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
```C# 
   Config.LazyLoading = true;
```
## 遅延読み込みのアクションURLを設定する。
たとえば：
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoadingStreamJson";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
ユーザーがアクティブでないワークシートをクリックした後、クエリデータの動作はスプレッドシートアプリケーションによって自動的にトリガーされます。 

## サーバーサイドのコントローラーで遅延読み込みアクションを実装する。
たとえば：
```C#
    [HttpPost]
 // post: /GridJs2/LazyLoadingStreamJson?name=&uid=
 public ActionResult LazyLoadingStreamJson()
 {
     string sheetName = HttpContext.Request.Form["name"];
     string uid = HttpContext.Request.Form["uid"];
     GridJsWorkbook wbj = new GridJsWorkbook();


     Response.ContentType = "application/json";
     Response.Headers.Add("Content-Encoding", "gzip");

     using (GZipStream gzip = new GZipStream(Response.Body, CompressionLevel.Optimal))
     {
        wbj.LazyLoadingStream(gzip, uid, sheetName);

     }

     return new EmptyResult();
 }
```





