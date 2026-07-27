---
title: Add Filter Fields to a Pivot Table in Aspose.Cells for .NET
description: Learn how to add and configure filter fields in pivot tables using Aspose.Cells for .NET, including adding filter fields, single-select filtering, and multi-select filtering.
keywords: Aspose.Cells, .NET, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Add Filter Fields
---


{{% alert color="primary" %}}
Aspose.Cells supports the full lifecycle of filter fields in pivot tables. You can add a filter field through a high-level convenience API or through the lower-level `PageFields` collection, and you can drive the filter in single-select mode, clear it to show every filter item, or switch the field to multi-select so users can pick several filter items at once through the checkbox UI in Excel.
{{% /alert %}}

## **Introduction**

A filter field is a pivot field that controls *which subset* of the source data the pivot body displays. End users see it as a dropdown at the top of a rendered pivot in Excel, and selecting one of the available filter items rebuilds the pivot body so that only the records belonging to that filter item are summarized. A pivot field becomes a filter field when it is registered as `PivotFieldType.Page` rather than `PivotFieldType.Row`, `PivotFieldType.Column`, or `PivotFieldType.Data`.

## **Adding a Filter Field**

### Adding a Filter Field with AddFieldToArea

The following example builds a small Fruit / Year / Amount dataset, places a pivot table at cell E3 with `Fruit` on the row area, `Amount` on the data area, and `Year` on the filter area, refreshes the pivot, and saves the workbook.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Set up the header row
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Populate 9 rows of sample data: Fruit, Year, Amount
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// Add a pivot table anchored at cell E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Refresh and calculate the pivot table data
pivotTable.CalculateData();

// Save the workbook
workbook.Save("pageFieldSample.xlsx");
```

### Adding a Filter Field with PageFields.Add

When you already work with a `PivotField` instance, you can pass it directly to `PivotTable.PageFields.Add`. The pivot table and filter field are constructed exactly as in the previous scenario; only the final filter-area registration is replaced with the lower-level API call.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add — the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Headers
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// Sample data (9 rows)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// Add pivot table at E3 covering A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Refresh so the new page field is reflected in the saved workbook
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Single-Select Filtering (Showing One Filter Item)**

In the default single-select behavior, the filter field renders as a single dropdown and the `PivotField.CurrentPageItem` integer selects which filter item drives the pivot body. Assigning a specific index picks that one item; assigning the special sentinel `0x7FFD` (decimal 32765) clears the filter so every filter item is summarized at once. Single-select is the default; you do not need to enable it explicitly.

### Showing All Items

Setting `CurrentPageItem` to the magic value `0x7FFD` is equivalent to clearing the filter: the pivot body summarizes every filter item as if no filter were applied.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // Create a new workbook
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Populate Fruit/Year/Amount data
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // Create pivot table at E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.CalculateData();

        // Clear the page filter so every item in the page field is visible.
        // 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
        // equivalent to selecting "(All)" in Excel's page-field dropdown.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### Showing One Specific Item

Setting `CurrentPageItem` to a real index picks just that one filter item. The index is the position of the item in the filter field's sorted item list, so for example `1` selects the second item after sorting.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Add sample data (Fruit/Year/Amount)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// Add pivot table at E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Page-field-specific operations
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")

// Refresh and calculate pivot table
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Multi-Select Filtering**

Multi-select filtering turns the filter dropdown into a checkbox list and lets the end user pick several filter items simultaneously. Aspose.Cells exposes two properties that work together. `PivotField.IsMultipleItemSelectionAllowed` must be set to `true` before the multi-select UI takes effect at all. After it is enabled, `PivotItem.IsHidden` controls which items appear in the checkbox list, so you can either show every item or whitelist only specific items.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Sample data: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — Enable multi-select on the page field
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// Part A — select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// Part B — select only specific items by source value
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **Note:** When using multi-select filtering through `PivotItem.IsHidden`, **at least one `PivotItem` must remain visible** (`IsHidden == false`). If every item is hidden, Excel either crashes when opening the file or renders a blank pivot. Always verify that your multi-select whitelist includes at least one item from your source data.

## **Which API and Which Mode Should I Use?**

The table below summarizes when to use each API and mode so you can pick the right combination without reading every scenario in detail.

| Scenario / Use Case | Recommended API | Property Used | Notes |
|---|---|---|---|
| Add a filter field by source-column name (most common) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | High-level, one-line. Use this unless you need a `PivotField` reference. |
| Add a filter field when you already have a `PivotField` object | `PivotTable.PageFields.Add(PivotField)` | n/a | Use when the field object was obtained elsewhere or needs to be reused. |
| Filter to a single filter item (default mode) | `PivotField.CurrentPageItem` | set to a specific index | For example, `1` shows the second item in the sorted list. |
| Show all items / clear the filter | `PivotField.CurrentPageItem` | set to `0x7FFD` | The magic value `0x7FFD` (decimal 32765) is the sentinel for "all items". |
| Enable multi-select UI in Excel | `PivotField.IsMultipleItemSelectionAllowed` | set to `true` | Required before any `IsHidden` calls take effect. |
| Hide / show individual items in a multi-select list | `PivotItem.IsHidden` | set per item | At least one item must remain visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Always remember the visibility constraint when configuring multi-select filtering. If every `PivotItem` in a multi-select filter field is hidden, Excel crashes on open or renders a blank pivot. Build your whitelist against your source data so at least one item stays visible, and your saved workbooks will open reliably on every machine.
{{% /alert %}}




## **Related Articles**

- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/net/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
