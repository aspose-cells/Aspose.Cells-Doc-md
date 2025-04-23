---
title: Как применить/установить выравнивание текста внутри TextBox с помощью Node.js через C++
linktitle: Применить/установить выравнивание текста для текстового поля
type: docs
weight: 20
url: /ru/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Как применить/установить выравнивание текста в TextBox в Aspose.Cells for Node.js via C++.
keywords: применить/установить выравнивание TextBox, лист, Excel, Aspose, Node.js через C++
---

Текстовые поля могут повысить выразительность наших документов и диаграмм, а применение разных выравниваний к разным частям TextBox может помочь выделить важные моменты для читателей. Но стандартное выравнивание TextBox не удовлетворяет все наши потребности. Для этого возможно потребуется настроить каждое TextBox под ваши требования. Если у вас немного объектов TextBox для настройки, это отлично. А если их много — это может стать проблемой. Не волнуйтесь, [Aspose.Cells](https://products.aspose.com/cells/) предоставляет API, который может помочь вам в этом.

Приведенный ниже образец кода применяет выравнивание текста к текстовому полю.

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

Вы также можете изменить выравнивание текста внутри некоторого текста в фигуре TextBox с помощью соответствующего HTML текста. Следующий пример демонстрирует применение выравнивания текста внутри части текста в TextBox.

[исходный файл](SampleTextboxExcel2016.xlsx)

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
