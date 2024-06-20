---
title: Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする
type: docs
weight: 50
url: /ja/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能な使用シナリオ**

Microsoft ExcelファイルをMicrosoft ExcelまたはAspose.Cellsを使用してHTMLにエクスポートすると、次のスクリーンショットに示すように、ドキュメント、ワークブック、ワークシートのさまざまな種類のプロパティもエクスポートされます。 [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties)、[**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)、[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)を**false**に設定することで、これらのプロパティをエクスポートしないようにすることができます。これらのプロパティのデフォルト値は**true**です。次のスクリーンショットは、これらのプロパティがエクスポートされたHTMLでどのように表示されるかを示しています。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする**

次のサンプルコードは、[サンプルExcelファイル](61767784.xlsx)を読み込み、HTMLに変換し、[出力HTML](61767783.zip)にドキュメント、ワークブック、ワークシートのプロパティをエクスポートしません。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
