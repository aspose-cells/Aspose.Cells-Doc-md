---
title: Updating Slicer with Golang via C++
linktitle: Updating Slicer
type: docs
weight: 50
url: /go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: This article shows how to update a slicer to filter the data of the linked pivot table or table using the Aspose.Cells for Go via C++ API.
keywords: Aspose.Cells Go via C++ Update slicer, Go how to change the slicer, how to filter a pivot table by slicer in Go, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Possible Usage Scenarios**
Updating a slicer means filtering the data of the pivot table or table that the slicer is connected to. When you select or unselect slicer items in Microsoft Excel, the linked pivot table or table is recalculated accordingly. With Aspose.Cells for Go via C++, you do not need to iterate the slicer cache items and refresh the slicer manually — the [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) method updates the slicer and recalculates the linked pivot table or table directly from the filter items:
- `Slicer.SelectItems(labels, append)` — selects the specified labels and recalculates the linked pivot table or table. When `append` is `true`, the originally selected labels are kept and the specified labels are added to the selection; when `append` is `false`, all original selections are cleared and only the specified labels stay selected.
- `Slicer.UnselectItems(labels)` — unselects part of the currently selected items.
- `Slicer.ClearFilter()` — removes the filter and selects all items.

{{% alert color="primary" %}}
Starting from Aspose.Cells for Go via C++ 26.10, the `SlicerCacheItem.Selected` property becomes read-only and its setter is no longer supported. Use the `Slicer.SelectItems`, `Slicer.UnselectItems`, and `Slicer.ClearFilter` methods instead of setting `SlicerCacheItem.Selected` item by item.
{{% /alert %}}

## **How to Update Slicer**
The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer connected to a pivot table. It selects only the "Blue" and "Pink" items of the slicer with `Slicer.SelectItems(labels, false)` — the pivot table is recalculated directly from the filter items, without a manual `Slicer.Refresh()` call. It then saves the workbook as the [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the pivot table shows only the filtered items.
![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**
Replace the current selection (only the specified labels stay selected) and recalculate the linked pivot table or table:

```go
package main
import (
    "fmt"
    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")
    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)
    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)
    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)
    // Save the modified workbook.
    wb.Save_String("out.xlsx")
    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

Keep the currently selected labels and additionally select more items:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Unselect part of the selected items:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Remove the filter (select all items):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}