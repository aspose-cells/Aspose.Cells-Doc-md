---
title: OpenXml’in Sheet.SheetId Özelliğini Aspose.Cells for Node.js via C++ kullanarak Yükleme
linktitle: Aspose.Cells Kullanarak OpenXml in Sayfa Kimliği Özelliğini Kullanın
type: docs
weight: 200
url: /tr/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel manipülasyonu ile OpenXml’in Sheet.SheetId özelliğini nasıl kullanacağınızı gösterir.
keywords: openxml düğüm.js sheet id özelliği C++ ile excel çalışma sayfası düğüm.js üzerinden sheet id
---

## **Olası Kullanım Senaryoları**

*Sheet.SheetId* özelliği *DocumentFormat.OpenXml.Spreadsheet* modülü içinde mevcuttur ve OpenXml'in bir parçasıdır. Bu özelliği ve değerini *workbook.xml* içinde aşağıdaki ekran görüntüsünde görebilirsiniz. Aspose.Cells, karşılık gelen özelliği [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--) olarak sağlar.

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **OpenXml'in Sheet.SheetId özelliğini Aspose.Cells for Node.js via C++ kullanarak kullanın**

Aşağıdaki örnek kod, [örnek Excel dosyasını](51740716.xlsx) yükler, Sayfa veya Sekme Kimliğini okur, ardından yeni Sekme Kimliğini atar ve [çıktı Excel dosyası](51740717.xlsx) olarak kaydeder. Ayrıca, aşağıda verilen kodun konsol çıktısını da inceleyin.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **Konsol Çıktısı**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
