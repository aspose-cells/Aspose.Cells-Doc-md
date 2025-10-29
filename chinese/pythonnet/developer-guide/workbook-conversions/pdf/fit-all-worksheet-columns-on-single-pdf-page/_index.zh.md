---
title: 将所有工作表列调整到单个PDF页面
type: docs
weight: 160
url: /zh/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: 学习如何使用Aspose.Cells for Python via .NET API将所有工作表列调整到单个PDF页面。
keywords: Python将所有工作表列调整到单个PDF页面，在Python中将工作表列调整到单个PDF页面，Python保存所有工作表列到PDF页面，Python将所有列保存到单个PDF页面
---

{{% alert color="primary" %}}

有时候，您希望生成一个PDF文件，将工作表的所有列适合一页。[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)属性以一种非常易于使用的方式提供了这种功能。输出PDF的高度和宽度等复杂计算是在内部处理的，是基于工作表中的数据。

{{% /alert %}}

## **使工作表列适合单个PDF页面**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)确保工作表中的所有列都呈现在单个PDF页面上，尽管根据工作表中的数据，行可能会扩展到几页。

下面的示例代码显示了如何使用[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)属性呈现一个包含100列的大型工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

当给定的工作表有很多列时，渲染的PDF文件可能以非常小的尺寸显示内容。在类似Acrobat Reader的查看应用程序中缩放后仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
