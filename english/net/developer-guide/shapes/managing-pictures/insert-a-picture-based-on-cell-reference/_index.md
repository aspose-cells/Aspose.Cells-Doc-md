---
title: Insert a Picture Based on Cell Reference
type: docs
weight: 150
url: /net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells supports this feature (Microsoft Excel 2010).

{{% /alert %}}

## Inserting a Picture Based on Cell Reference

Aspose.Cells supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object. Add a picture to the worksheet by calling the [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) method of the [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) object). Specify the cell range by using the [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attribute of the [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) object.

### Code Example

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}