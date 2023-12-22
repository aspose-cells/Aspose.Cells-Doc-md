---
title: 将指定工作表保存到PDF
type: docs
weight: 140
url: /zh/python-net/save-specified-worksheets-to-pdf/
description: 了解如何使用 Aspose.Cells for Python via .NET API 将指定工作表保存到 PDF。
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
默认 Aspose.Cells for Python via .NET 全部保存**可见的**工作簿中的工作表转换为 pdf 文件。和**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginationsaveoptions/sheet_set/)**选项，您可以将指定的工作表保存到 pdf 文件。例如，您可以将活动工作表保存为 pdf，将所有工作表（可见和隐藏工作表）保存为 pdf，将自定义多个工作表保存为 pdf。

##  **将活动工作表保存到 PDF**

如果您只想将活动工作表导出为 pdf，您可以通过传递来实现**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)**到**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginationsaveoptions/sheet_set/)**选项。

工作表`Sheet2`是源文件的活动工作表[图纸集示例.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **将所有工作表保存到 PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)**指示工作簿中的可见工作表，以及**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)**表示工作簿中的所有工作表，包括可见工作表和隐藏/不可见工作表。如果你想将所有工作表导出为pdf，你可以通过**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)**到**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginationsaveoptions/sheet_set/)**选项。

源文件[图纸集示例.xlsx](sheetset-example.xlsx)包含所有四张带有隐藏表 `Sheet3` 的表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **将指定工作表保存到PDF**
如果您想将所需/自定义的多个工作表导出为 pdf，您可以通过将多个工作表索引传递给**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginationsaveoptions/sheet_set/)**选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好致电[**工作簿.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)就在将电子表格渲染为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}
