---
title: 将指定的工作表保存为 PDF
type: docs
weight: 51
url: /zh/java/save-specified-worksheets-to-pdf/
---

默认情况下，Aspose.Cells 会将工作簿中所有**可见**的工作表保存为 PDF 文件。使用**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** 选项，你可以将指定的工作表保存为 PDF 文件。例如，你可以将活动工作表保存为 PDF，将所有工作表（包括可见和隐藏工作表）保存为 PDF，将自定义多个工作表保存为 PDF。

## **将活动工作表保存为 PDF**

如果你只想将活动工作表导出为 PDF，你可以通过将**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** 传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** 选项来实现。

工作表 `Sheet2` 是源文件[sheetset-example.xlsx](sheetset-example.xlsx)的活动工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **将所有工作表保存为 PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** 表示工作簿中的可见工作表，**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** 表示工作簿中所有工作表，包括可见和隐藏的/不可见的工作表。如果你想导出所有工作表为 PDF，你可以将**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** 传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** 选项。

源文件[sheetset-example.xlsx](sheetset-example.xlsx)包含所有四个工作表，其中隐藏了工作表`Sheet3`。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **将指定的工作表保存为 PDF**
如果你想将所需/自定义多个工作表导出为 PDF，你可以通过将多个工作表索引传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** 选项来实现。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

如果你的电子表格包含公式，最好在将电子表格渲染为 PDF 格式之前调用[`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--)。这样做可以确保公式依赖的值被重新计算，并且在 PDF 中呈现出正确的值。

{{% /alert %}}
