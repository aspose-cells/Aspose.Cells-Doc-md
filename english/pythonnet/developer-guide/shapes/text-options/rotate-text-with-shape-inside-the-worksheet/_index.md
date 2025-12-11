---
title: Rotate Text with Shape inside the Worksheet
type: docs
weight: 1300
url: /python-net/rotate-text-with-shape-inside-the-worksheet/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

You can add text inside any shape using Microsoft Excel. If you add a shape using the very old Microsoft Excel 2003, then the text will not rotate with the shape. But if you add a shape using newer versions of Microsoft Excel, e.g., 2007, 2010, 2013, or 2016, then the text will rotate with the shape. You can control whether the text should rotate with the shape using the [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) property. The default value is **true**, which means the text will rotate with the shape, but if you set it to **false**, the text will not rotate with the shape.

## **Rotate Text with Shape inside the Worksheet**

The following sample code loads the [sample Excel file](64716896.xlsx) that has a triangle shape and its text rotates with the shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) property to **false** and saves it as [output Excel file](64716897.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on the sample Excel file for reference.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-RotateTextWithShapeInsideWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
