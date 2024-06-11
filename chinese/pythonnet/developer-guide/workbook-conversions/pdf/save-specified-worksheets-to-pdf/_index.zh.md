---
title: 将指定的工作表保存为 PDF
type: docs
weight: 140
url: /zh/python-net/save-specified-worksheets-to-pdf/
description: 了解如何使用Aspose.Cells for Python via .NET API将指定的工作表保存为PDF。
keywords: 使用Python将活动工作表保存为PDF，将所有工作表保存为PDF，将指定工作表保存为PDF
---

默认情况下，Aspose.Cells for Python via .NET将工作簿中的**可见**工作表保存为PDF文件。使用**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**选项，您可以将指定的工作表保存为PDF文件。例如，您可以将活动工作表保存为PDF，将所有工作表（包括可见和隐藏的工作表）保存为PDF，将自定义的多个工作表保存为PDF。

## **将活动工作表保存为 PDF**

如果要将活动工作表单独导出为PDF，可以通过将**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells/rendering/sheetset/active/)**传递给**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**选项来实现这一点。

工作表 `Sheet2` 是源文件[sheetset-example.xlsx](sheetset-example.xlsx)的活动工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **将所有工作表保存为 PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells/rendering/sheetset/visible/)**表示工作簿中可见的工作表，而**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells/rendering/sheetset/all/)**表示工作簿中所有工作表，包括可见和隐藏/不可见的工作表。如果要将所有工作表导出为PDF，只需将 **[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells/rendering/sheetset/all/)**传递给**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**选项。

源文件[sheetset-example.xlsx](sheetset-example.xlsx)包含所有四个工作表，其中隐藏了工作表`Sheet3`。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **将指定的工作表保存为 PDF**
如果要将所需/自定义的多个工作表导出为PDF，可以通过将多个工作表索引传递给**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**选项来实现。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
