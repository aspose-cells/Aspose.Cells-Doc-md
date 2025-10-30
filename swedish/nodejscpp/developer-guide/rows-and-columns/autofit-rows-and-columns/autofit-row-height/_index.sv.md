---
title: Automatiskt anpassa radens höjd vid inläsning av fil med Node.js via C++
linktitle: Autofit radhöjden automatiskt när filen laddas
type: docs
weight: 120
url: /sv/nodejs-cpp/autofit-row-height/
description: Lär dig hur du anpassar höjden på rader som inte är anpassade när du laddar en fil med Aspose.Cells for Node.js via C++.
keywords: Automatiskt anpassa radhöjden vid inläsning av fil Node.js via C++, justera radhöjden automatiskt när du öppnar en Excel fil med Node.js via C++ 
---

## **Möjliga användningsscenario**
Rowhöjden matchar automatiskt teckensnittet för innehållet, men när höjden på den cachelagrade raden inte matchar höjden på innehållet i filen, kommer MS Excel automatiskt att justera radhöjden när filen laddas, medan Aspose.Cells for Node.js via C++ inte automatiskt justerar den för att förbättra prestandan. Om du behöver använda Aspose.Cells-programmet för att automatiskt matcha radhöjder vid filinläsning kan du åstadkomma detta genom parametern [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) i din kod.

Vänligen referera till följande bilddata. Vi kan observera att den cachelagrade radhöjden i rad 11 är 15, men Excel justerade automatiskt radhöjden när filen laddades.
<br>
<img src="1.png" width=70% />

## **Justera radhöjd med Aspose.Cells for Node.js via C++**
Om du laddar filen direkt och sparar den som PDF, kommer datan inte att visas helt i PDF eftersom dess cachelagrade radhöjd är endast 15.
<br>
<img src="2.png" width=70% />
<br>
Om du ställer in parametern [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) till true vid inläsning av filen, kommer Aspose.Cells automatiskt att justera radhöjden. Den justerade radhöjden kan effektivt möta textens visningskrav.
<br>
<img src="3.png" width=70% />

## **Node.js exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
