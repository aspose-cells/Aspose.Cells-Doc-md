---
title: Updating Slicer with Golang via C++
linktitle: Updating Slicer
type: docs
weight: 50
url: /go-cpp/updating-slicer/
description: This article shows how to update linked pivot tables by updating slicer using the Aspose.Cells for C++ API.
keywords: Aspose.Cells C++ Update slicer, C++ how to change the slicer, how to adjust the slicer in C++, how to select or unselect the slicer items.
---

## **Possible Usage Scenarios**

If you want to update a slicer in Microsoft Excel, select or unselect its items, it will then update the slicer table or pivot table accordingly. Please use [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) to select or unselect slicer items with Aspose.Cells and then call [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) method to update the slicer table or pivot table.

## **How to Update Slicer**

The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer. It unselects the 2nd and 3rd items of the slicer and refreshes the slicer. It then saves the workbook as [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, refreshing the slicer with selected items has also refreshed the pivot table accordingly.

![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}