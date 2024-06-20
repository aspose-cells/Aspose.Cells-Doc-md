---
title: 出力PDFの空白ページを回避する
type: docs
weight: 30
url: /ja/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

Excelファイルが空で、そのファイルをAspose.CellsでPDFに保存すると、出力PDFに空白ページがレンダリングされます。このデフォルトの動作は望ましくない場合があります。Aspose.Cellsはこの問題に対処するために [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) プロパティを提供します。これを **false** に設定すると、出力PDFに印刷する内容がない場合に [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) が発生します。

## **出力PDFの空白ページを回避する**

以下のサンプルコードは、空のワークブックを作成し、[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) プロパティを **false** に設定して出力PDFとして保存します。出力PDFに印刷する内容がないため、以下の [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) が発生します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **例外**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
