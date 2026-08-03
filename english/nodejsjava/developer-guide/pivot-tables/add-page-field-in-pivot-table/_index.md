---
title: Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java
description: Learn how to add and configure filter fields in pivot tables using Aspose.Cells for Node.js via Java, including adding filter fields, single-select filtering, and multi-select filtering.
keywords: Aspose.Cells, Node.js via Java, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /nodejs-java/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Add Filter Fields
---


{{% alert color="primary" %}}
Aspose.Cells supports the full lifecycle of filter fields in pivot tables. You can add a filter field through a high-level convenience API or through the lower-level `PageFields` collection, and you can drive the filter in single-select mode, clear it to show every filter item, or switch the field to multi-select so users can pick several filter items at once through the checkbox UI in Excel.
{{% /alert %}}

## **Introduction**

A filter field is a pivot field that controls *which subset* of the source data the pivot body displays. End users see it as a dropdown at the top of a rendered pivot in Excel, and selecting one of the available filter items rebuilds the pivot body so that only the records belonging to that filter item are summarized. A pivot field becomes a filter field when it is registered as `PivotFieldType.Page` rather than `PivotFieldType.Row`, `PivotFieldType.Column`, or `PivotFieldType.Data`.

## **Adding a Filter Field**

### Adding a Filter Field with addFieldToArea

The following example builds a small Fruit / Year / Amount dataset, places a pivot table at cell E3 with `Fruit` on the row area, `Amount` on the data area, and `Year` on the filter area, refreshes the pivot, and saves the workbook.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Populate 9 rows of sample data: Fruit, Year, Amount
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Add a pivot table anchored at cell E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Refresh and calculate the pivot table data
pivotTable.calculateData();

// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### Adding a Filter Field with getPageFields().add

When you already work with a `PivotField` instance, you can pass it directly to `pivotTable.getPageFields().add`. The pivot table and filter field are constructed exactly as in the previous scenario; only the final filter-area registration is replaced with the lower-level API call.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Add pivot table at E3 covering A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Single-Select Filtering (Showing One Filter Item)**

In the default single-select behavior, the filter field renders as a single dropdown and the `PivotField.CurrentPageItem` integer selects which filter item drives the pivot body. Assigning a specific index picks that one item; assigning the special sentinel `0x7FFD` (decimal 32765) clears the filter so every filter item is summarized at once. Single-select is the default; you do not need to enable it explicitly.

### Showing All Items

Setting `CurrentPageItem` to the magic value `0x7FFD` is equivalent to clearing the filter, the pivot body summarizes every filter item as if no filter were applied.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Create pivot table at E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Showing One Specific Item

Setting `CurrentPageItem` to a real index picks just that one filter item. The index is the position of the item in the filter field's sorted item list, so for example `1` selects the second item after sorting.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Add sample data (Fruit/Year/Amount)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// Add pivot table at E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = second item in sorted order (e.g. "2021")

// Refresh and calculate pivot table
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Multi-Select Filtering**

Multi-select filtering turns the filter dropdown into a checkbox list and lets the end user pick several filter items simultaneously. Aspose.Cells exposes two properties that work together. `PivotField.IsMultipleItemSelectionAllowed` must be set to `true` before the multi-select UI takes effect at all. After it is enabled, `PivotItem.IsHidden` controls which items appear in the checkbox list, so you can either show every item or whitelist only specific items.

```javascript
const AsposeCells = require("aspose.cells");

// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Part A — select ALL items (make every item visible)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Part B — select only specific items by source value
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Note:** When using multi-select filtering through `PivotItem.IsHidden`, **at least one `PivotItem` must remain visible** (`IsHidden == false`). If every item is hidden, Excel either crashes when opening the file or renders a blank pivot. Always verify that your multi-select whitelist includes at least one item from your source data.

## **Which API and Which Mode Should I Use?**

The table below summarizes when to use each API and mode so you can pick the right combination without reading every scenario in detail.

| Scenario / Use Case | Recommended API | Property Used | Notes |
|---|---|---|---|
| Add a filter field by source-column name (most common) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | High-level, one-line. Use this unless you need a `PivotField` reference. |
| Add a filter field when you already have a `PivotField` object | `pivotTable.getPageFields().add(PivotField)` | n/a | Use when the field object was obtained elsewhere or needs to be reused. |
| Filter to a single filter item (default mode) | `PivotField.CurrentPageItem` | set to a specific index | For example, `1` shows the second item in the sorted list. |
| Show all items / clear the filter | `PivotField.CurrentPageItem` | set to `0x7FFD` | The magic value `0x7FFD` (decimal 32765) is the sentinel for "all items". |
| Enable multi-select UI in Excel | `PivotField.IsMultipleItemSelectionAllowed` | set to `true` | Required before any `IsHidden` calls take effect. |
| Hide / show individual items in a multi-select list | `PivotItem.IsHidden` | set per item | At least one item must remain visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Always remember the visibility constraint when configuring multi-select filtering. If every `PivotItem` in a multi-select filter field is hidden, Excel crashes on open or renders a blank pivot. Build your whitelist against your source data so at least one item stays visible, and your saved workbooks will open reliably on every machine.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-java" >}}
