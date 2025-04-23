---
title: HTMLにスプレッドシートをレンダリングする際のデフォルトフォントを設定する
type: docs
weight: 830
url: /ja/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用すると、スプレッドシートをHTMLにレンダリングする際のデフォルトフォントを設定できます。この目的のために、[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)を使用してください。このプロパティは、スプレッドシート内のいくつかのセルに無効または存在しないフォントがある場合に便利です。その場合、これらのセルは[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)プロパティで指定されたフォントでレンダリングされます。

{{% /alert %}} 
## **スプレッドシートをHTMLにレンダリングする際のデフォルトフォントを設定する**
次のサンプルコードは、ブックを作成し、最初のワークシートのセルB4にテキストを追加し、そのフォントを未知の/存在しないフォントに設定します。それからブックを異なるデフォルトフォント名（Courier New、Arial、Times New Romanなど）でHTML形式で保存します。

スクリーンショットは、[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)プロパティを介して異なるデフォルトフォント名を設定した効果を示しています。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

このコードは、Courier Newを使用した[出力HTMLファイル](5472568)、Arialを使用した[出力HTML](5472567)、およびTimes New Romanを使用した[出力HTMLファイル](5472565)を生成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
