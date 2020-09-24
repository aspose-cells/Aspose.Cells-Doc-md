---
title: Managing Pictures
type: docs
weight: 40
url: /java/managing-pictures/
---

{{% alert color="primary" %}}

Aspose.Cells allows developers to add pictures to spreadsheets at runtime. Moreover, the positioning of these pictures can be controlled at runtime, which is discussed in more detail in the coming sections.

Aspose.Cells for Java only supports image formats: BMP, JPEG, PNG, GIF.

Indexes used in examples start from 0.

{{% /alert %}}

## **Adding Pictures**

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code.

Simply call the [**add**](https://apireference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) method of the [**Pictures**](https://apireference.aspose.com/cells/java/com.aspose.cells/PictureCollection) collection (encapsulated in the [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) object). The [**add**](https://apireference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) method takes the following parameters:

- **Upper left row index**, the index of the upper left row.
- **Upper left column index**, the index of the upper left column.
- **Image file name**, the name of the image file, complete with path.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Positioning of Pictures**

Pictures can be positioned using Aspose.Cells as follows:

- [Absolute Positioning](/cells/java/managing-pictures/#absolute-positioning).

### **Absolute Positioning**

Developers can position the pictures absolutely by using the [**setUpperDeltaX**](https://apireference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) and [**setUpperDeltaY**](https://apireference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) methods of the [**Picture**](https://apireference.aspose.com/cells/java/com.aspose.cells/Picture) object.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}
