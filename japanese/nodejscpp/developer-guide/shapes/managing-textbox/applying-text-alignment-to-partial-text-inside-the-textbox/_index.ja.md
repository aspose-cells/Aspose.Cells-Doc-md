---
title: Node.jsとC++を用いてテキストボックスのテキスト揃えを適用/設定する方法
linktitle: テキストボックスにテキストの配置を行う
type: docs
weight: 20
url: /ja/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Aspose.Cells for Node.js via C++でテキストボックスにテキスト揃えを適用/設定する方法
keywords: C++を使用してNode.jsでワークシートのテキストボックスの配置を適用/設定
---

TextBoxは、私たちの文書や図表の表現力を向上させることができ、TextBoxの異なる部分に異なる配置を適用することで、読者に強調したいポイントを際立たせることができます。しかし、デフォルトの配置ではすべてのニーズを満たしません。これには、それぞれのTextBoxを調整して目標要件を満たす必要があります。調整すべきTextBoxオブジェクトがたくさんなければ幸運です。多くのTextBoxを調整しなければならない場合、問題になるかもしれません。心配はいりません、[Aspose.Cells](https://products.aspose.com/cells/)は、そのためのAPIインターフェイスを提供しています。

次のサンプルコードは、テキストボックスにテキストの配置を適用します。

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

適切なHTMLテキストを使って、TextBox内の一部のテキストのテキスト配置を変更することも可能です。以下のサンプルコードは、部分的なテキストに対してテキスト配置を適用します。

[ソースファイル](SampleTextboxExcel2016.xlsx)

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
