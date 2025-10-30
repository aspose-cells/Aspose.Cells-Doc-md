---
title: Golang経由のC++でExcelをPDFに変換中のエラーを無視する
linktitle: Excel を PDF にレンダリングする際のエラーを無視
type: docs
weight: 80
url: /ja/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for C++を使用して、ExcelからPDFへの変換時にエラーを無視する方法を学びます。
---

## **可能な使用シナリオ**

ExcelをPDFに変換する際にエラーや例外が発生し、変換プロセスが終了することがあります。これらのエラーを無視するには、[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/)プロパティを使用します。この方法では、エラーや例外をスローせずに変換を完了できますが、データの損失が生じる可能性があります。したがって、データの損失が重要でない場合のみこのプロパティを使用してください。

## **Excel を PDF にレンダリングする際のエラーを無視**

以下のコードは、サンプルExcelファイル（55541778.xlsx）を読み込みますが、そのExcelファイルにはエラーがあり、17.11の[変換先PDF](55541779.pdf)でエラーがスローされます。ただし、[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/)プロパティを使用しているため、エラーは発生しません。ただし、このスクリーンショットに示される*丸みを帯びた赤い矢印のような図形*は失われます。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
