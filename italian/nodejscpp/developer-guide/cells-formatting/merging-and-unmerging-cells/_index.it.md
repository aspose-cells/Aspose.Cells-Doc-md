---
title: Unisci e separa le celle con Node.js tramite C++
linktitle: Unione e separazione di celle
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo, che supporta la fusione e l unione delle celle. Questo articolo introdurrà come unire e separare le celle usando la libreria Aspose.Cells, con opzioni per personalizzare lo stile della cella unita.
keywords: Aspose.Cells, libreria Node.js, foglio di calcolo, unire celle, separare celle, impostazioni di stile, stili personalizzati
type: docs
weight: 190
url: /it/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta questa funzionalità e può anche unire celle in un foglio di lavoro. È possibile anche separare o dividere le celle unite. Il riferimento della cella unita è il riferimento per la cella in alto a sinistra nell'intervallo selezionato originale.

{{% /alert %}} 
## **Introduzione**
Non si desidera sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, si potrebbe voler inserire un titolo in una cella che si estende su diverse colonne. Oppure, se si crea una fattura, potrebbe essere necessario meno colonne per il totale. Per rendere una cella da due o più celle, unirle. Microsoft Excel consente agli utenti di selezionare i file e unirli per strutturare il foglio di calcolo nel modo desiderato.

{{% alert color="primary" %}} 

Nota che quando le celle sono unite, vengono conservati solo i dati nella cella in alto a sinistra. Se ci sono dati nelle altre celle dell'intervallo, questi dati vengono eliminati. La formattazione, allo stesso modo, si basa sulla cella di riferimento in modo che, quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengono applicate sulla cella unita. Quando la cella viene divisa, le nuove celle mantengono le impostazioni di formattazione originali.

{{% /alert %}} 
## **Unione di celle in un foglio di lavoro**
### **Unione di celle in Microsoft Excel**
I seguenti passaggi descrivono come unire celle nel foglio di lavoro utilizzando MS Excel.

1. Copiare i dati che si desidera nella cella in alto a sinistra nell'intervallo.
1. Selezionare le celle che si desidera unire.
1. Per unire le celle in una riga o colonna e centrare i contenuti della cella, fare clic sull'icona **Unisci e centrato** sulla barra degli strumenti **Formattazione**.

### **Unione di celle con Aspose.Cells**
La classe Aspose.Cells.Cells dispone di alcuni metodi utili per il compito. Ad esempio, il metodo `merge()` unisce le celle in una singola cella all'interno di un intervallo specificato.

Nell'esempio seguente viene mostrato come unire le celle (C6:E7) in un foglio di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Dividere (Separare) celle unite**
### **Utilizzando Microsoft Excel**
I seguenti passaggi descrivono come dividere le celle unite usando Microsoft Excel.

1. Seleziona la cella unita.
   Quando le celle sono state unite, **Unisci e centra** è selezionato sulla barra degli strumenti **Formattazione**.
1. Fai clic su **Unisci e centra** sulla barra degli strumenti **Formattazione**.

### **Usare Aspose.Cells**
La classe Aspose.Cells.Cells ha un metodo chiamato `unmerge()` che divide le celle nel loro stato originale. Il metodo divide le celle utilizzando il riferimento della cella all'interno dell'intervallo di celle unito.

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio utilizza il file creato nel precedente esempio e divide le celle unite.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Argomenti avanzati**
- [Rileva le celle unite in un foglio di lavoro](/cells/it/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
