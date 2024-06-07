---
title: 将指定的工作表保存为 PDF
type: docs
weight: 51
url: /zh/java/save-specified-worksheets-to-pdf/
---

默认情况下，Aspose.Cells会将工作簿中的所有**可见**工作表保存为PDF文件。使用**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**选项，您可以将特定的工作表保存为PDF文件，例如将活动工作表保存为PDF，将所有工作表（包括可见和隐藏的工作表）保存为PDF，将自定义的多个工作表保存为PDF。

## **将活动工作表保存为PDF**

如果您只希望将活动工作表导出为PDF，可以通过将**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)**传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**选项来实现。

工作表 `Sheet2` 是源文件 [sheetset-example.xlsx](sheetset-example.xlsx) 的活动工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **将所有工作表保存为PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)**表示工作簿中可见的工作表，而**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)**表示工作簿中的所有工作表，包括可见和隐藏/不可见的工作表。如果要将所有工作表导出到PDF，只需将**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)**传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**选项。

源文件 [sheetset-example.xlsx](sheetset-example.xlsx) 包含所有四个工作表，其中隐藏工作表为 `Sheet3`。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **保存指定的工作表至PDF**
如果要将所需/自定义的多个工作表导出到PDF，可以通过将多个工作表索引传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**选项来实现。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格渲染为PDF格式之前调用[`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--)。这样做将确保重新计算公式依赖的值，并在PDF中呈现正确的值。

{{% /alert %}}
