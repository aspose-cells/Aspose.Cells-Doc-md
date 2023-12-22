---
title: Excel を PDF にレンダリングする際のエラーを無視する
type: docs
weight: 80
url: /ja/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for Python via .NET API を使用して Excel を PDF にレンダリングする際のエラーを無視する方法を説明します。
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **考えられる使用シナリオ**

 Excel ファイルを PDF に変換すると、エラーまたは例外が発生し、変換プロセスが終了することがあります。次のコマンドを使用すると、変換プロセス中にこのようなエラーをすべて無視できます。[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)財産。このようにして、変換プロセスはエラーや例外をスローすることなくスムーズに完了しますが、データの損失が発生する可能性があります。したがって、このプロパティは、データの損失が重大ではない場合にのみ使用してください。

##  **Excel を PDF にレンダリングする際のエラーを無視する**

次のコードは、[サンプル Excel ファイル](55541778.xlsx)しかし、サンプル Excel ファイルには誤りがあり、実行中にエラーがスローされます。[PDFへの変換](55541779.pdf) 17.11では、しかし私たちは使用しているので[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)プロパティを使用しても、エラーはスローされません。ただし、1 つは*丸い赤い矢印のような形*このスクリーンショットに示されているように、失われます。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
