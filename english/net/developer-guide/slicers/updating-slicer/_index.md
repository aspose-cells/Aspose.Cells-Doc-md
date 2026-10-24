---
title: Updating Slicer
linktitle: Updating Slicer
type: docs
weight: 50
url: /net/updating-slicer/
description: This article shows how to update a slicer to filter the data of the linked pivot table or table using the Aspose.Cells for .NET API.
keywords: Aspose.Cells C# Update slicer, C# how to change the slicer, how to filter a pivot table by slicer in C#, C# Slicer SelectItems, C# Slicer ClearFilter, C# Slicer UnselectItems.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Updating a slicer means filtering the data of the pivot table or table that the slicer is connected to. When you select or unselect slicer items in Microsoft Excel, the linked pivot table or table is recalculated accordingly. With Aspose.Cells for .NET, you do not need to iterate the slicer cache items and refresh the slicer manually — the [**Slicer.SelectItems(string[], bool)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/selectitems/) method updates the slicer and recalculates the linked pivot table or table directly from the filter items:
- `Slicer.SelectItems(labels, append)` — selects the specified labels and recalculates the linked pivot table or table. When `append` is `true`, the originally selected labels are kept and the specified labels are added to the selection; when `append` is `false`, all original selections are cleared and only the specified labels stay selected.
- `Slicer.UnselectItems(labels)` — unselects part of the currently selected items.
- `Slicer.ClearFilter()` — removes the filter and selects all items.

{{% alert color="primary" %}}
Starting from Aspose.Cells for .NET 26.10, the `SlicerCacheItem.Selected` property becomes read-only and its setter is no longer supported. Use the `Slicer.SelectItems`, `Slicer.UnselectItems`, and `Slicer.ClearFilter` methods instead of setting `SlicerCacheItem.Selected` item by item.
{{% /alert %}}

## **How to Update Slicer**
The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer connected to a pivot table. It selects only the "Blue" and "Pink" items of the slicer with `Slicer.SelectItems(labels, false)` — the pivot table is recalculated directly from the filter items, without a manual `Slicer.Refresh()` call. It then saves the workbook as the [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the pivot table shows only the filtered items.
![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**
Replace the current selection (only the specified labels stay selected) and recalculate the linked pivot table or table:

```csharp
using Aspose.Cells;
using Aspose.Cells.Slicers;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.Worksheets[0];
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.Slicers[0];
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.SelectItems(new string[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.Save("out.xlsx");
```

Keep the currently selected labels and additionally select more items:

```csharp
// Keep the current selection and add "Red" to it.
slicer.SelectItems(new string[] { "Red" }, true);
```

Unselect part of the selected items:

```csharp
// Remove "Pink" from the current selection.
slicer.UnselectItems(new string[] { "Pink" });
```

Remove the filter (select all items):

```csharp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="csharp" >}}