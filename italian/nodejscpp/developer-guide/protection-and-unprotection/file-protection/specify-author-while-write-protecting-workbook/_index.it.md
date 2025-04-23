---  
title: Specificare l autore durante la protezione in scrittura del workbook con Node.js tramite C++  
linktitle: Specificare l autore durante la protezione in scrittura del libro di lavoro  
type: docs  
weight: 40  
url: /it/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Specificare un nome autore durante la protezione in scrittura di un workbook usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**

Puoi specificare un nome autore durante la protezione in scrittura del tuo workbook usando l'API Aspose.Cells. Usa la proprietà [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) per questo scopo.

## **Specificare l'autore durante la protezione in scrittura del workbook**

Il codice di esempio seguente illustra l'uso della proprietà [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--). Il codice crea un workbook vuoto, lo protegge con una password, specifica il nome dell'autore e lo salva come [file Excel in output](67338582.xlsx). La schermata seguente illustra l'effetto del codice di esempio sul file Excel in output per tua referenza.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

