---
title: スプレッドシート エディター ナレッジ ベース
type: docs
weight: 30
url: /ja/java/spreadsheet-editor-knowledge-base/
---

## **どこにでもHTML5 スプレッドシート エディターを埋め込む**

HTML5 スプレッドシート エディターは、スプレッドシートをインターネット上で共有するためにウェブサイト、ブログ、フォーラムに埋め込むことができます。スタンドアロン エディターとして埋め込むか、スプレッドシート ファイルで読み込むことができます。

**スタンドアロン エディターとして埋め込む**

スタンドアロン エディターとして埋め込むには、HTML IFRAME タグをウェブサイトに追加します。例:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**スプレッドシートで埋め込む**

埋め込まれたエディターにスプレッドシートを読み込むには、**url**パラメータを使用します。例:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
