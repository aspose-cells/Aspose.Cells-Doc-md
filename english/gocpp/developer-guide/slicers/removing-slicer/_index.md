---
title: Removing Slicer with Golang via C++
linktitle: Removing Slicer
type: docs
weight: 30
url: /go-cpp/removing-slicer/
description: Learn how to remove slicers in Excel files programmatically using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

If you want to remove a slicer in Microsoft Excel, just select it and press the *Delete* button. Similarly, if you want to remove it using Aspose.Cells API programmatically, please use the [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/go-cpp/slicercollection/remove/) method. It will remove the slicer from the worksheet.

## **Removing Slicer**

The following sample code loads the [sample Excel file](67338478.xlsx) that contains an existing slicer. It accesses the slicers and then removes it. Finally, it saves the workbook as [output Excel file](67338477.xlsx). The following screenshot shows the slicer that will be removed after the execution of the sample code.

![todo:image_alt_text](removing-slicer_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingSlicer.go" >}}