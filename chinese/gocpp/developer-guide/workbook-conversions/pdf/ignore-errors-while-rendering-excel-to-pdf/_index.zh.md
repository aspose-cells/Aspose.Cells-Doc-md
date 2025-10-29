---
title: 在使用 C++ 通过 Golang 渲染 Excel 为 PDF 时忽略错误
linktitle: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 80
url: /zh/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: 了解如何在将Excel转换为PDF时使用Aspose.Cells for C++忽略错误。
---

## **可能的使用场景**

有时在将 Excel 文件转换为 PDF 时，会出现错误或异常，导致转换过程终止。您可以在转换过程中使用 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 属性，忽略所有此类错误。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会丢失部分数据。因此，只有在数据丢失对您来说不是关键的情况下，才建议使用此属性。

## **在将Excel渲染为PDF时忽略错误**

以下代码加载了[示例 Excel 文件](55541778.xlsx)，但该示例文件存在错误，在 17.11 版本中进行[转换为 PDF](55541779.pdf)时会抛出错误，但由于我们使用了 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 属性，它不会抛出错误。然而，像截图中显示的*圆角红色箭头形状*将会丢失。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
