---
title: Insert a Picture Based on Cell Reference
type: docs
weight: 150
url: /python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells for Python via .NET supports this feature (Microsoft Excel 2010).

{{% /alert %}}

## Inserting a Picture Based on Cell Reference

Aspose.Cells for Python via .NET supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object. Add a picture to the worksheet by calling the [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) method of the [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) object). Specify the cell range by using the [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) attribute of the [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object.

### Code Example

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
{{< app/cells/assistant language="python-net" >}}