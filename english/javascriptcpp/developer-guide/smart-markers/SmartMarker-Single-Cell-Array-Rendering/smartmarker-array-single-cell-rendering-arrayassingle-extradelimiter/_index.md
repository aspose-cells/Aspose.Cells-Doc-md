---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells for JavaScript via C++
description: Learn how to render array data into a single cell using the ArrayAsSingle and ExtraDelimiter attributes in Smart Markers with Aspose.Cells for JavaScript via C++.
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells
url: /javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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
When a Smart Marker references an array property, Aspose.Cells expands the array across multiple cells by default. For example, a marker such as `&=Product.Tags` against an array containing four strings will place each value into its own cell, pushing other template content outward and potentially breaking carefully designed report layouts.

### **Use Case Limitations**
There are many practical scenarios where the default spreading behavior is undesirable:
- **Summary-style reports** that need a compact one-row-per-record layout.
- **Tag, label, or keyword lists** that need to be displayed as comma-separated or pipe-separated values within a single cell.
- **Filter chips or status indicators** that group multiple values in one place for readability.
- **Downstream pipelines** (CSV export, PDF rendering, mail merge) that expect a single consolidated value per cell rather than an expanded range.
- **Cross-platform compatibility**, where some consumers cannot tolerate arrays that bleed across multiple cells.

### **The Gap It Fills**
Without a built-in mechanism, developers would be forced to pre-process data in JavaScript — joining arrays into delimited strings before binding them to the workbook designer. This duplicates logic, complicates data models, and increases the chance of errors. The `ArrayAsSingle` and `ExtraDelimiter` attributes eliminate this workaround by handling the formatting declaratively inside the Smart Marker itself.

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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
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
1. **Prepare the data source**: Create an object (or data structure) that exposes a property returning an array. The property can return an array of strings, numbers, or any other supported value type.
2. **Create a designer workbook**: Create a new `Workbook`, add a header row, and place a Smart Marker cell that references the array property with the `arrayasSingle` and `extraDelimiter` attributes.
3. **Instantiate the WorkbookDesigner**: Create a `WorkbookDesigner` object, attach the designer workbook to it, and bind your data source using the `setDataSource` method.
4. **Process the markers**: Call the `workbookDesigner.process()` method to expand the Smart Markers and populate the workbook with real data.
5. **Save the result**: Save the resulting workbook to disk in XLSX or any other supported file format.

### **Code Example 1 — Basic String Array Rendering**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Section 1: Default Smart Marker - values spread horizontally across cells
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Bind the data source and process Smart Markers
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Save the resulting workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

### **Notes & Best Practices**
Keep the following points in mind when working with the `ArrayAsSingle` and `ExtraDelimiter` attributes:
- The `extraDelimiter` value is treated as a string literal; escape any special characters that your template processor might interpret.
- The `arrayasSingle` attribute accepts a boolean value (`true` / `false`). Only `true` triggers the single-cell behavior; any other value falls back to the default spreading behavior.
- If the array is empty or null, the cell is left empty (or contains a blank string depending on the data type).
- The feature works with object data sources as well as tabular data sources where a column can be split into arrays.
- For newline-separated output, use `\n` as the delimiter value.

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for JavaScript via C++](/cells/javascript-cpp/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for JavaScript via C++](/cells/javascript-cpp/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/javascript-cpp/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for JavaScript via C++](/cells/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Converting Excel to OFD Format](/cells/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}