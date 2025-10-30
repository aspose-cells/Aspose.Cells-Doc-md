---
title: Hur man skriver ut Excel som anpassade sidor brett och högt med Node.js via C++
linktitle: Hur man skriver ut Excel som anpassade sidor breda och höga
type: docs
weight: 200
url: /sv/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Den här artikeln visar dig kod som förklarar hur man ställer in FitToPagesWide och FitToPagesTall med Aspose.Cells for Node.js via C++.
keywords: Node.js via C++ Hur man ställer in FitToPagesWide och FitToPagesTall, Hur man lägger till FitToPagesWide och FitToPagesTall i Node.js, Hur man ställer in FitToPagesWide och FitToPagesTall i Excel, Hur man rensar FitToPagesWide och FitToPagesTall i Excel, Hur man skriver ut Excel som anpassade sidor breda och höga, Hur man skriver ut arbetsblad som en sida, Hur man skriver ut alla kolumner i arbetsbladet på en sida.
---

## **Introduktion**

FitToPagesWide och FitToPagesTall-inställningarna används i kalkylprogram (som Microsoft Excel) för att styra hur ett kalkylblad skalas när det skrivs ut. Dessa inställningar hjälper till att säkerställa att ditt utskrivna utskriftsresultat passar inom ett specificerat antal sidor, både horisontellt och vertikalt. Här är en översikt av varje inställning:

1. FitToPagesWide: Denna inställning specificerar antalet sidor brett som utskriften ska passa in i. Till exempel, att ställa in FitToPagesWide till 1 innebär att innehållet skalas för att passa inom en enkel sidbredde, oavsett hur brett kalkylbladet är.
2. FitToPagesTall: Denna inställning anger antalet sidor högt som den utskrivna versionen ska passa in i. Till exempel, att sätta FitToPagesTall till 1 innebär att innehållet skalas för att passa inom en sidhöjd, oavsett antalet rader.

## **Varför använda FitToPagesWide och FitToPagesTall**
Här är några skäl att ställa in FitToPagesWide och FitToPagesTall:
1. Kontroll över utskriftslayout: Genom att specificera antalet sidor brett och högt kan du säkerställa att din utskrivna dokument är lätt att läsa och välorganiserad, utan att kolumner eller rader delas på ett oönskat sätt över sidor.
2. Konsistens: Om du skriver ut flera blad eller rapporter hjälper användningen av dessa inställningar att bibehålla ett konsekvent format, vilket gör det lättare att jämföra och analysera utskrivna dokument.
3. Professionell presentation: Att korrekt skalas och anpassa innehåll till ett specificerat antal sidor kan leda till en mer professionell och polerad presentation av dina data.

## **Hur man skriver ut filen som anpassade sidor breda och höga i Excel**

För att ställa in FitToPagesWide och FitToPagesTall i Microsoft Excel, följ dessa steg:

1. Öppna ditt Excel-arbetsbok och gå till det blad du vill skriva ut.
2. Gå till fliken Sidlayout i menyfliksområdet.
3. I gruppen Sidformat klickar du på den lilla pilen i nedre högra hörnet för att öppna dialogrutan Sidformat.
4. I dialogrutan Sidformat går du till fliken Utsida.
5. Under Skalning väljer du alternativet "Anpassa till" och anger sedan antalet sidor brett och högt du vill: Skriv in antalet sidor brett du vill i den första rutan (Anpassa till x sidor brett). Skriv in det antal sidor högt du vill i den andra rutan (Anpassa till y sidor högt).
<br>
<img src="2.png" width=60% />

6. Klicka på OK för att tillämpa inställningarna.

## **Hur man skriver ut Excel som anpassade sidor breda och höga med Aspose.Cells for Node.js via C++**

För att ställa in FitToPagesWide och FitToPagesTall i ett specifikt blad: först, ladda [exempel fil](input.xlsx), och sedan måste du ändra [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) och [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) egenskaperna hos objektet [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) för önskat blad. Här är ett exempel i Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Hur man skriver ut arbetsblad som en sida med Aspose.Cells for Node.js via C++**

För att skriva ut arbetsblad som en sida: först, ladda [exempel fil](sample.xlsx), och sedan måste du ställa in egenskapen [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) för objektet [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Här är ett exempel i Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

Utmatningsresultat:
<br>
<img src="3.png" width=60% />

## **Hur man skriver ut alla kolumner i arbetsblad på en sida med Aspose.Cells for Node.js via C++**

För att skriva ut alla kolumner i arbetsbladet på en sida: först, ladda [exempel fil](sample.xlsx), och sedan måste du ställa in egenskapen [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) för objektet [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Här är ett exempel i Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

Utmatningsresultat:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
