---
title: Insert a Picture Based on Cell Reference with Golang via C++
linktitle: Insert a Picture Based on Cell Reference
type: docs
weight: 150
url: /go-cpp/insert-a-picture-based-on-cell-reference/
description: Learn how to insert a picture based on cell reference using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells supports this feature (Microsoft Excel 2010).

{{% /alert %}}

## Inserting a Picture Based on Cell Reference

Aspose.Cells supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object. Add a picture to the worksheet by calling the [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) method of the [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) object). Specify the cell range by using the [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) attribute of the [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object.

### Code Example

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}