---
title: 生成されるページ数の制限  Golang経由のExcelからPDFへの変換
linktitle: 生成されるページ数を制限
type: docs
weight: 180
url: /ja/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aspose.CellsとC++を使用して、変換時のページ数を制限する方法を学びます。
---

{{% alert color="primary" %}}

時には、特定のページ範囲を出力PDFファイルに印刷したいことがあります。Aspose.Cellsには、ExcelスプレッドシートをPDFファイル形式に変換する際に生成されるページ数を制限する機能があります。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値が出力ファイルに表示されます。

{{% /alert %}}
