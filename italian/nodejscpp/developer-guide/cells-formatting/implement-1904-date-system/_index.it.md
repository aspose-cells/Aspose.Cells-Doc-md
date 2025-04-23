---
title: Implementa il sistema di data 1904 con Node.js tramite C++
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo. Supporta l implementazione del sistema di data 1904, consentendo agli utenti di calcolare e formattare in base al sistema di data del 1 gennaio 1904. Questo articolo descrive come implementare il sistema di data 1904 usando la libreria Aspose.Cells.
keywords: Aspose.Cells, sistema di data 1904, foglio di calcolo, calcolo, formattazione, Node.js tramite C++
type: docs
weight: 7000
url: /it/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel supporta due sistemi di data: il sistema di data 1900 (il sistema di data predefinito implementato in Excel per Windows) e il sistema di data 1904. Il sistema di data 1904 viene normalmente usato per garantire la compatibilità con i file Excel per Macintosh ed è il sistema predefinito se si usa Excel per Macintosh. È possibile impostare il sistema di data 1904 per i file Excel utilizzando Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

Per implementare il sistema di data 1904 in Microsoft Excel (ad esempio, Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**, e selezionare la scheda **Calcolo**.
1. Selezionare l'opzione **sistema di data del 1904**.
1. Fai clic su **OK**.

|**Selezione del sistema di data del 1904 in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Vedere il seguente codice di esempio su come realizzare questo utilizzando le API di Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
