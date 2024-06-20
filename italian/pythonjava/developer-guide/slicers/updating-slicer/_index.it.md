---
title: Aggiornamento Slicer
type: docs
weight: 60
url: /it/python-java/updating-slicer/
---

## **Aggiornamento dello slicer**
Aspose.Cells for Python via Java supporta l'aggiornamento degli slicer. A questo scopo, l'API fornisce la proprietà Slicer.SlicerCache.SlicerCacheItems che viene utilizzata per selezionare o deselezionare gli elementi dello slicer. Il seguente frammento di codice carica il [file di esempio Excel](106365050.xlsx) che contiene uno slicer. Deseleziona il 2° e 3° elemento dello slicer e aggiorna lo slicer utilizzando il metodo Slicer.refresh(). Quindi salva il documento di lavoro come [file Excel di output](106365051.xlsx). La seguente schermata mostra l'effetto del codice di esempio sul file Excel di esempio. Come si può vedere nella schermata, l'aggiornamento dello slicer con elementi selezionati ha anche aggiornato la tabella pivot di conseguenza.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
