---
title: Convert Apple Numbers to Excel
type: docs
weight: 220
url: /net/convert-numbers-to-excel/
description: Convert Apple Numbers file to Excel .
keywords: Convert, Convert Apple Numbers to Excel, Numbers to Excel
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


# Convert Apple Numbers to Excel

Apple Numbers is a spreadsheet application developed by Apple Inc. It stores spreadsheet data, formatting, formulas, tables, and other objects in the `.numbers` file format. Aspose.Cells for .NET enables developers to load Numbers spreadsheets and convert them to Excel workbooks programmatically, without requiring Microsoft Excel or Apple Numbers to be installed.

This article explains how to convert a Numbers file to Excel and how to handle formatting, table names, formulas, charts, and other spreadsheet content during the conversion.

## Convert Numbers to Excel

Aspose.Cells provides the `Workbook` class for loading and saving spreadsheet files. Use `NumbersLoadOptions` to configure the import process and save the loaded workbook in XLSX format.

### Steps to Convert Numbers to Excel

1. Create an instance of `NumbersLoadOptions`.
2. Configure the options required for the Numbers file.
3. Load the `.numbers` file into a `Workbook` object.
4. Save the workbook in XLSX format.

### C# Code Example
```
using Aspose.Cells;
using Aspose.Cells.Numbers;

class ConvertNumbersToExcel
{
    static void Main()
    {
        // Configure options for loading an Apple Numbers file.
        NumbersLoadOptions options = new NumbersLoadOptions();

        // Load the Numbers spreadsheet.
        Workbook workbook = new Workbook("input.numbers", options);

        // Save the workbook in Excel XLSX format.
        workbook.Save("output.xlsx", SaveFormat.Xlsx);
    }
}
```

The generated `output.xlsx` file can be opened in Microsoft Excel or other applications that support the XLSX format.

## Convert Formatted Numbers Spreadsheets to Excel

Numbers spreadsheets may contain more than plain cell values. They can include formatted tables, fonts, background colors, borders, number formats, formulas, charts, images, and other objects.

Aspose.Cells represents supported spreadsheet content in its workbook object model. When converting a Numbers file to XLSX, the workbook can be saved with the supported data and formatting represented in that model.

For example, a source Numbers spreadsheet might contain:

- A formatted header row with a background color and bold text.
- Borders and alignment applied to data cells.
- Currency, percentage, and date number formats.
- Formulas used to calculate totals.
- Multiple tables and worksheets.
- Charts and images.

Load and save the workbook using the same conversion procedure shown above. No separate formatting-conversion method is required for the supported cell styles.

**Note:** The appearance and behavior of some objects may differ between Numbers and Excel because the two applications use different spreadsheet models. Verify the generated XLSX file when fidelity is important, especially for complex tables, charts, formulas, and layout settings.

## Preserve Table Names When Importing Numbers Files

A Numbers worksheet can contain multiple tables, and table names can be important when identifying data or working with formulas.

Aspose.Cells provides the `PreserveTableName` property in the `NumbersLoadOptions` class to control whether table names are preserved when importing Numbers files.

### C# Code Example
```
using Aspose.Cells;
using Aspose.Cells.Numbers;

class PreserveNumbersTableNames
{
    static void Main()
    {
        NumbersLoadOptions options = new NumbersLoadOptions
        {
            PreserveTableName = true
        };

        Workbook workbook = new Workbook("input.numbers", options);

        workbook.Save("output.xlsx", SaveFormat.Xlsx);
    }
}
```

Set `PreserveTableName` to `true` when preserving source table names is important to your workflow.

For more information, see the [NumbersLoadOptions API Reference](https://reference.aspose.com/cells/net/aspose.cells.numbers/numbersloadoptions/).

## Load Multiple Tables from a Numbers Worksheet

A Numbers worksheet may contain multiple tables. The `LoadTableType` property lets you specify how multiple tables in one worksheet should be loaded.

The property uses the `LoadNumbersTableType` enumeration.

For example, the following code configures the loader to place each source table on a separate worksheet:
```
using Aspose.Cells;
using Aspose.Cells.Numbers;

class LoadNumbersTables
{
    static void Main()
    {
        NumbersLoadOptions options = new NumbersLoadOptions
        {
            LoadTableType = LoadNumbersTableType.OneTablePerSheet
        };

        Workbook workbook = new Workbook("input.numbers", options);

        workbook.Save("output.xlsx", SaveFormat.Xlsx);
    }
}
```

Choose the loading strategy according to the structure of the source file and how the resulting Excel workbook should be organized.

See the [LoadNumbersTableType API Reference](https://reference.aspose.com/cells/net/aspose.cells.numbers/loadnumberstabletype/) for the available values and their behavior.

## Convert Numbers Formulas and Calculated Values

Numbers and Excel do not use identical formula implementations. During conversion, Aspose.Cells processes supported formulas and represents them in the workbook model.

After conversion, check important formulas and their results in the generated Excel workbook. Formulas that depend on application-specific functions or features may require additional verification.

If your workflow depends on recalculated results, you can request formula calculation before saving:
```
using Aspose.Cells;
using Aspose.Cells.Numbers;

class ConvertNumbersAndCalculate
{
    static void Main()
    {
        NumbersLoadOptions options = new NumbersLoadOptions();
        Workbook workbook = new Workbook("input.numbers", options);

        // Recalculate formulas supported by Aspose.Cells.
        workbook.CalculateFormula();

        workbook.Save("output.xlsx", SaveFormat.Xlsx);
    }
}
```

Recalculation is optional. Use it when updated formula results are required rather than simply preserving the loaded workbook's existing state.

## Convert Numbers Charts, Images, and Other Objects

A Numbers spreadsheet may contain charts, images, shapes, text boxes, hyperlinks, and other objects in addition to cell data.

Aspose.Cells supports many spreadsheet objects through its workbook, worksheet, and drawing APIs. The conversion result depends on the object type and the features supported by both formats.

When converting a complex workbook, verify the following items in Excel:

- Chart types, titles, legends, axes, and data labels.
- Image and shape placement.
- Hyperlinks and text boxes.
- Row heights, column widths, hidden rows, and hidden columns.
- Conditional formatting and other supported worksheet settings.

If a specific object is essential to your application, include it in conversion tests before deploying the workflow.

## Handle Conversion Errors and Validate the Output

For production applications, validate the source file and handle exceptions that may occur while loading or saving a workbook.

A simple implementation can catch errors and report the affected file:
```
using System;
using Aspose.Cells;
using Aspose.Cells.Numbers;

class SafeNumbersConversion
{
    static void Main()
    {
        try
        {
            NumbersLoadOptions options = new NumbersLoadOptions();
            Workbook workbook = new Workbook("input.numbers", options);

            workbook.Save("output.xlsx", SaveFormat.Xlsx);

            Console.WriteLine("Conversion completed.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Conversion failed: {ex.Message}");
        }
    }
}
```

For important business documents, verify cell values, formulas, table names, formatting, and critical objects after conversion. A successful save confirms that the file was written; it does not guarantee that every source feature has an exact equivalent in Excel.

## Related Articles

- [NumbersLoadOptions API Reference](https://reference.aspose.com/cells/net/aspose.cells.numbers/numbersloadoptions/)
- [LoadNumbersTableType API Reference](https://reference.aspose.com/cells/net/aspose.cells.numbers/loadnumberstabletype/)
- [Conversion](https://docs.aspose.com/cells/net/conversion/)
