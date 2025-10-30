---
title: Golang経由でC++を使用して、標準または最小サイズでExcelをPDFに保存
linktitle: Excelを標準サイズまたは最小サイズのPDFに保存する
type: docs
weight: 340
url: /ja/go-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aspose.Cells for C++を使用して、Excelファイルを標準または最小サイズのPDFに保存する方法を学びます。
---

{{% alert color="primary" %}} 

デフォルトでは、Aspose.CellsはExcelを標準サイズのPDFに保存します。ただし、[PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getoptimizationtype/)プロパティを使用して最小サイズで保存することも可能です。次の値を受け入れます：

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **Aspose.Cellsを使用してExcelを標準サイズまたは最小サイズのPDFに保存する**
次のサンプルコードは、[PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getoptimizationtype/)プロパティを使用してExcelを標準または最小サイズのPDFに保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveExcelIntoPdfWithStandardOrMinimumSize.go" >}}
