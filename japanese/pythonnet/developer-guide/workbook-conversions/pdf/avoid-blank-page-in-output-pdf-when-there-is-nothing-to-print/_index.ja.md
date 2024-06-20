---
title: 出力PDFの空白ページを回避する
type: docs
weight: 30
url: /ja/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aspose.Cells for Python via .NET APIを使用した、出力PDFの空白ページを印刷する要素がない場合の回避方法の学習。
keywords: Pythonで出力PDFに何も印刷する要素がない場合の空白ページを回避する方法。
---

## **可能な使用シナリオ**

Excelファイルが空であり、Aspose.Cells for Python via .NETを使用してPDFに保存すると、出力PDFには空白のページが生成されます。このデフォルトの動作は望ましくない場合がありますので、Aspose.Cells for Python via .NETはこの問題に対処するための[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)プロパティを提供しています。これを**false**に設定すると、出力PDFに印刷する要素がない場合に[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)が発生します。

## **出力PDFの空白ページを回避する**

次のサンプルコードでは、空のワークブックを作成し、その後 [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) プロパティを **false** に設定して PDF として保存します。出力される PDF には印刷する内容がないため、以下のように [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) が発生します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **例外**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
