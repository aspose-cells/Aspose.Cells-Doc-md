---
title: 用Node.js通过C++按名称访问文本框
linktitle: 按名称访问文本框
type: docs
weight: 230
url: /zh/nodejs-cpp/access-the-text-box-by-the-name/
description: 学习如何使用Aspose.Cells for Node.js via C++从集合中按名称访问文本框。 
---

## 按名称访问文本框

早先，可以通过索引访问[**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--)集合中的文本框，但现在也可以通过名称访问此集合中的文本框。如果你已知其名称，这是一种方便快捷的访问方式。

以下示例代码首先创建了一个文本框并分配了一些文本和名称。然后在接下来的行中，我们通过其名称访问相同的文本框并打印其文本。

### 用Node.js通过C++按名称访问文本框的代码

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

### 样本代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
