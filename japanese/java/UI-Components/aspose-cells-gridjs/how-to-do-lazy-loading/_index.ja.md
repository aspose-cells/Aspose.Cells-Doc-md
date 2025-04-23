---
title: GridJsで遅延読み込みを行う方法  
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: この記事は、GridJsで遅延読み込みを実装する方法について説明しています。
keywords: GridJs,遅延読み込み,オンデマンド読み込み,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

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
```java 
  Config.setLazyLoading(true);
```
## 遅延読み込みのアクションURLを設定する。
たとえば：
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
ユーザーがアクティブでない別のワークシートをクリックすると、クエリデータのアクションがスプレッドシートアプリケーションによって自動的にトリガーされます。 

## サーバーサイドのコントローラーで遅延読み込みアクションを実装する。
たとえば：
```java
    @PostMapping("/LazyLoading")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setHeader(HttpHeaders.CONTENT_ENCODING, "gzip");

        try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
            try {
				wbj.lazyLoadingStream(gzipOutputStream, uid, sheetName);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
    }
```





