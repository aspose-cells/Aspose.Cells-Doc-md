---
title: Node.js kullanarak Dış Bağlantıları ile Aralıkları Alın (C++ ile)
linktitle: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 120
url: /tr/nodejs-cpp/get-range-with-external-links/
description: Aspose.Cells for Node.js via C++ kullanarak dış bağlantıları olan aralıkları nasıl alacağınızı öğrenin. Farklı Excel dosyalarından verileri verimli şekilde alın.
---

## **Harici Bağlantıları Olan Aralığı Al**

Birçok durumda Excel dosyaları, başka Excel dosyalarından dış bağlantılar kullanarak veri erişir. Aspose.Cells for Node.js via C++, [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) metodunu kullanarak bu dış bağlantıları almanızı sağlar. [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) metodu, [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) türünden bir dizi döner. [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) sınıfı, dış dosyanın adını döndüren [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) özelliğini sağlar. [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) sınıfı aşağıdaki üyeleri sergiler.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): Bölgenin son sütunu
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): Bölgenin son satırı
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Bu dış referanssa, dış dosya adını al
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Bu, bir alan mı gösterir
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Bu, dış bağlantı mı gösterir
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Bu, hangi sayfada olduğunu gösterir
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): Bölgenin başlangıç sütunu
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): Bölgenin başlangıç satırı

Aşağıda verilen örnek kod, Dış Bağlantılı Aralıkları almak için [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) metodunun kullanımını gösterir.

## **Örnek Kod**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
