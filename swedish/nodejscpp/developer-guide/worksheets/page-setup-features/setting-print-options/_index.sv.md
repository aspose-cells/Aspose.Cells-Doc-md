---
title: Inställning av utskriftsalternativ med Node.js via C++
linktitle: Inställning av utskriftsalternativ
type: docs
weight: 40
url: /sv/nodejs-cpp/setting-print-options/
description: Denna artikel demonstrerar hur man programmässigt ställer in utskriftsalternativen för bladets sidupplägg i Excel via Node.js API och C++ bibliotek. Du kan ställa in utskriftsområde, utskriftstitlar och sidordning.
keywords: ställa in excel utskriftsområde Node.js via C++, ställa in excel utskriftstitlar Node.js via C++, ställa in excel sidordning Node.js via C++
---

{{% alert color="primary" %}}

Microsoft Excels sidoinställningsinställningar ger flera utskriftsalternativ (även kallade kalkylblad) som låter användare styra hur kalkylbladssidor skrivs ut.

{{% /alert %}}

## **Ställa in utskriftsalternativ**

Dessa utskriftsalternativ låter användare:

- Välja ett specifikt utskriftsområde på en arbetsbok.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Aspose.Cells for Node.js via C++ stöder alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för blad med hjälp av egenskaperna i [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)-klassen. Hur dessa egenskaper används diskuteras nedan mer i detalj.

### **Ange utskriftsområde**

Som standard omfattar utskriftsområdet alla områden på kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde för kalkylbladet.

För att välja ett specifikt utskriftsområde, använd egenskapen [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) i klassen [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Ställ in utskriftstitlar**

Aspose.Cells låter dig ange att rad- och kolumnrubriker ska upprepas på alla sidor av en utskriven arbetsbok. Gör så genom att använda egenskaperna [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) och [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) i klassen [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Ange andra utskriftsalternativ**

Klassen [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) tillhandahåller också flera andra egenskaper för att ange allmänna utskriftsalternativ enligt följande:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): en boolesk egenskap som definierar om rutnätslinjer ska skrivas ut eller inte.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): en boolesk egenskap som definierar om bladet ska skrivas ut i svartvitt eller inte.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): anger vilken utskriftskommentarerna ska visas på kalkbladet eller i slutet av kalkbladet.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): en boolesk egenskap som anger om bladet ska skrivas ut utan grafik.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): definierar om cellfel ska skrivas ut som visas, tom, streck eller N/A.

För att ställa in egenskaperna [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) och [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) ger Aspose.Cells for Node.js via C++ också två uppräknade typer, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) och [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype), som innehåller fördefinierade värden att tilldela egenskaperna [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) och [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--).

De fördefinierade värdena i uppräkningen [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) listas nedan med deras beskrivningar.

|**Kommentarstyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintInPlace|Specificerar att skriva ut kommentarer som visas på kalkylbladet.|
|PrintNoComments|Specificerar att inte skriva ut kommentarer.|
|PrintSheetEnd|Specificerar att skriva ut kommentarer i slutet av kalkylbladet.|

De fördefinierade värdena för uppräkningen [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) listas nedan med deras beskrivningar.

|**Feltyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintErrorsBlank|Anger inte att skriva ut felmeddelanden.|
|PrintErrorsDash|Anger att skriva ut fel som "--".|
|PrintErrorsDisplayed|Anger att skriva ut fel som visas.|
|PrintErrorsNA|Anger att skriva ut fel som "#N/A".|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Ange sidordning**

Klassen [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) tillhandahåller egenskapen [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) som används för att ordna flera sidor av ditt kalkblad som ska skrivas ut. Det finns två möjligheter att ordna sidorna på följande sätt.

- **Nedåt sedan över:** skriver ut alla sidor nedåt innan några sidor till höger skrivs ut.
- **Över sedan nedåt:** skriver sidor från vänster till höger innan sidorna nedanför skrivs ut.

Aspose.Cells tillhandahåller en uppräkning, [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) som innehåller alla fördefinierade typer av ordningar.

De fördefinierade värdena för uppräkningen [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) listas nedan.

|**Utskriftsordningstyper**|**Beskrivning**|
| :- | :- |
|DownThenOver|Representerar utskriftsordning nedåt och sedan över.|
|OverThenDown|Representerar utskriftsordning över och sedan nedåt.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
