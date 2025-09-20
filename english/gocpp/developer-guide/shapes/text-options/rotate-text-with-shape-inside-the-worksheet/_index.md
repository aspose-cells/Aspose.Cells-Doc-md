---
title: Rotate Text with Shape inside the Worksheet with Golang via C++
linktitle: Rotate Text with Shape
type: docs
weight: 1300
url: /go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Learn how to control text rotation with shapes in Excel worksheets using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

You can add text inside any shape using Microsoft Excel. If you add a shape using the very old Microsoft Excel 2003, then the text will not rotate with the shape. However, if you add a shape using newer versions of Microsoft Excel, such as 2007, 2010, 2013, or 2016, the text will rotate with the shape. You can control whether the text should rotate with the shape or not using the [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) property. The default value of this property is **true**, which means the text will rotate with the shape. If you set it to **false**, the text will not rotate with the shape.

## **Rotate Text with Shape inside the Worksheet**

The following sample code loads the [sample Excel file](64716896.xlsx) that contains a triangle shape, and its text rotates with the shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) property to **false** and saves it as the [output Excel file](64716897.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on the sample Excel file for reference.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}