---
title: ArrayAsSingle  ExtraDelimiter | SmartMarker Single Cell Array Rendering
linktitle: Array As Single Cell
type: docs
weight: 60
url: /net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 1. Why This Feature Is Needed

By default, when Aspose.Cells SmartMarkers parse JSON array data, the array elements will be automatically expanded and rendered into**multiple rows** in the Excel worksheet.

However, many business scenarios require retaining the complete array structure without row splitting or line breaking. Users often need to render the entire simple array or object array into **a single cell** for data archiving, downstream system parsing, and original data retention.

To meet this requirement, we have extended two new SmartMarker parameters: **ArrayAsSingle** and **ExtraDelimiter**. These parameters eliminate the default row-splitting behavior and support aggregating all array elements into one single cell.

## 2. Feature Benefits

This enhanced SmartMarker capability overrides the default array expansion logic and provides the following core values:

- **Aggregate array data in one cell**: Both simple arrays and nested object arrays can be fully aggregated into a single cell without row breaking, maintaining complete data integrity and correlation.

- **Support two mainstream array types**: Compatible with plain value arrays for direct splicing and nested object arrays for extracting specified child fields, covering all common business array structures.

- **Customizable delimiter support**: Users can customize comma, line break, vertical bar and other separators to freely control the display format of array elements.

- **Template-driven, zero-code modification**: Enable aggregation by simply adding parameters in the SmartMarker template, without changing business code or preprocessing JSON data.

- **Flexible output format**: Plain arrays support direct aggregation, while object arrays can extract only required fields to generate clean and readable Excel reports.

## 3. How to Use This Feature

You can enable array single-cell aggregation by appending the corresponding parameters to standard SmartMarker tags. Parameters can be freely combined to adapt to all JSON array fields.

### 3.1 Core Parameter Description

- **ArrayAsSingle**: Applies to **simple value arrays**. Disables default row-splitting behavior and concatenates all array elements into one cell with comma separators by default.

- **ArrayAsSingle:FieldName**: Applies to **nested object arrays**. Specify the target child field name inside array objects. The engine will automatically traverse all sub-objects, extract the specified field values, and aggregate them into a single cell.

- **ExtraDelimiter**: Custom separator for concatenating array elements. Defaults to English comma **,** if not specified. Supports vertical bar, line break, space and custom symbols.

### 3.2 Common SmartMarker Syntax Examples

- **1. Simple array aggregation (default comma separator)**

      JSON Data: `SizeRange: [L, M, S, XL]`

      Marker Syntax: `=node.SizeRange(ArrayAsSingle)`

      Output Result: `L, M, S, XL`

- **2. Simple array with custom vertical bar separator**

      Marker Syntax: `=node.SizeRange(ArrayAsSingle,ExtraDelimiter:|)`

      Output Result: `L|M|S|XL`

- **3. Simple array with line break separator**

      Marker Syntax: `=node.SizeRange(ArrayAsSingle,ExtraDelimiter:n)`

      Output Result: Each element (L, M, S, XL) displays on a new line inside the cell

- **4. Extract specified fields from object arrays (core scenario)**

      JSON Data:
{
SizeRange: [
    { Size: L, Code: 1 },
    { Size: M, Code: 2 },
    { Size: S, Code: 3 },
    { Size: XL, Code: 4 }
]
}

      Marker Syntax: `=node.SizeRange(ArrayAsSingle:Size)`

      Output Result: `L, M, S, XL`

### 3.3 Full Runnable C# Code Examples

The following code covers **2D nested simple arrays** and **object arrays**. You can directly copy and run in your project:

#### Scenario 1: 2D Nested Simple Array

```Plain Text
// Initialize a new workbook template
Workbook w = new Workbook();
// Write SmartMarker tag in target cell
w.Worksheets[0].Cells["A1"].PutValue("&=node.SizeRange(ArrayAsSingle)");
WorkbookDesigner designer = new WorkbookDesigner(w);
// Bind 2D nested array JSON data
string json = "{"node": {"SizeRange": [["L","M"],["S","XL"]]}}";
designer.SetJsonDataSource(null, json);
// Process SmartMarker and aggregate array into single cell
designer.Process();
// Output result: L,M,S,XL
```

#### Scenario 2: Extract Specified Field from Object Array

```Plain Text
// Initialize a new workbook template
Workbook w = new Workbook();
// Extract "Size" field from all nested objects
w.Worksheets[0].Cells["A1"].PutValue("&=node.SizeRange(ArrayAsSingle:Size)");
WorkbookDesigner designer = new WorkbookDesigner(w);
// Bind object array JSON data
string json = "{"node": {"SizeRange": [{"Size":"L","Code":1},{"Size":"M","Code":2},{"Size":"S","Code":3},{"Size":"XL","Code":4}]}}";
designer.SetJsonDataSource(null, json);
// Process SmartMarker and aggregate field values
designer.Process();
// Output result: L, M, S, XL

```
