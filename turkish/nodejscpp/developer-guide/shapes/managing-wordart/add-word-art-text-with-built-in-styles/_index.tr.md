---
title: Node.js üzerinden C++ ile Yerleşik Stillerle Word Art Metni Ekle
linktitle: Dahili Stillerle Kelime Sanatı Metni Ekleyin
type: docs
weight: 270
url: /tr/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Aspose.Cells for Node.js via C++ kullanarak Yerleşik Stillerle Word Art Metni eklemeyi öğrenin. Excel de görsel olarak çekici metinler oluşturun.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Node.js via C++ kullanarak Yerleşik Stillerle Word Art Metni ekleyebilirsiniz. Bu amaçla [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) metodunu kullanın.

## **Dahili Stillerle Word Art Metni Ekleme**
Aşağıdaki örnek kod farklı Dahili Stillerle Kelime Sanatı metinleri ekler. Lütfen bu kodla oluşturulan [çıktı excel dosyasını](5115470.xlsx) kontrol edin. Bu, Microsoft Excel'de [çıktı excel dosyası](5115470.xlsx)'nın nasıl göründüğüdür.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add Word Art Text with Built-in Styles
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
