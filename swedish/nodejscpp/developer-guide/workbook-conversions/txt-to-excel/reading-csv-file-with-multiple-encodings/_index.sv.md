---
title: Läser CSV fil med flera teckenkodningar med Node.js via C++
linktitle: Läsning av CSV fil med flera kodningar
type: docs
weight: 200
url: /sv/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Lär dig hur du läser CSV filer med flera teckenkodningar med Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera teckenkodningar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells låter dig ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

Aspose.Cells ger egenskapen [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--), som du behöver ställa in på **true** för att ladda din CSV-fil med flera kodningar korrekt.

Följande skärmbild visar en prov-CSV-fil som innehåller två rader. Den första raden är kodad med **ANSI** och den andra raden är kodad med **Unicode**

|**Ingående fil**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Följande skärmbild visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)-egenskapen till **true**. Som du ser, tolkades Unicode-texten inte korrekt.

|**Utgående fil 1: ingen anpassning gjord för flera krypteringar**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Följande skärmbild visar XSLX-filen konverterad från ovan nämnda CSV-fil efter att egenskapen [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) har ställts in till **true**. Som du kan se är Unicode-texten nu konverterad korrekt.

|**Utgående fil 2: IsMultiEncoded är satt till true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är det exempelkod som konverterar ovanstående CSV-fil till XLSX-format korrekt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## Relaterade artiklar

- [Öppning av CSV-filer](/cells/sv/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
