---
title: Excel のドキュメント ワークブックとワークシートのプロパティを HTML 変換にエクスポートする
type: docs
weight: 50
url: /ja/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **考えられる使用シナリオ**

Microsoft Excel または Aspose.Cells を使用して Microsoft Excel ファイルを HTML にエクスポートすると、次のスクリーンショットに示すように、さまざまな種類のドキュメント、ワークブック、およびワークシート プロパティもエクスポートされます。を設定することで、これらのプロパティのエクスポートを回避できます。[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)と[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)なので**間違い**.これらのプロパティのデフォルト値は**真実**.次のスクリーンショットは、エクスポートされた HTML でこれらのプロパティがどのように見えるかを示しています。

![todo:画像_代替_文章](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excel のドキュメント、ワークブック、およびワークシートのプロパティを HTML 変換にエクスポートする**

次のサンプル コードは、[サンプル Excel ファイル](61767784.xlsx)HTML に変換し、ドキュメント、ワークブック、およびワークシートのプロパティをエクスポートしません。[出力 HTML](61767783.zip).

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
