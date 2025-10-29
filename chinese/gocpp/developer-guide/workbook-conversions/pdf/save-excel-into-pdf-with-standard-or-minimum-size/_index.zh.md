---
title: 以标准或最小尺寸保存 Excel 为 PDF，使用 C++ 通过 Golang
linktitle: 使用标准大小或最小大小将Excel保存为PDF
type: docs
weight: 340
url: /zh/go-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: 了解如何使用 Aspose.Cells for C++ 将 Excel 文件保存为标准或最小尺寸的 PDF。
---

{{% alert color="primary" %}} 

默认情况下，Aspose.Cells 将 Excel 以标准尺寸保存为 PDF。但您也可使用 [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getoptimizationtype/) 属性将其保存为最小尺寸。该属性接受以下值：

- PdfOptimizationType::Standard
- PdfOptimizationType::MinimumSize

{{% /alert %}} 

## **使用 Aspose.Cells 将 Excel 保存为标准或最小尺寸的 PDF**
以下示例代码展示了如何使用 [PdfSaveOptions.GetOptimizationType()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getoptimizationtype/) 属性，将 Excel 保存为标准尺寸或最小尺寸的 PDF。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveExcelIntoPdfWithStandardOrMinimumSize.go" >}}
