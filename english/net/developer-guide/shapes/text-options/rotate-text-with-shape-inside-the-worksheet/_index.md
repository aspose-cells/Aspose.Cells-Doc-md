---
title: Rotate Text with Shape inside the Worksheet
type: docs
weight: 1300
url: /net/rotate-text-with-shape-inside-the-worksheet/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

You can add text inside any shape using Microsoft Excel. If you add a shape using the very old Microsoft Excel 2003, then the text will not rotate with the shape. But if you add a shape using newer versions of Microsoft Excel, e.g., 2007, 2010, 2013, or 2016, etc., then the text will rotate with the shape. You can control whether the text should rotate with the shape using the [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) property. The default value is **true**, which means the text will rotate with the shape, but if you set it to **false**, the text will not rotate with the shape.

## **Rotate Text with Shape inside the Worksheet**

The following sample code loads the [sample Excel file](64716896.xlsx) that has a triangle shape whose text rotates with the shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) property to **false** and saves it as the [output Excel file](64716897.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on the sample Excel file for reference.

![rotate-text-with-shape-inside-the-worksheet_1.png](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
