---
title: Insert a Picture based on Cell Reference
type: docs
weight: 90
url: /java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}} 

Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells supports this feature (Microsoft Excel 2010).

{{% /alert %}} 
### **Inserting a Picture Based on Cell Reference**
Aspose.Cells supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes to the data automatically appear in the graphic object. Add a picture to the worksheet by calling the [addPicture](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#addPicture\(int,%20int,%20int,%20int,%20java.io.InputStream\)) method of the [ShapeCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/ShapeCollection) collection (encapsulated in the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) object). Specify the cell range by using the [setFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/picture#Formula) method of the [Picture](https://apireference.aspose.com/java/cells/com.aspose.cells/Picture) object.

Below is a screenshot of the file the code below generates.

**Inserting a picture based on cell reference** 

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)
#### **Code Example**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
