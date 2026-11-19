---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET
description: Learn how to render array data into a single cell using the arrayassingle and arraydelimiter Smart Marker attributes in Aspose.Cells for Python via .NET.
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells
url: /python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Python via .NET library, spreadsheet, Smart Markers, arrayassingle, arraydelimiter, single cell array, array rendering, template
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells can render an array data source into one single cell through Smart Markers. The `arrayassingle` attribute turns off the default element-by-element spreading, and the `arraydelimiter` attribute chooses the separator placed between the joined elements — comma by default, or any single character or quoted multi-character string you specify.
{{% /alert %}}

## **Introduction**
Smart Markers in Aspose.Cells are a template-based feature that populates spreadsheet data dynamically using marker expressions such as `&=DataSource.Field`. The marker is placed in a designer workbook, and when the template is processed by the `WorkbookDesigner`, the markers are replaced with values from the supplied data source.
By default, when a Smart Marker references an array field (for example, `&=Product.Tags` bound to a list of four values), the engine expands the array and places each element into its own cell, spreading the values vertically down the column below the marker. While this behavior is convenient in many scenarios, there are situations where you would prefer to render the entire array into one single cell, with the elements concatenated and separated by a delimiter of your choice.
The `arrayassingle` and `arraydelimiter` attributes, written inside a Smart Marker's parentheses in `name:value` form, address exactly this requirement. They allow you to keep report layouts compact and predictable while still working natively with array data sources.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
When a Smart Marker references an array field, Aspose.Cells expands the array across multiple cells by default. For example, a marker such as `&=Product.Tags` against a list containing four values places each value into its own cell below the marker, pushing other template content outward and potentially breaking carefully designed report layouts.

### **Use Case Limitations**
There are many practical scenarios where the default spreading behavior is undesirable:
- **Summary-style reports** that need a compact one-row-per-record layout.
- **Tag, label, or keyword lists** that need to be displayed as comma-separated or pipe-separated values within a single cell.
- **Filter chips or status indicators** that group multiple values in one place for readability.
- **Downstream pipelines** (CSV export, PDF rendering, mail merge) that expect a single consolidated value per cell rather than an expanded range.
- **Cross-platform compatibility**, where some consumers cannot tolerate arrays that bleed across multiple cells.

### **The Gap It Fills**
Without a built-in mechanism, developers would be forced to pre-process data in Python — joining lists into delimited strings before binding them to the workbook designer. This duplicates logic, complicates data models, and increases the chance of errors. The `arrayassingle` and `arraydelimiter` attributes eliminate this workaround by handling the formatting declaratively inside the Smart Marker itself.

## **Feature Benefits**
Using the `arrayassingle` and `arraydelimiter` attributes in your Smart Markers provides several advantages:
- **Single-cell containment**: All array elements are rendered into exactly one cell, keeping layouts compact and predictable.
- **Custom delimiter control**: Specify the separator you like — the default comma, a semicolon, a hyphen, a pipe, or a quoted multi-character string such as `" | "`.
- **Template-driven formatting**: No additional code is required to pre-process the data; formatting rules live inside the Smart Marker tag.
- **Cleaner reports**: Array data no longer pushes neighboring template content into different rows or columns.
- **Versatile data types**: Works with string lists and numeric lists supplied as JSON rows.
- **Backwards compatibility**: When the attributes are omitted, the original spreading behavior is preserved, so existing templates continue to work unchanged.

## **How to Use This Feature**

### **Smart Marker Syntax**
The `arrayassingle` and `arraydelimiter` attributes use Aspose.Cells' `name:value` attribute grammar inside the parentheses of a standard Smart Marker. The general syntax is:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

The marker is composed of the following parts:
- `&=DataSource.ArrayField` — the standard Smart Marker referencing the array field on the bound data source.
- `arrayassingle:true` — instructs the engine to render the whole array into a single cell instead of spreading the elements.
- `arraydelimiter:;` — optional; defines the separator placed between array elements. When it is omitted, a comma is used.

{{% alert color="warning" %}}
Write attributes in `name:value` form (a colon, not an equals sign) and separate multiple attributes with a comma **without spaces**. A space after the comma shifts the parsed value by one character — `(arrayassingle:true, arraydelimiter:;)` would join with the erroneous separator `:;` instead of `;`.
{{% /alert %}}

### **Delimiter Forms**
- A single character follows the colon directly: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- A multi-character separator is written in double quotes: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Step-by-Step Workflow**
The following workflow describes how to render an array into a single cell using Smart Markers.
1. **Prepare the data source**: Arrange each record as a JSON object whose field holds an array, for example `{"Tags": ["C#", "Aspose"]}`. Plain Python class instances, dictionaries, and lists passed to `set_data_source` do not bind array fields on this platform — JSON rows are the supported tabular form.
2. **Create a designer workbook**: Create a new `Workbook`, add a header row, and place a Smart Marker cell that references the array field with the `arrayassingle` attribute (and `arraydelimiter` when a custom separator is needed).
3. **Instantiate the WorkbookDesigner**: Create a `WorkbookDesigner` around the workbook and attach your JSON rows with `set_json_data_source`.
4. **Process the markers**: Call the `WorkbookDesigner.process()` method to expand the Smart Markers and populate the workbook with real data.
5. **Save the result**: Save the resulting workbook to disk in XLSX or any other supported file format.

### **Code Example 1 — Basic String Array Rendering**

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

The example prints the joined value of the whole array. The four tags land in one cell, separated by the default comma:

```
C#,Aspose,SmartMarker,Excel
```

### **Code Example 2 — Numeric Array with a Custom Delimiter**

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

JSON numbers join exactly like strings — each element keeps its plain numeric text:

```
95-88-76-100-67
```

### **Code Example 3 — Comparing Default vs. Single-Cell Rendering**

```python
import aspose.cells as ac
workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

The default marker fills one cell per element down column B, while the `arrayassingle` marker collapses the same array into a single cell in column C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notes & Best Practices**
Keep the following points in mind when working with the `arrayassingle` and `arraydelimiter` attributes:
- Attribute values use the `name:value` form. An equals-sign form such as `arrayassingle=true` is not recognized and silently falls back to the default spreading behavior.
- Separate attributes with a comma and no spaces; a space after the comma shifts the delimiter value by one character (see the warning above).
- The `arraydelimiter` value may be a single character written directly after the colon, or a multi-character string wrapped in double quotes.
- When `arraydelimiter` is omitted, elements are joined with a comma.
- Supply array fields through `set_json_data_source` row objects. Plain Python objects and dictionaries passed to `set_data_source` do not bind on this platform, and a custom `ICellsDataTable` whose column returns a Python list renders the list's container text instead of joining the elements.
- JSON numbers keep their plain integer form in the joined output.

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET](/cells/python-net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET](/cells/python-net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/python-net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Python via .NET](/cells/python-net/convert-sparkline-to-image-and-html/)
- [Converting Excel to OFD Format](/cells/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}