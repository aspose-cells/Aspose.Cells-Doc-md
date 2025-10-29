---
title: Загрузите рабочую книгу с конкретной информацией о системной культуре с помощью Node.js и C++
linktitle: Загрузите книгу с использованием определенной информации о культуре системы
type: docs
weight: 190
url: /ru/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Возможные сценарии использования**
 Ранее приходилось изменять настройку cultura всей потоковой среды для обработки чисел и дат в определенном формате культуры, но теперь Aspose.Cells for Node.js via C++ предоставляет свойство `LoadOptions.CultureInfo`, которое позволяет загружать рабочие книги с конкретной информацией о культуре без изменения культуры всей потоковой среды.

## **Загрузите книгу с использованием определенной информации о культуре системы**
 Следующий пример показывает, как загружать рабочую книгу с конкретной системной информацией о культуре для обработки дат.

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

 Следующий пример показывает, как загружать рабочую книгу с конкретной системной информацией о культуре для обработки чисел.

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
