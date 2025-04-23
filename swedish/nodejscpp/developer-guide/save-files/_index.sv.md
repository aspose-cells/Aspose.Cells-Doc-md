---
title: Olika sätt att spara filer med Node.js via C++
linktitle: Spara filer
type: docs
weight: 40
url: /sv/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ kan spara filer i olika format inklusive PDF, HTML, DOCX, PPTX, JSON och MHTML.
keywords: Aspose.Cells sparar Excel till PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML och fler med Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att skapa och spara filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}}

## **Olika sätt att spara filer**

Aspose.Cells tillhandahåller [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil och ger de egenskaper och metoder som krävs för att arbeta med Excel-filer. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen tillhandahåller [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-metoden som används för att spara Excel-filer. [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-metoden har många överlagringar som används för att spara filer på olika sätt.

Det filformat som filen sparas i bestäms av [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-enumerationen

|**Filtyp**|**Beskrivning**|
| :- | :- |
|CSV|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007 XLSX-fil|
|Xlsm|Representerar en Excel 2007 XLSM-fil|
|Xltx|Representerar en Excel 2007-mall XLTX-fil|
|Xltm|Representerar en Excel 2007 med makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007 binär XLSB-fil|
|SpreadsheetML|Representerar en kalkyl XML-fil|
|TSV|Representerar en tab-separated values-fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|ODS|Representerar en ODS-fil|
|Html|Representerar HTML-fil(er)|
|MHtml|Representerar MHTML-fil(er)|
|Pdf|Representerar en PDF-fil|
|XPS|Representerar ett XPS-dokument|
|TIFF|Representerar Tagged Image File Format (TIFF)|

## **Så här sparar du filen i olika format**

 För att spara filer till en lagringsplats, ange filnamnet (fullständig lagringsväg) och önskat filformat (från [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-enumerationen) när du anropar [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-objektets [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-metod.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Så här sparar du arbetsbok till Pdf**
 Portable Document Format (PDF) är en typ av dokument som skapades av Adobe på 1990-talet. Syftet med detta filformat var att införa en standard för presentation av dokument och annat referensmaterial i ett format som är oberoende av applikationsprogramvara, hårdvara och operativsystem. PDF-filtet innehåller fulla kapaciteter för att innehålla information som text, bilder, hyperlänkar, formulärfält, rik media, digitala signaturer, bilagor, metadata, geospatiala funktioner och 3D-objekt som kan bli en del av källa dokumentet.

 Följande kod visar hur man sparar arbetsbok som PDF-fil med Aspose.Cells:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Så här sparar du arbetsboken till Text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

 Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda arbetsboken som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylbladsfil som helst (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil till CSV. Som standardspecifikation är [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) komma, så ange inte en separator om du sparar till CSV-format. Observera: Om du använder utvärderingsversionen och även om egenskapen [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) är inställd på true, kommer programmet fortfarande endast att exportera ett kalkylblad.

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

## **Så här sparar du filen till textfiler med anpassad avskiljare**

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

## **Så här sparar du filen till en ström**

För att spara filer till en ström, skapa ett *MemoryStream* eller *FileStream*-objekt och spara filen till den strömmen genom att anropa [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) objektets [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metod. Specificera önskat filformat med enumrationen [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) när du anropar [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-metoden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Så här sparar du Excel-filen till HTML- och MHT-filer**
Aspose.Cells kan enkelt spara en Excel-fil, JSON, CSV eller andra filer som kan laddas av Aspose.Cells som .html och .mht-filer.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Så här sparar du Excel-filen till OpenOffice (ODS, SXC, FODS, OTS)**
Vi kan spara filerna i OpenOffice-format: ODS, SXC, FODS, OTS, etc.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Så här sparar du Excel-filen till JSON eller XML**

JSON (JavaScript Object Notation) är ett öppet standardfilformat för att dela data som använder mänskligt läsbar text för att lagra och överföra data. JSON-filer lagras med filändelsen .json. JSON kräver mindre formatering och är ett bra alternativ till XML. JSON härstammar från JavaScript men är ett språkoberoende dataformat. Generering och tolkning av JSON stöds av många moderna programmeringsspråk. application/json är mediatypen som används för JSON.

Aspose.Cells stöder att spara filer i JSON eller XML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **Fortsatta ämnen**
- [Justera arbetsbokens kompressionsnivå](/cells/sv/nodejs-cpp/adjust-workbook-compression-level/)
- [Spara arbetsbok i strikt öppet XML-kalkylbladsformat](/cells/sv/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Spara fil till responsobjekt](/cells/sv/nodejs-cpp/saving-file-to-response-object/)
