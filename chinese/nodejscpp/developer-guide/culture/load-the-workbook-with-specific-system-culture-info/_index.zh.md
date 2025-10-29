---
title: 使用 Node.js 及 C++ 加载具有特定系统文化信息的工作簿
linktitle: 使用特定系统的区域设置信息加载工作簿
type: docs
weight: 190
url: /zh/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **可能的使用场景**
以前，你需要更改整个线程的文化信息以处理特定文化格式中的数字和日期，但现在Aspose.Cells for Node.js via C++提供了`LoadOptions.CultureInfo`属性，你可以用它在不更改整个线程文化信息的情况下加载具有特定文化信息的工作簿。

## **使用特定系统的区域设置信息加载工作簿**
下列示例代码演示如何使用特定系统文化信息加载工作簿以处理日期。

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');

// Create a readable stream
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>");
inputStream.push(null); // Signal end of stream

const culture = new Intl.NumberFormat("en-GB", {
minimumFractionDigits: 2,
maximumFractionDigits: 2
```

下列示例代码演示如何使用特定系统文化信息加载工作簿以处理数字。

```javascript
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');
const path = require("path");

const dataDir = path.join(__dirname, "data");
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>");
inputStream.push(null);

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Html);        
options.setRegion(AsposeCells.CountryCode.UnitedKingdom);

(async () => {
const workbook = new AsposeCells.Workbook(inputStream, options);
const cell = workbook.getWorksheets().get(0).getCells().get("A1");
console.assert(cell.getType() === AsposeCells.CellValueType.IsNumeric);
console.assert(cell.getDoubleValue() === 1234.56);
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
