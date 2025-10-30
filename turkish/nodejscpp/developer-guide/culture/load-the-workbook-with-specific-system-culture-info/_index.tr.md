---
title: Node.js ve C++ kullanarak belirli Sistem Kültür Bilgisi ile Çalışma Kitabı Yükleyin
linktitle: Belirli Sistem Kültür Bilgisiyle Çalışma Kitabı Yükle
type: docs
weight: 190
url: /tr/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Olası Kullanım Senaryoları**
Daha önce, sayı ve tarihleri belirli bir kültür formatında yönetmek için tüm iş parçacığının kültür bilgisini değiştirmeniz gerekiyordu, ancak şimdi Aspose.Cells for Node.js via C++, `LoadOptions.CultureInfo` özelliği sağlar ve tüm iş parçacığını değiştirmeden belirli kültür bilgisi ile çalışma kitabınızı yüklemenize olanak tanır.

## **Belirli Sistem Kültür Bilgisiyle Çalışma Kitabı Yükleme**
Aşağıdaki örnek kod, tarihleri yönetmek için belirli sistem kültür bilgisiyle çalışma kitabını nasıl yükleyeceğinizi gösterir.

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

Aşağıdaki örnek kod, sayıları yönetmek için belirli sistem kültür bilgisiyle çalışma kitabını nasıl yükleyeceğinizi gösterir.

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
