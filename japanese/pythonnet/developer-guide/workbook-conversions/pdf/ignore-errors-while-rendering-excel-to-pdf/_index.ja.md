---
title: Excel を PDF にレンダリングする際のエラーを無視
type: docs
weight: 80
url: /ja/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for Python via .NET APIを使用してExcelをPDFに変換する際に、エラーを無視する方法を学びます。
keywords: Pythonを使用してExcelをPDFに変換する際にエラーを無視し、エラーを無視してExcelをPDFに保存する方法を学びます。Pythonを使用してExcelをPDFに変換する際にエラーを無視し、PythonでExcelをPDFに変換する際にエラーを無視します。
---

## **可能な使用シナリオ**

ExcelファイルをPDFに変換する際に、エラーや例外が発生して変換プロセスが終了することがあります。[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)プロパティを使用して変換中のすべてのエラーを無視することができます。これにより、変換プロセスはエラーや例外をスローすることなくスムーズに完了しますが、データの損失が発生する可能性があります。したがって、データの損失が重要でない場合にのみこのプロパティを使用してください。

## **Excel を PDF にレンダリングする際のエラーを無視**

次のコードは、[サンプルExcelファイル](55541778.xlsx)を読み込みますが、サンプルExcelファイルにエラーがあり、17.11で[PDFに変換](55541779.pdf)する際にエラーが発生しますが、[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)プロパティを使用しているため、エラーは発生しません。ただし、このスクリーンショットに表示されているように、1つの*赤い矢印のような形*が失われます。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
{{< app/cells/assistant language="python-net" >}}
