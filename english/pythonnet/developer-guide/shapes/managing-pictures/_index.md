---
title: Managing Pictures
type: docs
weight: 10
url: /python-net/managing-pictures/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for Python via .NET allows developers to add pictures to spreadsheets at runtime. Moreover, the positioning of these pictures can be controlled at runtime, which is discussed in more detail in the coming sections.

This article explains how to add pictures, and how to insert an image that shows the content of certain cells.

## **Adding Pictures**

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code:
Simply call the [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) method of the [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) object). The [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) method takes the following parameters:

- **Upper left row index**, the index of the upper left row.
- **Upper left column index**, the index of the upper left column.
- **Image file name**, the name of the image file, complete with path.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Positioning Pictures**

There are two possible ways to control the positioning of pictures using Aspose.Cells for Python via .NET:

- Proportional positioning: define a position proportional to the row height and width.
- Absolute positioning: define the exact position on the page where the image will be inserted, for example, 40 pixels to the left and 20pixels below the edge of the cell.

### **Proportional Positioning**

Developers can position the pictures proportional to row height and column width using the [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) and [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) properties of the [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object. A [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object can be obtained from the [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) collection by passing its picture index. This example places an image in the F6 cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Absolute Positioning**

Developers can also position the pictures absolutely by using the [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) and [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) properties of the [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object. This example places an image in cell F6, 60 pixels from the left and 10 pixels from the top of the cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Inserting a Picture Based on Cell Reference**

Aspose.Cells for Python via .NET lets you display the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell, or cell range, is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object.

Add a picture to the worksheet by calling the [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) method of the [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) object). Specify the cell range by using the [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) attribute of the [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Advance topics**
- [Add Conditional Icons Set with the Cell Text](/cells/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Insert a Linked Picture from Web Address](/cells/python-net/insert-a-linked-picture-from-web-address/)
- [Insert a Picture Based on Cell Reference](/cells/python-net/insert-a-picture-based-on-cell-reference/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="python-net" >}}
