---
title: Determina se la dimensione carta del foglio di lavoro è automatica con Node.js tramite C++
linktitle: Determina se la dimensione carta del foglio di lavoro è automatica
type: docs
weight: 90
url: /it/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Questo articolo spiega come usare l API Node.js con addon C++ per determinare se la dimensione della carta di un foglio di lavoro è impostata su automatica programmaticamente.
keywords: Determina se la dimensione della carta del foglio di lavoro è automatica con Node.js tramite C++
---

## **Possibili Scenari di Utilizzo**

La maggior parte delle volte, la dimensione del foglio del foglio di lavoro è automatica. Quando è automatica, è spesso impostata come *Letter*. A volte l'utente setta la dimensione della carta del foglio di lavoro secondo le proprie esigenze. In questo caso, la dimensione della carta non è automatica. Puoi verificare se la dimensione della carta del foglio di lavoro è automatica o meno usando la proprietà [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--).

## **Determina se le dimensioni del foglio di lavoro sono automatiche**

Il codice di esempio riportato di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

e verifica se la dimensione carta del loro primo foglio di lavoro è automatica o meno. In Microsoft Excel, puoi verificare se la dimensione carta è automatica o meno tramite la finestra Impostazioni pagina come mostrato in questa immagine.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice di Esempio**

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

## **Output della console**

Ecco l'output sulla console del codice di esempio sopra quando eseguito con i file Excel di esempio forniti.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
