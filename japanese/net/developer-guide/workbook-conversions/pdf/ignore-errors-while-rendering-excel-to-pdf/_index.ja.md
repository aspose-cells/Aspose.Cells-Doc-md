---
title: Excel を PDF にレンダリングする際のエラーを無視
type: docs
weight: 80
url: /ja/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **可能な使用シナリオ**

ExcelファイルをPDFに変換する際に、エラーや例外が発生して変換プロセスが終了することがあります。[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)プロパティを使用して変換中のすべてのエラーを無視することができます。これにより、変換プロセスはエラーや例外をスローすることなくスムーズに完了しますが、データの損失が発生する可能性があります。したがって、データの損失が重要でない場合にのみこのプロパティを使用してください。

## **Excel を PDF にレンダリングする際のエラーを無視**

次のコードは、[サンプルExcelファイル](55541778.xlsx)を読み込みますが、サンプルExcelファイルにエラーがあり、17.11で[PDFに変換](55541779.pdf)する際にエラーが発生しますが、[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)プロパティを使用しているため、エラーは発生しません。ただし、このスクリーンショットに表示されているように、1つの*赤い矢印のような形*が失われます。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
