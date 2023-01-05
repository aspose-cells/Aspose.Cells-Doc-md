---
title: スプレッドシート エディターのナレッジ ベース
type: docs
weight: 30
url: /ja/java/spreadsheet-editor-knowledge-base/
---
## **HTML5 スプレッドシート エディタをどこにでも埋め込む**

HTML5 スプレッドシート エディターは、任意の Web サイト、ブログ、フォーラムに埋め込んで、インターネット上でスプレッドシートを共有できます。スタンドアロン エディターとして埋め込むことも、スプレッドシート ファイルと共に読み込むこともできます。

**スタンドアロン エディタとして埋め込む**

スタンドアロン エディターとして埋め込むには、HTML IFRAME タグを使用して Web サイトに追加します。例えば：

{{< highlight "html" >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**スプレッドシートで埋め込む**

埋め込みエディタにスプレッドシートをロードするには**URL**パラメータ。例えば：

{{< highlight "html" >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
