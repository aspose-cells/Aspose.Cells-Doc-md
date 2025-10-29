---
title: 使用 Golang 通过 C++ 将所有工作表列适配到单个 PDF 页面
linktitle: 将所有工作表列调整到单个PDF页面
type: docs
weight: 160
url: /zh/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: 生成一个 PDF，使所有工作表列都适合单个页面，使用 Aspose.Cells 通过 Golang 结合 C++。
---

{{% alert color="primary" %}}

有时你想生成一个 PDF 文件，将工作表的所有列适合在一页上。 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 属性提供了这个功能，内部处理复杂的计算，如输出 PDF 的高度和宽度，基于工作表中的数据。

{{% /alert %}}

## **使工作表列适合单个PDF页面**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 确保将工作表中的所有列渲染到单个 PDF 页面上，虽然行可能会根据工作表中的数据扩展到多页。

以下示例代码演示了如何使用 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 属性来渲染包含 100 列的大型工作表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

当给定的工作表有很多列时，渲染的PDF文件可能以非常小的尺寸显示内容。在类似Acrobat Reader的查看应用程序中缩放后仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
