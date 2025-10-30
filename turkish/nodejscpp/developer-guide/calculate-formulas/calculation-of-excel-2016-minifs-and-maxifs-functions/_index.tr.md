---
title: Node.js aracılığıyla C++ kullanarak Excel 2016 MINIFS ve MAXIFS fonksiyonlarının hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Node.js aracılığıyla C++ ile Microsoft Excel 2016 da MINIFS ve MAXIFS fonksiyonlarını nasıl hesaplayacağınızı tanıtmaktadır. Mevcut bir Excel dosyasını yükleyin veya yeni bir tane oluşturun, ardından Aspose.Cells yöntemlerini kullanarak bu fonksiyonları hesaplayın ve sonuçları diske kaydedin.
keywords: Aspose.Cells, Excel, 2016, MINIFS fonksiyonu, MAXIFS fonksiyonu, hesaplama Node.js aracılığıyla C++
type: docs
weight: 300
url: /tr/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel 2016, MINIFS ve MAXIFS fonksiyonlarını destekler. Bu fonksiyonlar Excel 2013 veya daha eski sürümlerde desteklenmez. Aspose.Cells for Node.js via C++ ayrıca bu fonksiyonların hesaplanmasını da destekler. Aşağıdaki ekran görüntüsü bu fonksiyonların kullanımını göstermektedir. Bu fonksiyonların nasıl çalıştığını bilmek için ekran görüntüsündeki kırmızı yorumları okuyun.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması**
Aşağıdaki örnek kod, [örnek excel dosyasını](5115149.xlsx) yükler ve [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) metodunu çağırarak Aspose.Cells for Node.js via C++ aracılığıyla formül hesaplamasını gerçekleştirir ve sonuçları [çıktı PDF'sine](5115154.pdf) kaydeder.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleMINIFSAndMAXIFS.xlsx");

// Load your source workbook containing MINIFS and MAXIFS functions
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Perform Aspose.Cells formula calculation
workbook.calculateFormula();

// Save the calculations result in pdf format
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);
const outputFilePath = path.join(dataDir, "outputMINIFSAndMAXIFS.pdf");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
