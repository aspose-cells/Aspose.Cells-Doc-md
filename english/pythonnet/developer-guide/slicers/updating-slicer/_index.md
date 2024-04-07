---
title: Updating Slicer
type: docs
weight: 50
url: /python-net/updating-slicer/
description: Learn how to update slicer with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Python update Slicer without Excel, Update Slicer using Aspose.Cells for Python.
---

## **Possible Usage Scenarios**

If you want to update slicer in Microsoft Excel, select or unselect its items, it will then update the slicer table or pivot table accordingly. Please use [**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/) to select or unselect slicer items with Aspose.Cells for Python via .NET and then call [**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#) method to update the slicer table or pivot table.

## **How to Update Slicer Using Aspose.Cells for Python Excel Library**

The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer. It unselects the 2nd and 3rd items of the slicer and refreshes the slicer. It then saves the workbook as [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, refreshing the slicer with selected items has also refreshed the pivot table accordingly.

![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
