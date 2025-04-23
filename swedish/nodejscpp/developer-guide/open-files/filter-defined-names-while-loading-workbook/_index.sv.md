---
title: Filtrera definierade namn vid inläsning av arbetsbok med Node.js via C++
linktitle: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig filtrera eller ta bort definierade namn som finns i arbetsboken. Vänligen använd [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) för att ladda definierade namn och [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) för att ta bort dem vid inläsning av arbetsboken. Observera, om du tar bort definierade namn kan formlerna i arbetsboken gå sönder.

## **Filtrera Definierade namn vid inläsning av arbetsbok**

Följande exempel laddar [exempel Excel-fil](61767860.xlsx) som har en formel i cell **C1** som innehåller de definierade namnen, dvs. *=SUM(MyName1, MyName2)*. Eftersom vi använder [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) för att ta bort de definierade namnen vid inläsning av arbetsboken, bryts formeln i cell C1 i [utgångs Excel-fil](61767861.xlsx) och du ser *#NAME?* istället. Se skärmbilden nedan som visar hur koden påverkar exempel-Excel-filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
