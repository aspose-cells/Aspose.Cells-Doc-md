---
title: Node.jsを通じたC++を使った自己閉塞タグの認識
linktitle: 自己閉じタグを認識してください。
type: docs
weight: 120
url: /ja/nodejs-cpp/recognise-self-closing-tags/
---

HTML can have a variety of tag formatting for empty tags like `<td></td>` or `<td/>`. Aspose.Cells for Node.js via C++ supports both these formats now whereas earlier it was supporting only `<td></td>` like tags. This feature can be tested by converting the attached sample HTML file to an Excel file. The sample HTML file and output Excel file can be downloaded from the following links for testing.

[sampleSelfClosingTags.html](sampleSelfClosingTags)

[outsampleSelfClosingTags.xlsx](73990156.xlsx)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Load sample source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleSelfClosingTags.html"), loadOptions);

// Save the workbook
wb.save(path.join(outputDir, "outsampleSelfClosingTags.xlsx"));
```

