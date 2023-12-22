---
title: 印刷するものが何もない場合の出力 PDF の空白ページを回避する
type: docs
weight: 30
url: /ja/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aspose.Cells for Python via .NET API で印刷するものが何もない場合の出力 PDF の空白ページを回避する方法を学びます。
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **考えられる使用シナリオ**

Excel ファイルが空で、ユーザーが Aspose.Cells for Python via .NET を使用して Excel ファイルを PDF に保存すると、出力 PDF に空白ページが表示されます。このデフォルトの動作が望ましくない場合があります。 Aspose.Cells for Python via .NET は、[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)この問題に対処するためのプロパティ。 *false** に設定する場合は、[**セル例外**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)出力 PDF に印刷するものが存在しない場合は常に発生します。

##  **印刷するものが何もない場合の出力 PDF の空白ページを回避する**

次のサンプル コードでは、空のブックを作成し、設定後にそれを PDF として保存します。[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)プロパティを *false** に設定します。出力 PDF には印刷するものが何もないため、[**セル例外**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)以下のように発生します。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **例外**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
