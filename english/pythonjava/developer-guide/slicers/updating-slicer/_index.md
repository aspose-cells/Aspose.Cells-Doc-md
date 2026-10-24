---
title: Updating Slicer
linktitle: Updating Slicer
type: docs
weight: 60
url: /python-java/updating-slicer/
description: This article shows how to update a slicer to filter the data of the linked pivot table or table using the Aspose.Cells for Python via Java API.
keywords: Aspose.Cells for Python via Java Update slicer, Python Java update Slicer, how to filter a pivot table by slicer in Python, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Updating Slicer**
Updating a slicer means filtering the data of the pivot table or table that the slicer is connected to. Aspose.Cells for Python via Java updates the slicer and recalculates the linked pivot table or table directly from the filter items:
- `Slicer.selectItems(labels, append)` — selects the specified labels and recalculates the linked pivot table or table. When `append` is `True`, the originally selected labels are kept and the specified labels are added to the selection; when `append` is `False`, all original selections are cleared and only the specified labels stay selected.
- `Slicer.unselectItems(labels)` — unselects part of the currently selected items.
- `Slicer.clearFilter()` — removes the filter and selects all items.

{{% alert color="primary" %}}
Starting from Aspose.Cells for Python via Java 26.10, the `SlicerCacheItem.Selected` property becomes read-only and its setter is no longer supported. Use the `Slicer.selectItems`, `Slicer.unselectItems`, and `Slicer.clearFilter` methods instead of setting `SlicerCacheItem.Selected` item by item.
The following code snippet loads the [sample Excel file](106365050.xlsx) that contains a slicer connected to a pivot table. It selects only the "Blue" and "Pink" items of the slicer with `Slicer.selectItems(labels, False)` — the pivot table is recalculated directly from the filter items, without a manual `Slicer.refresh()` call. It then saves the workbook as the [output Excel file](106365051.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the pivot table shows only the filtered items.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Sample Code**
Replace the current selection (only the specified labels stay selected) and recalculate the linked pivot table or table:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Keep the currently selected labels and additionally select more items:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Unselect part of the selected items:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Remove the filter (select all items):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}