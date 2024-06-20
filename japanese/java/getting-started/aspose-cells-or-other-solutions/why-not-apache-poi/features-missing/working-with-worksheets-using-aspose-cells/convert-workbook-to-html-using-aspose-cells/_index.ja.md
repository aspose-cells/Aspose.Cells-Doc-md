---
title: Aspose.Cellsを使用してワークブックをHTMLに変換する
type: docs
weight: 20
url: /ja/java/convert-workbook-to-html-using-aspose-cells/
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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

詳細については、[ExcelファイルをHTMLに変換](/cells/ja/java/converting-workbook-to-different-formats/)をご覧ください。

{{% /alert %}}
