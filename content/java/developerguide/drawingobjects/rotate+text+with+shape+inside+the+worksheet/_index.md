---
title : "Rotate Text with Shape inside the Worksheet" 
description : "" 
weight : 12228 
toc : false
type: docs
url: /java/developerguide/drawingobjects/rotate+text+with+shape+inside+the+worksheet/
---

# Aspose.Cells for Java : Rotate Text with Shape inside the Worksheet


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Rotate Text with Shape inside the Worksheet](#rotate-text-with-shape-inside-the-worksheet)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

You can add text inside any shape using Microsoft Excel. If you add shape using the very old Microsoft Excel 2003, then the text will not rotate with shape. But if you add shape using newer versions of Microsoft Excel e.g. 2007, 2010, 2013 or 2016, etc. then the text will rotate with shape. You can control if the text should rotate with the shape or not using the [ShapeTextAlignment.RotateTextWithShape](https://apireference.aspose.com/java/cells/com.aspose.cells/shapetextalignment#RotateTextWithShape) property. The default value of it is **true **which means text will rotate with shape but if you set it as **false**, then the text will not rotate with shape.

## Rotate Text with Shape inside the Worksheet

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/64456361/64716919.xlsx) that has a triangle shape and its text rotates with shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [ShapeTextAlignment.RotateTextWithShape](https://apireference.aspose.com/java/cells/com.aspose.cells/shapetextalignment#RotateTextWithShape) property as **false **and saves it as [output Excel file](https://docs2.aspose.com/cells/java/attachments/64456361/64716917.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on sample Excel file for a reference.

![](https://docs2.aspose.com/cells/java/attachments/64456361/64716918.png)

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputRotateTextWithShape.xlsx](https://docs2.aspose.com/cells/java/attachments/64456361/64716917.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleRotateTextWithShape.xlsx](https://docs2.aspose.com/cells/java/attachments/64456361/64716919.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Rotate-Text-With-Shape.png](https://docs2.aspose.com/cells/java/attachments/64456361/64716918.png) (image/png)  

