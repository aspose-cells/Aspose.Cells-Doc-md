---
title: تحميل الدفتر بحكمة الثقافة النظامية عبر Node.js و C++
linktitle: تحميل سجل العمل بمعلومات الثقافة النظامية المحددة
type: docs
weight: 190
url: /ar/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **سيناريوهات الاستخدام المحتملة**
 سابقًا، كان عليك تغيير المعلومات الثقافية للنص بأكمله للتعامل مع الأرقام والتواريخ بتنسيق ثقافي معين، لكن الآن يوفر Aspose.Cells for Node.js via C++ خاصية `LoadOptions.CultureInfo` التي يمكنك استخدامها لتحميل دفتر العمل الخاص بك بمعلومات ثقافية محددة بدون تغيير الثقافة العامة للنظام.

## **تحميل سجل العمل بمعلومات الثقافة النظامية المحددة**
 يظهر الكود النموذجي التالي كيف يتم تحميل دفتر العمل بمعلومات ثقافية نظامية محددة للتعامل مع التواريخ.

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

 يظهر الكود التالي كيف يتم تحميل دفتر العمل بمعلومات ثقافية نظامية محددة للتعامل مع الأرقام.

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
