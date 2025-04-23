---  
title: 使用 Node.js 通过 C++ 设置范围边框  
linktitle: 设置范围边框  
type: docs  
weight: 600  
url: /zh/nodejs-cpp/set-range-border/  
---  

## **可能的使用场景**  
 当你想为一个范围设置边框时，无需逐个单元格设置。你可以直接在范围上设置边框。Aspose.Cells for Node.js via C++ 提供了此功能。  
 本文提供了使用 Aspose.Cells for Node.js via C++ 设置范围边框的示例代码。  

## **在Excel中设置范围边框**  
要在Excel中设置范围的边框，可以按照以下步骤进行：  
1. 选择要应用边框的单元格范围。  
2. 在功能区“主页”选项卡中，找到“字体”组。  
3. 在“字体”组内，单击“边框”下拉按钮。  
<br>  
<img src="border.png" />  
4. 从下拉菜单中选择要应用的边框类型。您可以选择预设的边框样式或自定义您自己的边框。  
5. 选择所需的边框样式后，边框将应用于所选的单元格范围。  

## ** 使用 Aspose.Cells for Node.js via C++ 设置范围边框**  
此示例演示如何：  

1. 创建一个工作簿。  
2. 在第一个工作表的单元格中添加数据。  
3. 创建一个[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)。  
 4. 设置范围的内部边框。  
 5. 设置范围的外部边框。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
