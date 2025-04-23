---
title: xlsx4j でワークブックをHTMLに変換する
type: docs
weight: 10
url: /ja/java/convert-workbook-to-html-in-xlsx4j/
---

## **Aspose.Cells - ワークブックをHTMLに変換する**
Aspose.Cells のAPIは、スプレッドシートをHTML形式にエクスポートするサポートを提供しています。この目的のために、Aspose.CellsはHTMLSaveOptionsクラスを使用し、開発者が出力HTMLのさまざまな側面を制御することができます。

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

詳細については、[ExcelファイルをHTMLに変換](/cells/ja/java/converting-workbook-to-different-formats/)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
