---
title: GolangをC++経由でExcelのドキュメントブックとワークシートのプロパティをHTML変換時にエクスポート
linktitle: ExcelからHTMLへの変換において、ドキュメント、ワークブック、ワークシートのプロパティをエクスポート
type: docs
weight: 50
url: /ja/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Aspose.Cells for C++を使用して、Excelファイルの変換時にドキュメント、ワークブック、ワークシートのプロパティをエクスポートまたは省略する方法を学びます。
---

## **可能な使用シナリオ**

Microsoft ExcelまたはAspose.Cellsを使用してExcelファイルをHTMLにエクスポートする際、さまざまな種類のドキュメント、ワークブック、ワークシートのプロパティもエクスポートされます（以下のスクリーンショット参照）。これらのプロパティのエクスポートを抑制するには、[**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/)、[**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/)、[**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) を **false** に設定します。デフォルトは **true** です。以下のスクリーンショットは、エクスポートされたHTML内のこれらのプロパティの見た目を示しています。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **ExcelからHTMLへの変換でドキュメント、ワークブック、ワークシートのプロパティをエクスポート**

次のサンプルコードは、[サンプルExcelファイル](61767776.xlsx) を読み込み、ドキュメント、ワークブック、ワークシートのプロパティをエクスポートせずにHTMLに変換します（ [出力HTML](61767779.zip) 参照）。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
