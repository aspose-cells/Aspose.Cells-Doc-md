---
title: 将所有工作表列适配到单个PDF页面
type: docs
weight: 160
url: /zh/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: 学习如何使用 Aspose.Cells for Python via .NET API 在单个 PDF 页上调整所有工作表列。
keywords: 在 Python 中在单个 PDF 页上调整所有工作表列，使用 Python 在单个 PDF 页上调整工作表列，使用 Python 将所有工作表列保存到单个 PDF 页中，在 Python 中将所有列保存到单个 PDF 页。
---

{{% alert color="primary" %}}

有时您想生成一个将工作表的所有列适配到一个页面上的PDF文件。[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)属性以一种非常易于使用的方式提供了这个功能。输出PDF的高度和宽度等复杂计算由内部处理，基于工作表中的数据。

{{% /alert %}}

## **将工作表列适配到单个PDF页面**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)确保工作表中的所有列都呈现在单个PDF页面上，尽管根据工作表中的数据，行可能会扩展到几个页面。

下面的示例代码展示了如何使用[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)属性呈现具有100列的大型工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

当给定的工作表有很多列时，呈现的PDF文件可能以非常小的尺寸显示内容。当在查看应用程序中放大时，它仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样做可确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
