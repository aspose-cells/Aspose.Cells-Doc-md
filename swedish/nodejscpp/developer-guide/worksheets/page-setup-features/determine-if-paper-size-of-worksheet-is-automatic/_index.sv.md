---
title: Avgör om pappersstorleken för arbetsbladet är Automatisk med Node.js via C++
linktitle: Bestäm om Papper Storleken på Arbetsbladet är Automatisk
type: docs
weight: 90
url: /sv/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Denna artikel förklarar hur man använder Node.js API med C++ tillägg för att bestämma om pappersstorleken för ett arbetsblad är inställd på automatisk programmässigt.
keywords: avgör om pappersstorleken för arbetsbladet är automatisk Node.js via C++
---

## **Möjliga användningsscenario**

Det mesta av tiden är pappersstorleken för arbetsbladet automatisk. När den är automatisk är den ofta inställd på *Letter*. Ibland ställer användaren in pappersstorleken på arbetsbladet efter sina behov. I detta fall är pappersstorleken inte automatisk. Du kan ta reda på om arbetsbladets pappersstorlek är automatisk eller inte med hjälp av [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--)-egenskapen.

## **Avgöra om sidstorleken för arbetsbladet är automatisk**

Den provkod som ges nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

och ta reda på om papperstorleken på deras första arbetsblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om papperstorleken är automatisk eller inte via fönstret Sidlayout som visas i denna skärmbild.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **Konsoloutput**

Här är konsolutdata från ovanstående provkod när den körs med de angivna provexelfilerna.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
