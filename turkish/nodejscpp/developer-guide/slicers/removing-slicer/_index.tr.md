---
title: Node.js ve C++ kullanarak Dilimleyiciyi Kaldırma
linktitle: Dilimleyici Kaldırma
type: docs
weight: 30
url: /tr/nodejs-cpp/removing-slicer/
---

## **Olası Kullanım Senaryoları**

 Excel'de bir dilimleyiciyi kaldırmak istiyorsanız, onu seçin ve *Sil* düğmesine basın. Benzer şekilde, Aspose.Cells API kullanarak programlı olarak kaldırmak için lütfen [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-) metodunu kullanın. Bu, dilimleyiciyi çalışma sayfasından kaldırır.

## **Süzgeci Kaldırma**

 Aşağıdaki örnek kod, var olan bir dilimleyici içeren [örnek Excel dosyasını](67338478.xlsx) yükler. Dilimleyiciyi erişir ve sonra kaldırır. Son olarak, çalışma kitabını [çıktı Excel dosyası](67338477.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çalışması sonrası kaldırılacak olan dilimleyiciyi gösterir.

![todo:image_alt_text](removing-slicer_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
