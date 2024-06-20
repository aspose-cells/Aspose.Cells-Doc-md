---
title: 出力PDFの空白ページを回避する
type: docs
weight: 30
url: /ja/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

Excelファイルが空で、そのファイルをAspose.CellsでPDFに保存すると、出力PDFに空白ページがレンダリングされます。このデフォルトの動作は望ましくない場合があります。Aspose.Cellsはこの問題に対処するために [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) プロパティを提供します。これを **false** に設定すると、出力PDFに印刷する内容がない場合に [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) が発生します。

## **出力PDFの空白ページを回避する**

次のサンプルコードでは、空のワークブックを作成し、その後 [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) プロパティを **false** に設定して PDF として保存します。出力される PDF には印刷する内容がないため、以下のように [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) が発生します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **例外**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
