---
title: Filtrera VBA projekt vid laddning av en arbetsbok med Node.js via C++
linktitle: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 140
url: /sv/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Lär dig hur du filtrerar VBA projekt när du laddar Excel arbetsböcker med Aspose.Cells for Node.js via C++.
---

## **Filtrera VBA-projekt vid laddning av en Excel-arbetsbok i Node.js via C++**

Vissa .xlsm/.xslb-filer har extremt mycket makron (eller mycket, mycket långa makron). Aspose.Cells for Node.js via C++ laddar ovillkorligen dessa (meta)data när du öppnar sådana arbetsböcker. Du kan behöva kontrollera detta via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) när du verkligen bara behöver extrahera bladnamnen för ett stort antal arbetsböcker, och därigenom hoppa över sådant onödigt innehåll. Denna filterfunktion tillhandahålls genom att introducera ett nytt alternativ, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).

## **Exempelkod**

Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. En testfil för att testa denna funktion kan hämtas från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
