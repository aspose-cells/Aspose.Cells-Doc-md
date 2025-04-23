---  
title: Formattare uno Slicer con Node.js tramite C++  
linktitle: Formattazione del filtro  
type: docs  
weight: 20  
url: /it/nodejs-cpp/formatting-slicer/  
---  

## **Possibili Scenari di Utilizzo**  

Puoi formattare lo slicer in Microsoft Excel impostando il numero di colonne o impostando lo stile ecc. Aspose.Cells for Node.js via C++ ti permette anche di farlo utilizzando le proprietà [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) e [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--).  

## **Formattazione del selettore**  

Si prega di vedere il seguente codice, carica il [file Excel di esempio](67338473.xlsx) che contiene un slicer. Accede quindi al slicer e imposta il numero di colonne e il tipo di stile e lo salva come [file Excel di output](67338474.xlsx). La schermata mostra come appare il slicer dopo l'esecuzione del codice di esempio.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

