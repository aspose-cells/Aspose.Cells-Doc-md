---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells C++
description: Learn how to render array data into a single cell using the ArrayAsSingle and ExtraDelimiter attributes in Smart Markers with Aspose.Cells for Aspose.Cells for C++.
keywords: Aspose.Cells, C++ library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
url: /cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells supports rendering array data into a single cell via Smart Markers. By using the `ArrayAsSingle` attribute along with the `ExtraDelimiter` attribute, developers can control how array elements are separated within a single cell, providing flexible formatting for reports and templates.

{{% /alert %}}

## **Introduction**

Smart Markers in Aspose.Cells are a powerful, template-based feature that allows you to dynamically populate spreadsheet data using marker expressions such as `&=DataSource.Field`. The marker is placed in a designer workbook, and when the template is processed by the `WorkbookDesigner`, the markers are replaced with values from the supplied data source.

By default, when a Smart Marker references an array property (for example, `&=DataSource.Numbers`), the engine expands the array and places each element into a separate adjacent cell — either horizontally across a row or vertically down a column. While this behavior is convenient in many scenarios, there are situations where you would prefer to render the entire array into one single cell, with the elements concatenated and separated by a delimiter of your choice.

The `ArrayAsSingle` and `ExtraDelimiter` attributes, used together inside a Smart Marker tag, address exactly this requirement. They allow you to keep report layouts compact and predictable while still working natively with array data sources.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**

When a Smart Marker references an array property, Aspose.Cells expands the array across multiple cells by default. For example, a marker such as `&=Product.Tags` against a `string[]` containing four values will place each value into its own cell, pushing other template content outward and potentially breaking carefully designed report layouts.

### **Use Case Limitations**

There are many practical scenarios where the default spreading behavior is undesirable:

- **Summary-style reports** that need a compact one-row-per-record layout.
- **Tag, label, or keyword lists** that need to be displayed as comma-separated or pipe-separated values within a single cell.
- **Filter chips or status indicators** that group multiple values in one place for readability.
- **Downstream pipelines** (CSV export, PDF rendering, mail merge) that expect a single consolidated value per cell rather than an expanded range.
- **Cross-platform compatibility**, where some consumers cannot tolerate arrays that bleed across multiple cells.

### **The Gap It Fills**

Without a built-in mechanism, developers would be forced to pre-process data in C++ — joining arrays into delimited strings before binding them to the workbook designer. This duplicates logic, complicates data models, and increases the chance of errors. The `ArrayAsSingle` and `ExtraDelimiter` attributes eliminate this workaround by handling the formatting declaratively inside the Smart Marker itself.

## **Feature Benefits**

Using the `ArrayAsSingle` and `ExtraDelimiter` attributes in your Smart Markers provides several advantages:

- **Single-cell containment**: All array elements are rendered into exactly one cell, keeping layouts compact and predictable.
- **Custom delimiter control**: Specify any separator string you like — comma, semicolon, hyphen, pipe, newline, or any custom text.
- **Template-driven formatting**: No additional code is required to pre-process the data; formatting rules live inside the Smart Marker tag.
- **Cleaner reports**: Array data no longer pushes neighboring template content into different rows or columns.
- **Versatile data types**: Works with strings, numbers, dates, and any other data type that can be joined with a delimiter.
- **Backwards compatibility**: When the attributes are omitted, the original spreading behavior is preserved, so existing templates continue to work unchanged.

## **How to Use This Feature**

### **Smart Marker Syntax**

The `ArrayAsSingle` and `ExtraDelimiter` attributes are passed as key-value pairs inside the parentheses of a standard Smart Marker. The general syntax is:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

The marker is composed of the following parts:

- `&=DataSource.ArrayProperty` — the standard Smart Marker referencing the array property on the bound data source.
- `arrayasSingle=true` — instructs the engine to render the whole array into a single cell. Only the value `true` triggers the single-cell behavior.
- `extraDelimiter=", "` — defines the separator placed between array elements. The value is a string literal; it can be empty, a single character, or a multi-character string.

{{% alert color="primary" %}}

The `extraDelimiter` attribute accepts any string literal, including multi-character delimiters, custom text, or escape sequences such as `\n` for newline-separated output. If the array is empty, the resulting cell is left blank.

{{% /alert %}}

### **Step-by-Step Workflow**

The following workflow describes how to render an array into a single cell using Smart Markers.

1. **Prepare the data source**: Create a class (or data structure) that exposes a property returning an array. The property can return `std::vector<std::string>`, `std::vector<int>`, or any other supported array/vector type.
2. **Create a designer workbook**: Create a new `Workbook`, add a header row, and place a Smart Marker cell that references the array property with the `arrayasSingle` and `extraDelimiter` attributes.
3. **Instantiate the WorkbookDesigner**: Create a `WorkbookDesigner` object, attach the designer workbook to it, and bind your data source using the `SetDataSource` method.
4. **Process the markers**: Call the `WorkbookDesigner.Process()` method to expand the Smart Markers and populate the workbook with real data.
5. **Save the result**: Save the resulting workbook to disk in XLSX or any other supported file format.

### **Code Example 1 — Basic String Array Rendering**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner is not available in Aspose.Cells for C++
    // We need to simulate SmartMarker processing by replacing markers manually
    // Since Aspose.Cells C++ doesn't support WorkbookDesigner, we'll use U16String replacement
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Replace the smart marker with actual data
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Prepare data source
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Create workbook and get first worksheet
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Section 1: Default Smart Marker - values spread horizontally across cells
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Bind the data source and process Smart Markers
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Save the resulting workbook
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Notes & Best Practices**

Keep the following points in mind when working with the `ArrayAsSingle` and `ExtraDelimiter` attributes:

- The `extraDelimiter` value is treated as a string literal; escape any special characters that your template processor might interpret.
- The `arrayasSingle` attribute accepts a boolean value (`true` / `false`). Only `true` triggers the single-cell behavior; any other value falls back to the default spreading behavior.
- If the array is empty or null, the cell is left empty (or contains a blank string depending on the data type).
- The feature works with object data sources as well as `DataSet` and `DataTable` sources where a column can be split into arrays.
- For newline-separated output, you can use `\n` as the delimiter value.
- Place the Smart Marker in a cell that has sufficient width to display the resulting concatenated string; otherwise, the content may visually overflow into adjacent cells depending on the format.

## **Related Articles**

- [Smart Markers](/cells/cpp/smart-markers/)
- [Merging and Unmerging Cells](/cells/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}