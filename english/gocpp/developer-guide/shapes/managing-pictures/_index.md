---
title: Managing Pictures with Golang via C++
linktitle: Managing Pictures
type: docs
weight: 10
url: /go-cpp/managing-pictures/
description: Add, position, and manage images in spreadsheets using Aspose.Cells for Go via Go API.
---

Aspose.Cells allows developers to add pictures to spreadsheets at runtime. Moreover, the positioning of these pictures can be controlled at runtime, which is discussed in more detail in the coming sections.

This article explains how to add pictures and insert an image that shows the content of certain cells.

## **Adding Pictures**

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code:
Simply call the [**Add**](https://reference.aspose.com/cells/go-cpp/picturecollection/add_int_int_int_int_stream/) method of the [**PictureCollection**](https://reference.aspose.com/cells/go-cpp/picturecollection/) (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) object). The [**Add**](https://reference.aspose.com/cells/go-cpp/picturecollection/add_int_int_int_int_stream/) method takes the following parameters:

- **Upper left row index**, the index of the upper left row.
- **Upper left column index**, the index of the upper left column.
- **Image file name**, the name of the image file, complete with path.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingPictures.go" >}}

## **Positioning Pictures**

There are two possible ways to control the positioning of pictures using Aspose.Cells:

- Proportional positioning: define a position proportional to the row height and column width.
- Absolute positioning: define the exact position on the page where the image will be inserted, for example, 40 pixels to the left and 20 pixels below the edge of the cell.

### **Proportional Positioning**

Developers can position the pictures proportional to row height and column width using the [**UpperDeltaX**](https://reference.aspose.com/cells/go-cpp/shape/getupperdeltax/) and [**UpperDeltaY**](https://reference.aspose.com/cells/go-cpp/shape/getupperdeltay/) properties of the [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) object. A [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) object can be obtained from the [**PictureCollection**](https://reference.aspose.com/cells/go-cpp/picturecollection/) by passing its picture index. This example places an image in the F6 cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingPictures-1.go" >}}

### **Absolute Positioning**

Developers can also position the pictures absolutely by using the [**Left**](https://reference.aspose.com/cells/go-cpp/shape/getleft/) and [**Top**](https://reference.aspose.com/cells/go-cpp/shape/gettop/) properties of the [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) object. This example places an image in cell F6, 60 pixels from the left and 10 pixels from the top of the cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingPictures-2.go" >}}

## **Inserting a Picture Based on Cell Reference**

Aspose.Cells lets you display the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data you want to display. Since the cell—or cell range—is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object.

Add a picture to the worksheet by calling the [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) method of the [**ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) object). Specify the cell range by using the [**GetFormula**](https://reference.aspose.com/cells/go-cpp/picture/getformula/) property of the [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) object.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingPictures-3.go" >}}

## **Advanced topics**
- [Add Conditional Icons Set with the Cell Text](/cells/go-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insert a Linked Picture from Web Address](/cells/go-cpp/insert-a-linked-picture-from-web-address/)
- [Insert a Picture Based on Cell Reference](/cells/go-cpp/insert-a-picture-based-on-cell-reference/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/go-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="go" >}}
