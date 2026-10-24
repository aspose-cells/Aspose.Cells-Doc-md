---
title: Aggiornamento dello slicer
linktitle: Aggiornamento dello slicer
type: docs
weight: 60
url: /it/python-java/updating-slicer/
description: Questo articolo mostra come aggiornare uno slicer per filtrare i dati della Tabella Pivot o della tabella collegata utilizzando l'API Aspose.Cells for Python via Java.
keywords: Aspose.Cells for Python via Java Aggiorna slicer, Python Java aggiornare Slicer, come filtrare una Tabella Pivot tramite slicer in Python, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aggiornamento dello slicer**
Aggiornare uno slicer significa filtrare i dati della Tabella Pivot o della tabella a cui lo slicer è collegato. Aspose.Cells for Python via Java aggiorna lo slicer e ricalcola la Tabella Pivot o la tabella collegata direttamente dagli elementi del filtro:
- `Slicer.selectItems(labels, append)` — seleziona le etichette specificate e ricalcola la Tabella Pivot o la tabella collegata. Quando `append` è `True`, le etichette originariamente selezionate vengono mantenute e le etichette specificate vengono aggiunte alla selezione; quando `append` è `False`, tutte le selezioni originali vengono cancellate e solo le etichette specificate restano selezionate.
- `Slicer.unselectItems(labels)` — deseleziona parte degli elementi attualmente selezionati.
- `Slicer.clearFilter()` — rimuove il filtro e seleziona tutti gli elementi.

{{% alert color="primary" %}}
A partire da Aspose.Cells for Python via Java 26.10, la proprietà `SlicerCacheItem.Selected` diventa di sola lettura e il relativo setter non è più supportato. Utilizzare i metodi `Slicer.selectItems`, `Slicer.unselectItems` e `Slicer.clearFilter` anziché impostare `SlicerCacheItem.Selected` elemento per elemento.
Il seguente frammento di codice carica il [file Excel di esempio](106365050.xlsx) che contiene uno slicer collegato a una Tabella Pivot. Seleziona solo gli elementi "Blue" e "Pink" dello slicer con `Slicer.selectItems(labels, False)` — la Tabella Pivot viene ricalcolata direttamente dagli elementi del filtro, senza una chiamata manuale a `Slicer.refresh()`. Salva quindi la cartella di lavoro come [file Excel di output](106365051.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, la Tabella Pivot mostra solo gli elementi filtrati.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Codice di Esempio**
Sostituire la selezione corrente (restano selezionate solo le etichette specificate) e ricalcolare la Tabella Pivot o la tabella collegata:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Mantenere le etichette attualmente selezionate e selezionare ulteriori elementi:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Deselezionare parte degli elementi selezionati:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Rimuovere il filtro (selezionare tutti gli elementi):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}