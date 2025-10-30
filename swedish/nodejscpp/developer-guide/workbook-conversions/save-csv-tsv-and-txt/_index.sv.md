---
title: Konvertera Excel till CSV, TSV och Txt med Node.js via C++
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Lär dig konvertera Excel filer till CSV, TSV och TXT med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att konvertera Excel, ODS, JSON och andra formatfiler till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara ett arbetsbok med flera flikar till textformat. För textformat (t.ex. TXT, TabDelim, CSV, etc.), sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva kalkylbladet.

Följande kodexempel förklarar hur man sparar en hel arbetsbok till textformat. Ladda den källa arbetsboken, som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylbladsfil som helst (såsom XLS, XLSX, XLSM, XLSB, ODS osv.) med valfritt antal kalkylblad.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan ändra samma exempel för att spara din fil till CSV. Som standard är [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) ett kommatecken, så ange inte en avskiljare om du sparar till CSV-format.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Fortsatta ämnen**
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
