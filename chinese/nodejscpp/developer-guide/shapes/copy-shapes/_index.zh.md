---
title: 通过 C++ 使用 Node.js 在工作表之间复制 Shapes
linktitle: 复制形状
type: docs
weight: 200
url: /zh/nodejs-cpp/copy-shapes-between-worksheets/
description: 了解如何使用 Aspose.Cells for Node.js via C++ 在工作表之间复制图片、图表等形状。
---

{{% alert color="primary" %}}

有时候，您需要在工作表之间复制元素，比如图片、图表和其他绘图对象。Aspose.Cells for Node.js via C++ 支持此功能。可以以最高精度复制图表、图像和其他对象。

本文详细介绍了如何在工作表之间复制形状。

{{% /alert %}}

## **从一个工作表复制图片到另一个工作表**

要将图片从一个工作表复制到另一个，请使用以下示例代码中显示的 [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) 方法。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_picture.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Picture from the "Picture" worksheet.
const picturesource = workbook.getWorksheets().get("Picture").getPictures().get(0);

// Save Picture to Memory Stream
const ms = picturesource.getData();

// Copy the picture to the Result Worksheet
workbook.getWorksheets().get("Result").getPictures().add(picturesource.getUpperLeftRow(), picturesource.getUpperLeftColumn(), ms, picturesource.getWidthScale(), picturesource.getHeightScale());

// Save the Worksheet
workbook.save(path.join(dataDir, "PictureCopied_out.xlsx"));
```

## **将图表从一个工作表复制到另一个**

以下代码演示了使用 [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) 方法将图表从一个工作表复制到另一个。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Chart from the "Chart" worksheet.
const chartsource = workbook.getWorksheets().get("Chart").getCharts().get(0);
const cshape = chartsource.getChartObject();

// Copy the Chart to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(cshape, 20, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ChartCopied_out.xlsx"));
```

## **从一个工作表复制控件和其他绘图对象到另一个**

若要复制控件和其他绘图对象，请使用 [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) 方法，如下面的示例所示。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_control.xlsx");
// Open the template file
const workbook = new AsposeCells.Workbook(filePath);

// Get the Shapes from the "Control" worksheet.
const shape = workbook.getWorksheets().get("Control").getShapes();

// Copy the Textbox to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(0), 5, 0, 2, 0);

// Copy the Oval Shape to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(1), 10, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ControlsCopied_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
