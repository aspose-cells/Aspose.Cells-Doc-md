---  
title: Node.js ve C++ ile Tabloyu ODS ye dönüştürme  
linktitle: Tabloyu ODS ye Dönüştür  
type: docs  
weight: 70  
url: /tr/nodejs-cpp/convert-table-to-ods/  
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel dosyasını tablo ile birlikte ODS formatına nasıl dönüştüreceğinizi öğrenin.  
---  

Aspose.Cells, bir Excel dosyasını tablo içeren ODS dosyasına dönüştürmeyi destekler. Sadece dosyayı ODS formatında kaydetmeniz yeterlidir ve oluşturulan ODS dosyası fonksiyonel bir tabloya sahip olur.

## Örnek Kod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

Örnek kod tarafından oluşturulan çıktı ODS dosyası referansınız için ekte sunulmuştur.

[**Output ODS File**](ConvertTableToOds_out.ods)  

