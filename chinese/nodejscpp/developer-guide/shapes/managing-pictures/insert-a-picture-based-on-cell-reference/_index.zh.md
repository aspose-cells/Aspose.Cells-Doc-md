---
title: 使用Node.js通过C++基于单元格引用插入图片
linktitle: 基于单元格引用插入图片
type: docs
weight: 150
url: /zh/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: 学习如何基于单元格引用使用Aspose.Cells for Node.js via C++在工作表中插入图片。显示单元格中的数据为图片。
---

{{% alert color="primary" %}}
有时您会有一张空白图片，并且需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。Aspose.Cells支持此功能（Microsoft Excel 2010）。
{{% /alert %}}

## 根据单元格引用插入图片

Aspose.Cells for Node.js via C++支持在图片形状中显示工作表单元格的内容。你可以将图片链接到包含要显示数据的单元格。由于单元格或单元格范围与图形对象关联，您对该单元格或范围的数据所做的更改会自动显示在图形对象中。通过调用[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)方法（封装在[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection)对象中）将图片添加到工作表中。使用[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)对象的[**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)属性指定单元格范围。

### 代码示例

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
