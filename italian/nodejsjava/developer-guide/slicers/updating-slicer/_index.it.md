---
title: Aggiornamento dello slicer con Node.js tramite Java
linktitle: Aggiornamento dello slicer
type: docs
weight: 50
url: /it/nodejs-java/updating-slicer/
description: Questo articolo mostra come aggiornare uno slicer per filtrare i dati della Tabella Pivot o della tabella collegata utilizzando Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells Node.js via Java, Aggiorna slicer Node.js, come cambiare lo slicer Node.js, come filtrare una Tabella Pivot tramite slicer in Node.js, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili Scenari di Utilizzo**
Aggiornare uno slicer significa filtrare i dati della Tabella Pivot o della tabella a cui lo slicer è collegato. Quando si selezionano o si deselezionano gli elementi dello slicer in Microsoft Excel, la Tabella Pivot o la tabella collegata viene ricalcolata di conseguenza. Con Aspose.Cells for Node.js via Java, non è necessario iterare gli elementi della cache dello slicer e aggiornare manualmente lo slicer — il metodo [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs/slicer/) aggiorna lo slicer e ricalcola la Tabella Pivot o la tabella collegata direttamente dagli elementi del filtro:
- `Slicer.selectItems(labels, append)` — seleziona le etichette specificate e ricalcola la Tabella Pivot o la tabella collegata. Quando `append` è `true`, le etichette originariamente selezionate vengono mantenute e le etichette specificate vengono aggiunte alla selezione; quando `append` è `false`, tutte le selezioni originali vengono cancellate e solo le etichette specificate restano selezionate.
- `Slicer.unselectItems(labels)` — deseleziona parte degli elementi attualmente selezionati.
- `Slicer.clearFilter()` — rimuove il filtro e seleziona tutti gli elementi.

{{% alert color="primary" %}}
A partire da Aspose.Cells for Node.js via Java 26.10, la proprietà `SlicerCacheItem.Selected` diventa di sola lettura e il relativo setter non è più supportato. Utilizzare i metodi `Slicer.selectItems`, `Slicer.unselectItems` e `Slicer.clearFilter` anziché impostare `SlicerCacheItem.Selected` elemento per elemento.
{{% /alert %}}

## **Come aggiornare lo slicer**
Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene uno slicer esistente collegato a una Tabella Pivot. Seleziona solo gli elementi "Blue" e "Pink" dello slicer con `Slicer.selectItems(labels, false)` — la Tabella Pivot viene ricalcolata direttamente dagli elementi del filtro, senza una chiamata manuale a `Slicer.refresh()`. Salva quindi la cartella di lavoro come [file Excel di output](67338476.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, la Tabella Pivot mostra solo gli elementi filtrati.
![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**
Sostituire la selezione corrente (restano selezionate solo le etichette specificate) e ricalcolare la Tabella Pivot o la tabella collegata:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Mantenere le etichette attualmente selezionate e selezionare ulteriori elementi:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Deselezionare parte degli elementi selezionati:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Rimuovere il filtro (selezionare tutti gli elementi):

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-java" >}}