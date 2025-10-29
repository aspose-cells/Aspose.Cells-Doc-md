---
title: 如何通过 Node.js 和 C++ 设置文本框的文本对齐方式
linktitle: 应用/设置文本框的文本对齐
type: docs
weight: 20
url: /zh/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: 如何在 Aspose.Cells for Node.js via C++ 中设置文本框的文本对齐方式
keywords: 使用 Node.js 和 C++ 对 Excel Aspose 中的文本框对齐方式进行设置
---

文本框可以提升我们文档和图表的表现力，对文本框不同部分应用不同的对齐方式，可以帮助突出重点。但默认的文本框对齐方式不能满足所有需求。对此，你可能需要调整每个文本框以满足目标要求。如果你没有大量的文本框需要调整，你很幸运。如果有很多文本框需要调整，我想你会遇到麻烦。别担心，[Aspose.Cells](https://products.aspose.com/cells/) 提供了相关API接口帮你实现这一点。

以下示例代码将文本对齐应用于文本框。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const shapes = workbook.getWorksheets().get(0).getShapes();

// add a TextBox
const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
shape.setText("This is a test.");

// set alignment
shape.setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
shape.setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Save the excel file.
workbook.save(path.join(dataDir, "result.xlsx"));
```

你还可以用适当的HTML文本改变文本框内某些文本的对齐方式。以下示例代码将对文本框内部的部分文本应用对齐方式。

[源文件](SampleTextboxExcel2016.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SampleTextboxExcel2016.xlsx");

// Initialize an object of the Workbook class to load the template file
const sourceWb = new AsposeCells.Workbook(sourceFilePath);

// Access the target textbox whose text is to be aligned
const sourceTextBox = sourceWb.getWorksheets().get(0).getShapes().get(0);

// Create an object of the target workbook
const destWb = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const _sheet = destWb.getWorksheets().get(0);

// Create new textbox
const _textBox = _sheet.getShapes().addShape(AsposeCells.MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

// Alternatively text box can be added using the following line as well
// const _textBox = _sheet.getShapes().addTextBox(1, 0, 1, 0, 200, 200);

// Use Html string from a template file textbox
_textBox.setHtmlText(sourceTextBox.getHtmlText());

// Save the workbook on disk
destWb.save("Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
