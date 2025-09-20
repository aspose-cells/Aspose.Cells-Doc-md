---
title: Refresh Values of Linked Shapes with Golang via C++
linktitle: Refresh Values of Linked Shapes
type: docs
weight: 3200
url: /go-cpp/refresh-values-of-linked-shapes/
description: Learn how to refresh values of linked shapes in Excel files using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) method to refresh the value of the linked shape.

{{% /alert %}}

## Example

The following screenshot shows the source Excel file used in the sample code below. It has a linked picture linked to cells A1 to E4. We will change the value of cell B4 with Aspose.Cells and then call [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) method to refresh the value of the picture and save it in PDF format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

You can download the [source Excel file](95584291.xlsx) and the [output PDF](95584292.pdf) from the given links.

### C++ code to refresh the values of linked shapes

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}