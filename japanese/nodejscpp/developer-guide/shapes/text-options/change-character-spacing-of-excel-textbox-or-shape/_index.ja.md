---
title: Node.jsを通じたC++でのExcelのTextBoxやShapeの文字間隔変更方法
linktitle: Excelテキストボックスまたは図形の文字間隔を変更する
type: docs
weight: 280
url: /ja/nodejs-cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Aspose.Cells for Node.js via C++を使用して、ExcelのテキストボックスまたはShapeの文字間隔を変更します。 
---

{{% alert color="primary" %}}

[**TextOptions.getSpacing()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getSpacing--) プロパティを使用して、ExcelのテキストボックスまたはShapeの文字間隔を変更できます。

{{% /alert %}}

次のサンプルコードは、Excelファイル内のテキストボックスの文字間隔をポイント4に設定し、ディスクに保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load your excel file inside a workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeTextBoxOrShapeCharacterSpacing.xlsx"));

// Access your text box which is also a shape object from shapes collection
const shape = workbook.getWorksheets().get(0).getShapes().get(0);

// Access the first font setting object via getRichFormattings() method
const fontSetting = shape.getRichFormattings()[0];

// Set the character spacing to point 4
fontSetting.getTextOptions().setSpacing(4);

// Save the workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeTextBoxOrShapeCharacterSpacing.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

```javascript
const { Workbook } = require('aspose.cells'); 

// Create a workbook
const workbook = new Workbook(); 

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0); 

// Add a textbox to the worksheet
const shape = worksheet.getShapes().addTextBox(5, 5, 100, 50); 
shape.getTextBody().getText().setText("Hello World!"); 

// Change character spacing
shape.getTextBody().getParagraphs().get(0).getPortions().get(0).getFontSetting().getTextOptions().setSpacing(4); 

// Save the workbook
workbook.save("ChangedCharacterSpacing.xlsx"); 
```
