---
title: Caratteristiche di impostazione pagina con Node.js tramite C++
linktitle: Caratteristiche della configurazione pagina
type: docs
weight: 60
url: /it/nodejs-cpp/page-setup-features/
description: Esplora le caratteristiche di impostazione pagina usando Aspose.Cells for Node.js via C++. Impara come configurare dimensioni pagina, orientamenti e impostazioni.
keywords: Caratteristiche di impostazione pagina Node.js tramite C++, configura dimensioni pagina Node.js tramite C++, impostazioni di orientamento pagina Node.js tramite C++
---



## **Introduzione**
Con Aspose.Cells for Node.js via C++, puoi manipolare varie caratteristiche di impostazione pagina di un workbook Excel. Queste caratteristiche includono la configurazione della dimensione della pagina, orientamento, margini e altro. Una corretta configurazione di queste caratteristiche permette una migliore esperienza di stampa e visualizzazione.

## **Imposta dimensione e orientamento della pagina**
Puoi specificare la dimensione e l'orientamento della pagina di un foglio di lavoro utilizzando la classe `PageSetup`. Fornisce varie proprietà per gestire le dimensioni della pagina e il layout.

### **Codice di esempio**
Ecco un esempio di codice che dimostra come impostare la dimensione e l'orientamento della pagina.

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **Impostazione margini**
Puoi anche impostare i margini della pagina utilizzando la stessa classe `PageSetup`. I margini possono essere regolati per il lato sinistro, destro, superiore e inferiore.

### **Codice di esempio**
Ecco come puoi impostare i margini di un foglio di lavoro.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **Conclusioni**
In questo documento, hai imparato come manipolare le funzioni di configurazione della pagina in Excel usando Aspose.Cells for Node.js via C++. Utilizzando efficacemente la classe `PageSetup`, puoi controllare come vengono stampati e visualizzati i tuoi fogli di lavoro, migliorando la presentazione generale delle informazioni.

---
