---
title: Node.js ve C++ kullanarak Pivot Bağlantısı Ekleme
linktitle: Pivot Bağlantısı Ekleme
type: docs
weight: 30
url: /tr/nodejs-cpp/add-pivot-connection/
description: Aspose.Cells for Node.js via C++ kullanarak pivot bağlantısı eklemeyi öğrenin.
keywords: Office 2013, Office 2016, Office 2019 ve Office 365 olmadan Node.js ve C++ kullanarak pivot bağlantısı ekleyin.
---

## **Olası Kullanım Senaryoları**

Excel'de bir dilimleyici ve pivot tablosunu ilişkilendirmek istiyorsanız, dilimleyiciyi sağ tıklayın ve "Rapor Bağlantıları..." seçeneğini seçin. Seçenek listesinden onay kutusunu kullanabilirsiniz. Benzer şekilde, Aspose.Cells API kullanarak programlı olarak bir dilimleyici ve pivot tablosunu ilişkilendirmek için lütfen [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-) metodunu kullanın. Bu, dilimleyici ve pivot tabloyu ilişkilendirecektir.

## **Dilimleyiciyi ve Pivot Tablosunu İlişkilendir**

 Aşağıdaki örnek kod, var olan bir dilimleyici içeren [örnek Excel dosyasını](add-pivot-connection.xlsx) yükler. Dilimleyiciyi erişir ve ardından dilimleyici ile pivot tabloyu ilişkilendirir. Son olarak çalışma kitabını [çıktı Excel dosyası](add-pivot-connection-out.xlsx) olarak kaydeder.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
