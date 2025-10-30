---
title: Ottieni la larghezza e l altezza della pagina nella configurazione pagina del foglio di lavoro con Node.js tramite C++
linktitle: Ottieni larghezza e altezza della carta della configurazione della pagina del foglio di lavoro
type: docs
weight: 50
url: /it/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Scopri come ottenere la larghezza e l altezza della pagina nella configurazione pagina del foglio di lavoro Excel usando Node.js tramite C++ programmaticamente.
keywords: larghezza e altezza della pagina della configurazione pagina di Excel Node.js tramite C++, larghezza e altezza della pagina della configurazione pagina di Excel Node.js tramite C++
---

## **Possibili Scenari di Utilizzo**

A volte devi conoscere la larghezza e l'altezza della carta impostata nella configurazione pagina del foglio di lavoro. Usa le proprietà [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) e [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) a questo scopo.

## **Ottenere larghezza e altezza della pagina di configurazione del foglio di lavoro**

Il seguente esempio di codice spiega come usare le proprietà [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) e [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). Innanzitutto cambia la dimensione della carta in *A2* e poi trova la larghezza e l'altezza della carta, quindi la cambia in *A3*, *A4*, *Letter* e trova rispettivamente la larghezza e l'altezza della carta.

### **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Output della console**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
