---
title: Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする
type: docs
weight: 50
url: /ja/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能な使用シナリオ**

Microsoft ExcelファイルがMicrosoft ExcelまたはAspose.Cellsを使用してHTMLにエクスポートされると、次のスクリーンショットに示すように、Document、Workbook、Worksheetなどのさまざまなタイプのプロパティもエクスポートされます。 [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties)、[**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)、[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) を**false**に設定することでこれらのプロパティのエクスポートを回避できます。これらのプロパティのデフォルト値は**true**です。次のスクリーンショットは、エクスポートされたHTML内のこれらのプロパティの見た目を示しています。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする**

次のサンプルコードは[サンプルExcelファイル](61767776.xlsx)をロードし、[output HTML](61767779.zip)内でDocument、Workbook、Worksheetプロパティをエクスポートしません。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
