---
title: Rimozione Slicer con Node.js tramite C++
linktitle: Rimozione del filtro
type: docs
weight: 30
url: /it/nodejs-cpp/removing-slicer/
---

## **Possibili Scenari di Utilizzo**

Se vuoi rimuovere uno slicer in Excel, selezionalo e premi il pulsante *Elimina*. In modo simile, se desideri rimuoverlo utilizzando l'API Aspose.Cells programmaticamente, utilizza il metodo [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-). Rimuoverà lo slicer dal foglio di lavoro.

## **Rimozione dello slicer**

Il seguente esempio di codice carica il [file Excel di esempio](67338478.xlsx) che contiene uno slicer esistente. Lo accede e poi lo rimuove. Infine, salva il workbook come [file Excel di output](67338477.xlsx). La schermata seguente mostra lo slicer che verrà rimosso dopo l'esecuzione dell'esempio di codice.

![todo:image_alt_text](removing-slicer_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
