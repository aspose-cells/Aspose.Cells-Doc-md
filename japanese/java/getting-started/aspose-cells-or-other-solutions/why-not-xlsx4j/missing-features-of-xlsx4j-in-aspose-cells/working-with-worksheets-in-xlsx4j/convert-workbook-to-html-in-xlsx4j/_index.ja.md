---
title: ワークブックをxlsx4jでHTMLに変換
type: docs
weight: 10
url: /ja/java/convert-workbook-to-html-in-xlsx4j/
---
## **Aspose.Cells - ワークブックを HTML に変換**
Aspose.Cells API は、スプレッドシートを HTML 形式にエクスポートするためのサポートを提供します。この目的のために、**Aspose.Cells**を使用します**HtmlSaveOptions**開発者が出力 HTML のいくつかの側面を制御できるようにするクラス。

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[Excel ファイルを HTML に変換する](/cells/ja/java/converting-workbook-to-different-formats/).

{{% /alert %}}
