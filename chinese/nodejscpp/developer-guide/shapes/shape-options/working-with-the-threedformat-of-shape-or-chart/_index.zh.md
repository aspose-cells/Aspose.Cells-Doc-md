---
title: 通过Node.js使用C++处理Shape或Chart的三维格式
linktitle: 使用 Aspose.Cells 处理形状或图表的三维格式
type: docs
weight: 250
url: /zh/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **可能的使用场景**
Aspose.Cells for Node.js via C++提供[Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) 属性和[ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat)类，用于处理形状或图表的三维格式。 [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat)类包含多个属性，可根据应用需求设置以实现不同效果。

## **使用 Aspose.Cells 处理形状或图表的三维格式**
以下示例代码加载[源Excel文件](5115419.xlsx)，访问第一个工作表中的第一个形状，设置[Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--)属性的子属性，然后将工作簿保存为[输出Excel文件](5115410.xlsx)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
