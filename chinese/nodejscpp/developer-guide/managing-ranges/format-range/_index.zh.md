---  
title: 通过 C++ 使用 Node.js 格式化范围  
linktitle: 格式化范围  
type: docs  
weight: 105  
url: /zh/nodejs-cpp/how-to-format-a-range/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 格式化 Excel 中的一组单元格。  
---  

## **可能的使用场景**  
当您需要对一组范围应用样式时，可以使用范围格式化。  

## **如何在Excel中格式化范围**  

要在Excel中格式化一系列单元格，您可以使用Excel提供的内置格式选项。以下是如何直接在Excel中格式化一系列单元格的方法：  

1. 打开Excel并打开包含要格式化的范围的工作簿。  

2. 选择您要格式化的单元格范围。您可以单击并拖动以选择范围，或者您可以使用诸如Shift+箭头键之类的键盘快捷键来扩展选择。  

3. 选择范围后，右键单击所选范围，然后从上下文菜单中选择“格式单元格”。或者，您可以转到ExcelRibbon中的“主页”选项卡，在“单元格”组中的“格式”下拉菜单中单击“格式单元格”进行选择。  

4. “格式单元格”对话框将会出现。在这里，您可以选择各种格式选项来应用于所选范围。例如，您可以更改字体样式、字体大小、字体颜色、数字格式、边框、背景颜色等。在对话框中探索不同的标签以访问各种格式选项。  

5. 在进行所需的格式更改后，单击“确定”按钮以将格式应用于所选范围。  

## **如何使用 Node.js 格式化范围**  

要使用 Aspose.Cells for Node.js via C++ 格式化范围，可以使用以下方法：  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **示例代码**  
在此示例中，我们创建一个Excel工作簿，添加一些示例数据，访问第一个工作表，并定义两个范围("A1:C3"和"A4:C5")。然后，我们创建新样式，设置各种格式选项（如字体颜色，加粗），并将样式应用到范围。最后，我们将工作簿保存到一个新文件。  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
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

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
