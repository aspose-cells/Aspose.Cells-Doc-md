---
title: Node.js ve C++ kullanarak Pivot Bağlantısını Kaldırma
linktitle: Pivot Bağlantısını Kaldır
type: docs
weight: 30
url: /tr/nodejs-cpp/remove-pivot-connection/
description: Aspose.Cells for Node.js via C++ kullanarak pivot bağlantısını nasıl kaldıracağınızı öğrenin.
keywords: Office 2013, Office 2016, Office 2019 ve Office 365 olmadan Node.js ve C++ kullanarak pivot bağlantısını kaldırın.
---

## **Olası Kullanım Senaryoları**

 Excel'de bir dilimleyiciyi ve pivot tablosunu bağlıyken ayırmak istiyorsanız, dilimleyiciyi sağ tıklayın ve "Rapor Bağlantıları..." öğesini seçin. Seçenek listesinden onay kutusunu kullanabilirsiniz. Benzer şekilde, Aspose.Cells API kullanarak programlı olarak dilimleyici ve pivot tabloyu ayırmak için lütfen [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-) metodunu kullanın. Bu, dilimleyici ve pivot tabloyu ayıracaktır.

## **Dilimleyici ve pivot tablosunu ayır**

 Aşağıdaki örnek kod, var olan bir dilimleyici içeren [örnek Excel dosyasını](remove-pivot-connection.xlsx) yükler. Dilimleyicilere erişir ve ardından dilimleyiciyi ve pivot tabloyu ayırır. Son olarak, çalışma kitabını [çıktı Excel dosyası](remove-pivot-connection-out.xlsx) olarak kaydeder.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
