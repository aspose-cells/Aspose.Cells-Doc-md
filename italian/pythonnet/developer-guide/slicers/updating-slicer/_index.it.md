---
title: Aggiornamento dello slicer
linktitle: Aggiornamento dello slicer
type: docs
weight: 50
url: /it/python-net/updating-slicer/
description: Scopri come aggiornare uno slicer per filtrare i dati della Tabella Pivot o della tabella collegata con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, libreria Excel Python, Python aggiornare Slicer senza Excel, filtrare una Tabella Pivot tramite slicer in Python, Slicer select_items, Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili Scenari di Utilizzo**
Aggiornare uno slicer significa filtrare i dati della Tabella Pivot o della tabella a cui lo slicer è collegato. Quando si selezionano o si deselezionano gli elementi dello slicer in Microsoft Excel, la Tabella Pivot o la tabella collegata viene ricalcolata di conseguenza. Con Aspose.Cells for Python via .NET, non è necessario iterare gli elementi della cache dello slicer e aggiornare manualmente lo slicer — il metodo [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) aggiorna lo slicer e ricalcola la Tabella Pivot o la tabella collegata direttamente dagli elementi del filtro:
- `Slicer.select_items(labels, append)` — seleziona le etichette specificate e ricalcola la Tabella Pivot o la tabella collegata. Quando `append` è `True`, le etichette originariamente selezionate vengono mantenute e le etichette specificate vengono aggiunte alla selezione; quando `append` è `False`, tutte le selezioni originali vengono cancellate e solo le etichette specificate restano selezionate.
- `Slicer.unselect_items(labels)` — deseleziona parte degli elementi attualmente selezionati.
- `Slicer.clear_filter()` — rimuove il filtro e seleziona tutti gli elementi.

{{% alert color="primary" %}}
A partire da Aspose.Cells for Python via .NET 26.10, la proprietà `SlicerCacheItem.selected` diventa di sola lettura e il relativo setter non è più supportato. Utilizzare i metodi `Slicer.select_items`, `Slicer.unselect_items` e `Slicer.clear_filter` anziché impostare `SlicerCacheItem.selected` elemento per elemento.
{{% /alert %}}

## **Come aggiornare uno slicer utilizzando la libreria Excel Aspose.Cells for Python**
Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene uno slicer esistente collegato a una Tabella Pivot. Seleziona solo gli elementi "Blue" e "Pink" dello slicer con `Slicer.select_items(labels, False)` — la Tabella Pivot viene ricalcolata direttamente dagli elementi del filtro, senza una chiamata manuale a `Slicer.refresh()`. Salva quindi la cartella di lavoro come [file Excel di output](67338476.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, la Tabella Pivot mostra solo gli elementi filtrati.
![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**
Sostituire la selezione corrente (restano selezionate solo le etichette specificate) e ricalcolare la Tabella Pivot o la tabella collegata:

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

Mantenere le etichette attualmente selezionate e selezionare ulteriori elementi:

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

Deselezionare parte degli elementi selezionati:

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

Rimuovere il filtro (selezionare tutti gli elementi):

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}