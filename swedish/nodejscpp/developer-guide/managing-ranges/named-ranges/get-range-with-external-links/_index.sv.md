---
title: Hämta område med externa länkar med Node.js via C++
linktitle: Hämta intervall med externa länkar
type: docs
weight: 120
url: /sv/nodejs-cpp/get-range-with-external-links/
description: Lär dig hur man hämtar områden med externa länkar med Aspose.Cells for Node.js via C++. Hämta data från olika Excel filer effektivt.
---

## **Hämta intervall med externa länkar**

Många gånger öppnar Excel-filer data från andra Excel-filer med hjälp av externa länkar. Aspose.Cells for Node.js via C++ ger möjlighet att hämta dessa externa länkar med hjälp av [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-)-metoden. [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-)-metoden returnerar en array av typen [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea)-klassen tillhandahåller en [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--)-egenskap som returnerar namnet på den externa filen. [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea)-klassen exponerar följande medlemmar.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): ändens kolumn för området
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): ändens rad för området
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Hämta det externa filnamnet om detta är en extern referens
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Indikerar om detta är ett område
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Indikerar om detta är en extern länk
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Indikerar vilken bladreferens detta är i
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): Startkolumn för området
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): Startrad för området

Kodexemplet nedan visar hur man använder [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) metoden för att hämta områden med externa länkar.

## **Exempelkod**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
