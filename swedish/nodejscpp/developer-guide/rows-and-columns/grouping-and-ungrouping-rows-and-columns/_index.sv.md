---
title: Gruppering och Ogruppering av rader och kolumner med Node.js via C++
linktitle: Gruppering och avgruppering av rader och kolumner
type: docs
weight: 50
url: /sv/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Upptäck hur man grupperar och avgrupperar rader och kolumner i Excel med Aspose.Cells for Node.js via C++.
--- 

## **Introduktion**

I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymbolerna**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik som visas nedan i figuren:

|**Gruppering av rader och kolumner.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Grupperingshantering av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling som representerar alla celler i kalkylbladet.

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen ger flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan i mer detalj.

### **Gruppering av rader och kolumner**

Det är möjligt att gruppera rader eller kolumner genom att anropa [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) och [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-)-metoderna i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen. Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Gruppinställningar**

Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.

Utvecklare kan konfigurera dessa gruppinställningar med [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--)-egenskapen i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen.

### **Sammanfattande rader nedanför detalj**

Det är möjligt att kontrollera om sammanfattningsrader visas under detaljer genom att sätta [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline)-klassens [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--)-egenskap till **true** eller **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Sammanfattande kolumner till höger om detalj**

Utvecklare kan också kontrollera visningen av sammanfattningskolumner till höger om detaljer genom att sätta [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--)-egenskapen i [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline)-klassen till **true** eller **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Avgruppering av rader och kolumner**

För att ogruppera några grupperade rader eller kolumner, ring [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingens [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-)- och [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-)-metoder. Båda metoderna tar två parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) har en överbelastning som tar en tredje Boolean-parameter. Att ställa in den till **true** tar bort all gruppinformation. Annars tas bara den yttre gruppinformationen bort.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
