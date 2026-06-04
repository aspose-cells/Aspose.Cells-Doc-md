---
title: Splitting Excel Files by Worksheet or Range
description: Aspose.Cells for .NET enables developers to split Excel files into multiple workbooks by copying individual worksheets or specific cell ranges. This article explains how to programmatically split Excel files using two common approaches: copying entire worksheets to new workbooks, and copying specific ranges to new workbooks.
keywords: Aspose.Cells, .NET, split Excel, workbook split, worksheet copy, range copy, Excel file split, C# Excel split
type: docs
weight: 69
url: /net/splitting-excel-files/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET supports non-destructive splitting of Excel files — the original file remains unchanged unless explicitly overwritten. Developers can split files at the worksheet level (one workbook per sheet) or at the range level (extract specific cell regions into new workbooks), preserving formatting, formulas, charts, and other objects.

{{% /alert %}}

## **Introduction**

Splitting an Excel file refers to the process of dividing a single workbook into multiple separate workbooks based on specific criteria — such as individual worksheets or designated cell ranges. This operation is commonly used in scenarios such as:

- Distributing specific sheets (e.g., monthly reports) from a central master workbook.
- Extracting subsets of data for archival or processing purposes.
- Reducing file size by splitting large spreadsheets into manageable parts.
- Generating tailored output files for different departments or recipients.

Aspose.Cells for .NET provides robust APIs for splitting Excel files without requiring Microsoft Excel to be installed. The library supports:

- **Worksheet-level splitting**: Copying entire worksheets—including their formatting, formulas, charts, and embedded objects—into new workbooks.
- **Range-level splitting**: Extracting specific cell ranges (e.g., A1:Z1000) to new workbooks, with optional control over formatting, formulas, and cell references.

Both approaches preserve the integrity of cell contents, styles, and named ranges (within the scope of the copied worksheet or range). The original workbook remains unmodified unless explicitly saved back.

---

## **Approach 1: Split Excel File by Copying Each Worksheet to a New Workbook**

This approach creates a separate workbook for each worksheet in the source Excel file. The result is one output file per worksheet, maintaining all content—including formulas, charts, and conditional formatting—intact in the new workbooks.

### **Overview**

Each worksheet from the source file is copied into a new `Workbook` instance using the `Worksheet.Copy()` method. This ensures that all related elements—such as worksheet-scoped named ranges, styles, and embedded objects—are preserved. The default empty worksheet in the new workbook is typically removed before copying.

> **Note**: Hidden or very hidden sheets retain their visibility state upon copy. Chart sheets (e.g., `ChartSheet` objects) are also copied as standalone worksheets if embedded in the workbook structure.

### **Step-by-Step Instructions**

1. Load the source Excel file using the `Workbook` class.
2. Iterate through each `Worksheet` in the `sourceWorkbook.Worksheets` collection.
3. For each worksheet:
   - Create a new `Workbook`. By default, this includes one empty worksheet.
   - Remove the default worksheet to avoid duplicates.
   - Use `Worksheet.Copy(Worksheet)` or `Worksheets.AddCopy(string)` to duplicate the source worksheet into the new workbook.
   - Optionally rename the output filename based on the worksheet name (e.g., `"Sales_Jan.xlsx"`).
4. Save each new workbook to disk using `Workbook.Save(string filePath)`.

{{< gist "aspose-cells-gists" "" "SplittingExcelFiles-LoadExcelFileWorkbookIterateThroughItsWorksheetsCr-0.cs" >}}

### **Input/Output Expectations**

| Input | Output |
|-------|--------|
| One Excel file with *N* worksheets (e.g., `"SalesData.xlsx"`) | *N* Excel files (e.g., `"Sheet1.xlsx"`, `"Sheet2.xlsx"`, …) |
| Preserved: formulas, cell styles, charts, images, named ranges (local only), conditional formatting | Each output file contains only one worksheet, with original formatting and behavior intact |

---

## **Approach 2: Split Excel File by Copying Ranges to New Workbooks**

This approach extracts a specific range (e.g., `"A1:D50"`) from a worksheet into a new workbook. It is useful for exporting filtered or subset data (e.g., a quarterly summary or selected columns) without including the full worksheet context.

### **Overview**

A cell range is copied using `Cells.CopyRange(...)`, which supports control over whether formatting, formulas, and cell references are preserved. Unlike full worksheet copying, range copying does *not* include charts, images, or shapes unless manually handled.

> **Important**: Relative cell references in formulas may break after copying unless `CopyOptions.SetUpdateReference(true)` is used. This setting adjusts references to align with the new location.

### **Step-by-Step Instructions**

1. Load the source Excel file using the `Workbook` class.
2. Access the source worksheet by name or index (e.g., `sourceWorkbook.Worksheets["DataSheet"]`).
3. Create a new `Workbook` and access its first worksheet (`destWorkbook.Worksheets[0]`).
4. Define the source range (e.g., A1:D50) and corresponding destination starting point (e.g., A1 in the new workbook).
5. Configure `CopyOptions` to control:
   - Whether styles and formatting are preserved (`SetCopyFormatStyle(true)`),
   - Whether formulas and references are updated (`SetUpdateReference(true)`, `SetUpdateFormula(true)`),
   - Whether to copy only values (`SetCopyValueOnly(true)`).
6. Use `sourceCells.CopyRange(destCells, 0, 0, rowCount, colCount, copyOptions)` to perform the copy.
7. Save the new workbook.

{{< gist "aspose-cells-gists" "" "SplittingExcelFiles-SplitExcelFileByCopyingRangesToNewWorkbooks-1.cs" >}}

### **Input/Output Expectations**

| Input | Output |
|-------|--------|
| A source workbook with sample data (e.g., 80 rows of Product/Region/Quarter/Sales in columns A-D, with bold header formatting) | A new workbook containing only the first 21 rows (header + 20 data rows), with formatting preserved |
| Source data created programmatically or loaded from an existing file | `ExtractedRange_Output.xlsx` with one worksheet named `"ExtractedRange"`, auto-fitted columns, and styles intact |

---

## **Notes & Best Practices**

- **Performance Considerations**: Splitting large workbooks (e.g., files with many sheets or large cell populations) can be memory-intensive. Consider using `Workbook.Settings.MemorySetting = MemorySetting.MemoryPreference` to optimize memory usage.
  
---

{{< app/cells/assistant language="csharp" >}}