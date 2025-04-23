---
title: Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする
type: docs
weight: 50
url: /ja/python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **可能な使用シナリオ**

Microsoft ExcelファイルがMicrosoft ExcelまたはAspose.Cellsを使用してHTMLにエクスポートされると、次のスクリーンショットに示すように、Document、Workbook、Worksheetなどのさまざまなタイプのプロパティもエクスポートされます。 [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties)、[**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties)、[**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) を**false**に設定することでこれらのプロパティのエクスポートを回避できます。これらのプロパティのデフォルト値は**true**です。次のスクリーンショットは、エクスポートされたHTML内のこれらのプロパティの見た目を示しています。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする**

次のサンプルコードは[サンプルExcelファイル](61767776.xlsx)をロードし、[output HTML](61767779.zip)内でDocument、Workbook、Worksheetプロパティをエクスポートしません。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
