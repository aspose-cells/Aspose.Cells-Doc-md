+++
title = "Managing Pictures" 
description = "" 
weight = 12221 
+++

Aspose.Cells for Java : Managing Pictures  

# Aspose.Cells for Java : Managing Pictures



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Pictures](#ManagingPictures-AddingPictures)
*   2 [Positioning of Pictures](#ManagingPictures-PositioningofPictures)
    *   2.1 [Absolute Positioning](#ManagingPictures-AbsolutePositioning)
{{< /panel >}}
 

Aspose.Cells allows developers to add pictures to spreadsheets at runtime. Moreover, the positioning of these pictures can be controlled at runtime, which is discussed in more detail in the coming sections.

Aspose.Cells for Java only supports image formats: BMP, JPEG, PNG, GIF.

Indexes used in examples start from 0.

### Adding Pictures

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code.

Simply call the [add](https://apireference.aspose.com/java/cells/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) method of the [Pictures](https://apireference.aspose.com/java/cells/com.aspose.cells/PictureCollection) collection (encapsulated in the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) object). The [add](https://apireference.aspose.com/java/cells/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) method takes the following parameters:

*   **Upper left row index**, the index of the upper left row.
*   **Upper left column index**, the index of the upper left column.
*   **Image file name**, the name of the image file, complete with path.

### Positioning of Pictures

Pictures can be positioned using Aspose.Cells as follows:

*   [Absolute Positioning](https://docs2.aspose.com/cells/java/developerguide/drawingobjects/managing+pictures).

#### Absolute Positioning

Developers can position the pictures absolutely by using the [setUpperDeltaX](https://apireference.aspose.com/java/cells/com.aspose.cells/picture#UpperDeltaX) and [setUpperDeltaY](https://apireference.aspose.com/java/cells/com.aspose.cells/picture#UpperDeltaY) methods of the [Picture](https://apireference.aspose.com/java/cells/com.aspose.cells/Picture) object.

