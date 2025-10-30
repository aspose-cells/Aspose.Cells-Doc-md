---
title: Excel çalışma kitabını Ods, Sxc ve Fods (OpenOffice / LibreOffice hesap tablosu) formatlarına Node.js kullanarak dönüştürme
linktitle: Ods
type: docs
weight: 20
url: /tr/nodejs-cpp/convert-excel-to-ods/
description: Excel i Ods ye (OpenOffice / LibreOffice Calc) dönüştürme veya Ods yi (OpenOffice / LibreOffice Calc) Excel e dönüştürme Aspose.Cells for Node.js via C++ ile nasıl yapılır.
---

## **OpenDocument Hakkında**
[OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument), orijinal olarak Sun tarafından Open Office paketi için geliştirilen elektronik ofis belgeleri için ücretsiz ve açık bir dosya formatıdır. OpenDocument Spreadsheet (ODS), Excel belgelerinin dosya biçimidir. OpenDocument şu anda bir OASIS ve ISO standardıdır.

## **Ods (OpenOffice / LibreOffice calc)'i Excel'e dönüştür**
Aspose.Cells for Node.js via C++, OpenOffice / LibreOffice Calc tarafından desteklenen Ods, Sxc ve Fods dosyalarını yüklemeyi destekler ve [Ods](book1.ods), [Sxc](book1.sxc) ve [Fods](book1.fods) dosyalarını Excel formatına dönüştürür.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **Excel'i Ods (OpenOffice / LibreOffice Calc)'e dönüştür**
Aspose.Cells for Node.js via C++, Excel dosyalarını Ods, Sxc ve Fods dosyalarına dönüştürmeyi destekler. Aşağıdaki kod örneği, [şablon](book1.xlsx) dosyasını Ods, Sxc ve Fods dosyalarına nasıl dönüştüreceğinizi gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Gelişmiş Konular**
- [ODS Dosyasını ODF 1.1 ve 1.2 Özelliklerine Kaydetme](/cells/tr/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [ODS Dosyalarında Arkaplanla Çalışma](/cells/tr/nodejs-cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="nodejs-cpp" >}}
