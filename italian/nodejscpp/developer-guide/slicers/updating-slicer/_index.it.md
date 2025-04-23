---
title: Aggiornamento Slicer con Node.js tramite C++
linktitle: Aggiornamento Slicer
type: docs
weight: 50
url: /it/nodejs-cpp/updating-slicer/
description: Questo articolo mostra come aggiornare le tabelle pivot collegate aggiornando lo slicer usando Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js tramite C++, Aggiorna slicer Node.js, come cambiare lo slicer Node.js, come regolare lo slicer in Node.js, come selezionare o deselezionare gli elementi dello slicer Node.js tramite C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi aggiornare uno slicer in Microsoft Excel, seleziona o deseleziona i suoi elementi, e aggiornará di conseguenza la tabella dello slicer o la tabella pivot. Per favore usa [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) per selezionare o deselezionare gli elementi dello slicer con Aspose.Cells e poi chiama il metodo [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) per aggiornare la tabella dello slicer o la tabella pivot.

## **Come aggiornare il riquadro di selezione**

Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene un filtro esistente. Deseleziona il 2° e 3° elemento del filtro e aggiorna il filtro. Quindi salva il lavoro come [file Excel di output](67338476.xlsx). La seguente schermata mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, l'aggiornamento del filtro con gli elementi selezionati ha anche aggiornato la tabella pivot di conseguenza.

![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
