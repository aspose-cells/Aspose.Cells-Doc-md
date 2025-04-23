---
title: Node.js経由で名前によるテキストボックスへのアクセス
linktitle: 名前でテキストボックスにアクセス
type: docs
weight: 230
url: /ja/nodejs-cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for Node.js via C++を使用してコレクションから名前でテキストボックスにアクセスする方法を学習します。 
---

## 名前でテキストボックスにアクセスする

以前は、テキストボックスは[**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--)コレクションのインデックスでアクセスされていましたが、現在はこのコレクションから名前でアクセスすることもできます。これは、名前をすでに知っている場合に便利で迅速な方法です。

次のサンプルコードはまずテキストボックスを作成し、テキストと名前を割り当てます。次に、その名前で同じテキストボックスにアクセスし、そのテキストを出力します。

### Node.jsを使った名前によるテキストボックスアクセスコード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
