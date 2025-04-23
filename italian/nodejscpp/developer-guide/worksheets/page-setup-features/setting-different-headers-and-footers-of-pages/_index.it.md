---
title: Impostare intestazioni e piè di pagina diverse per pagine diverse con Node.js tramite C++
linktitle: Impostazione di diversi intestazioni e piè di pagina per pagine diverse
type: docs
weight: 35
url: /it/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Questo articolo fornisce un esempio di codice che mostra come impostare programmaticamente intestazioni e piè di pagina della configurazione pagina del foglio Excel usando Aspose.Cells for Node.js via C++. Imposta intestazioni e piè di pagina per le prime, le pagine dispari e le pagine pari.
keywords: imposta intestazione piè di pagina Excel prima pagina Node.js tramite C++, imposta intestazione piè di pagina Excel pagine dispari Node.js tramite C++, imposta intestazione piè di pagina Excel pagine pari Node.js tramite C++
---

{{% alert color="primary" %}}

 MS Excel supporta la possibilità di impostare intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e le pagine pari dall'Excel 2007.
Aspose.Cells for Node.js via C++ supporta la stessa funzionalità.

{{% /alert %}}

## **Impostazione di Intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di Intestazioni e piè di pagina diversi](difpage.png)**

1. Fare clic su **Layout di pagina > Titoli di stampa > Intestazione/piè di pagina**.
1. Seleziona **Pagine dispari e pari diverse** o **Prima pagina diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## **Impostare intestazioni e piè di pagina diverse con Aspose.Cells for Node.js via C++**

Aspose.Cells si comporta allo stesso modo di Excel.
1. Imposta i flag [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) e [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Inserisci intestazioni e piè di pagina diversi.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
