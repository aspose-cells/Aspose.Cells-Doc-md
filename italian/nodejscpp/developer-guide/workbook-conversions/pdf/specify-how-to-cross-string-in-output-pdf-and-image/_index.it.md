---  
title: Specifica come attraversare le stringhe in output PDF e immagini con Node.js tramite C++  
linktitle: Specifica come incrociare la stringa in PDF ed immagine di output  
type: docs  
weight: 120  
url: /it/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Impara a controllare il trabocco del testo in PDF/Image di output specificando il tipo di attraversamento usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o una stringa ma è più larga della larghezza della cella, allora la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in PDF/Image, puoi controllare questo trabocco specificando il tipo di attraversamento usando l'enumerazione [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Ha i seguenti valori:

- **TextCrossType.Default**: Visualizza il testo come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa attraverserà o sarà troncata.

- **TextCrossType.CrossKeep**: visualizza la stringa come MS Excel esportando in PDF/Immagine.

- **TextCrossType.CrossOverride**: visualizza tutto il testo attraversando le altre celle e sovrascrive il testo delle celle attraversate.

- **TextCrossType.StrictInCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF / Immagine di output utilizzando TextCrossType**

Il seguente esempio di codice carica il file Excel di esempio e lo salva in formato PDF/Immagine specificando vari [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Il file Excel di esempio e i file di output possono essere scaricati dai link seguenti:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Codice di esempio

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
