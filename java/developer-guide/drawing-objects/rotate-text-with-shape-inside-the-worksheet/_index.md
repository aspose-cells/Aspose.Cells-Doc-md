---
title: Rotate Text with Shape inside the Worksheet
type: docs
weight: 110
url: /java/rotate-text-with-shape-inside-the-worksheet/
---

## **Possible Usage Scenarios**

You can add text inside any shape using Microsoft Excel. If you add shape using the very old Microsoft Excel 2003, then the text will not rotate with shape. But if you add shape using newer versions of Microsoft Excel e.g. 2007, 2010, 2013 or 2016, etc. then the text will rotate with shape. You can control if the text should rotate with the shape or not using the [**ShapeTextAlignment.RotateTextWithShape**](https://apireference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) property. The default value of it is **true** which means text will rotate with shape but if you set it as **false**, then the text will not rotate with shape.

## **Rotate Text with Shape inside the Worksheet**

The following sample code loads the [sample Excel file](64716919.xlsx) that has a triangle shape and its text rotates with shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [**ShapeTextAlignment.RotateTextWithShape**](https://apireference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) property as **false** and saves it as [output Excel file](64716917.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on sample Excel file for a reference.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Sample Code**

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
