---
title: "Convert Excel and Apple Numbers Files"
linktitle: Numbers
type: docs
weight: 310
url: /net/convert-excel-to-numbers/
description: "Learn how to convert Excel workbooks to Apple Numbers format and import Apple Numbers spreadsheets into Excel using Aspose.Cells for .NET."
keywords: ["Aspose.Cells", "Excel to Numbers", "Numbers to Excel", "Apple Numbers", "NumbersLoadOptions"]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Convert Excel and Apple Numbers Files

Apple Numbers is a spreadsheet application developed by Apple Inc. It uses the `.numbers` file format to store spreadsheet data, formatting, formulas, tables, charts, and other objects.

Aspose.Cells for .NET supports converting Excel workbooks to Apple Numbers format and loading Numbers spreadsheets into Excel workbooks. These operations can be performed programmatically without requiring Microsoft Excel or Apple Numbers to be installed.

This section introduces the conversion capabilities for Apple Numbers and provides detailed guides for converting spreadsheets in both directions.

## Convert Excel to Apple Numbers

Aspose.Cells for .NET allows you to export an Excel workbook to Apple Numbers format by using the `Workbook.Save` method with `SaveFormat.Numbers`.

The conversion process loads the source Excel workbook and saves it as a `.numbers` file. Supported workbook content and formatting are written to the output file according to the capabilities of the Numbers format writer.

For a detailed example, including formatting, formulas, charts, images, and multi-worksheet workbooks, see [Convert Excel to Apple Numbers](/cells/python-net/convert-excel-to-apple-numbers/).

## Convert Apple Numbers to Excel

Aspose.Cells for .NET allows you to load Apple Numbers spreadsheets by using the `NumbersLoadOptions` class and save them as Excel workbooks.

During import, you can configure options such as `PreserveTableName` to control whether source table names are preserved. The `LoadTableType` property can also be used to specify how multiple tables in a Numbers worksheet are loaded.

For detailed instructions and code examples, see [Convert Apple Numbers to Excel](/cells/python-net/convert-apple-numbers-to-excel/).

## Conversion Features

The following table summarizes the main topics covered by the conversion guides.

| Feature | Description |
|---|---|
| Excel to Numbers | Export Excel workbooks to `.numbers` format. |
| Numbers to Excel | Import Numbers spreadsheets and save them in Excel formats such as XLSX. |
| Cell formatting | Convert supported fonts, fills, borders, alignment, and number formats. |
| Formulas | Process supported formulas and verify calculated results after conversion. |
| Tables | Configure Numbers table loading and preserve table names when required. |
| Charts and images | Convert supported charts, pictures, shapes, and other spreadsheet objects. |
| Multiple worksheets | Convert workbooks containing multiple worksheets and verify their organization. |

The actual conversion results depend on the features supported by Aspose.Cells and the capabilities of the source and destination formats. Some objects or formatting features may be represented differently after conversion.

## Validate Converted Files

For important workbooks, open the generated file in the target spreadsheet application and verify the cell values, formulas, formatting, table structure, charts, images, and other essential content.

A successful save confirms that the output file has been written, but it does not guarantee that every source feature has an identical representation in the destination format.

## Related Resources

- [Convert Excel to Apple Numbers](/cells/python-net/convert-excel-to-apple-numbers/)
- [Convert Apple Numbers to Excel](/cells/python-net/convert-apple-numbers-to-excel/)
- [SaveFormat Enumeration](https://reference.aspose.com/cells/net/aspose.cells/saveformat/)
- [NumbersLoadOptions API Reference](https://reference.aspose.com/cells/net/aspose.cells.numbers/numbersloadoptions/)
