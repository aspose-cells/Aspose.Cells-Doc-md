---
title: JSON dan Excel e dönüşüm Node.js aracılığıyla C++ kullanılarak
linktitle: JSON u Excel dosyasına Dönüştürme
type: docs
weight: 300
url: /tr/nodejs-cpp/convert-json-to-excel/
description: Aspose.Cells for Node.js via C++ kullanarak JSON u Excel dosyasına dönüştürmeyi öğrenin.
keywords: JSON u Office 2013, Office 2016, Office 2019 ve Office 365 kullanmadan Node.js aracılığıyla içe aktarın.
---

{{% alert color="primary" %}}

Aspose.Cells, JSON (JavaScript Nesne Gösterimi) dosyasını Excel Workbook'una dönüştürmeyi destekler.

{{% /alert %}}

## **JSON'u Excel Workbook'e dönüştür**
JSON'u Excel dosyasına dönüştürmenin en iyi çözümünü sunar, çünkü Aspose.Cells for Node.js via C++ en iyi sonucu sağlar. Aspose.Cells API, JSON formatını elektronik tabloya dönüştürmeyi destekler. JSON'u Workbook'a ithal etmek için [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, JSON'u Excel Çalışma Kitabına içe aktarmayı göstermektedir. Lütfen başvuru için kodu inceleyin [kaynak dosyası](örnek.json) kod tarafından oluşturulan xlsx dosyası.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

Aşağıdaki kod örneği, JsonLoadOptions sınıfını kullanarak ek ayarların gösterildiği, JSON'u Excel Workbook'a ithal etmeyi sağlar. [Kaynak dosyası](sample.json) 'yi XLSX formatına dönüştürmek için kodu inceleyebilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

Aşağıdaki kod örneği, JSON dizesini Excel Workbook'a ithal etmeyi gösterir. JSON'u ithal ederken düzenin konumunu da belirtebilirsiniz. Dönüşüm için kodu kullanarak JSON dizesini XLSX dosyasına dönüştürmeyi görebilirsiniz.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
