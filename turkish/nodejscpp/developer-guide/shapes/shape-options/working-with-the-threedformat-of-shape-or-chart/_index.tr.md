---
title: Şekil veya Grafiklerin ThreeDFormat ile Node.js ve C++ kullanarak çalışma
linktitle: Şekil veya Grafik ThreeDFormat ile Çalışma
type: docs
weight: 250
url: /tr/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Node.js via C++, [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) özelliği ve [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) sınıfı ile şekil veya grafiklerin 3 boyutlu formatları üzerinde çalışmanıza olanak tanır. [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) sınıfı, farklı sonuçlar elde etmek için ayarlanabilen çeşitli özellikleri içerir.

## **Şekil veya Grafik ThreeDFormat ile Çalışma**
Aşağıdaki örnek kod, [orijinal excel dosyasını](5115419.xlsx) yükler ve ilk çalışma sayfasındaki ilk şekle erişir. [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıktı excel dosyasına](5115410.xlsx) kaydeder.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
