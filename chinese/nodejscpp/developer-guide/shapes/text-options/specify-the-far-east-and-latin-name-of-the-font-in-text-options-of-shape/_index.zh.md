---  
title: 在形状的文本选项中指定东亚和拉丁字体名称，使用Node.js通过C++  
linktitle: 在形状的文本选项中指定远东和拉丁文字体的名字  
type: docs  
weight: 1600  
url: /zh/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: 学习如何在形状的文本选项中指定东亚和拉丁字体名称，使用Aspose.Cells for Node.js via C++。  
---  

## **可能的使用场景**  

有时你希望用东亚语言字体（如日语、中文、泰语等）显示文本。Aspose.Cells for Node.js via C++提供[**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--)属性，用以指定东亚语言的字体名。另外，还可以用[**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--)属性指定拉丁字体名。  

## **在形状的文本选项中指定远东和拉丁文字体的名字**  

以下示例代码创建了一个文本框并在其中添加一些日语文本，然后指定了文本的拉丁和远东字体名称，并将工作簿保存为[输出Excel文件](67338274.xlsx)。下方截图显示输出文本框在Microsoft Excel中的拉丁和远东字体名称。  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

