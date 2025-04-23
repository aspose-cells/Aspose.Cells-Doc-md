---
title: Node.js ve C++ kullanarak Dilimleyici Özelliklerini Değiştir
linktitle: Slice Özelliklerini Değiştir
type: docs
weight: 70
url: /tr/nodejs-cpp/change-slicer-properties/
---

## **Olası Kullanım Senaryoları**

 Bazı durumlarda, dilimleyicinin konumu veya satır yüksekliği gibi özelliklerini değiştirmek isteyebilirsiniz. Aspose.Cells for Node.js via C++, bu özellikleri güncelleme seçeneği sunar.

## **Slice Özelliklerini Değiştir**

Lütfen aşağıdaki örnek kodu görün. İçinde bir tablo içeren [örnek Excel dosyasını](sampleCreateSlicerToExcelTable.xlsx) yükler. Ardından, ilk sütuna dayalı olarak dilimleyici oluşturur ve satır yüksekliği, genişlik, yazdırılabilir, başlık vb. gibi özelliklerini değiştirir. Çalışma kitabını [çıkışDilimleyiciÖzellikleriniDeğiştir.xlsx](çıkışDilimleyiciÖzellikleriniDeğiştir.xlsx) olarak kaydeder.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing a table.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateSlicerToExcelTable.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first table inside the worksheet.
const table = worksheet.getListObjects().get(0);

// Add slicer
const idx = worksheet.getSlicers().add(table, 0, "H5");

const slicer = worksheet.getSlicers().get(idx);
slicer.setPlacement(AsposeCells.PlacementType.FreeFloating);
slicer.setRowHeightPixel(50);
slicer.setWidthPixel(500);
slicer.setTitle("Aspose");
slicer.setAlternativeText("Alternate Text");
slicer.setIsPrintable(false);
slicer.setIsLocked(false);

// Refresh the slicer.
slicer.refresh();

// Save the workbook in output XLSX format.
workbook.save(path.join(outputDir, "outputChangeSlicerProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
