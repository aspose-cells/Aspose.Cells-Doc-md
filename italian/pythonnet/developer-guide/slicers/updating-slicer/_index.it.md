---
title: Aggiornamento dell'affettatrice
type: docs
weight: 50
url: /it/python-net/updating-slicer/
---
##  **Possibili scenari di utilizzo**

Se desideri aggiornare l'affettatrice in Microsoft Excel, seleziona o deseleziona i suoi elementi, quindi aggiornerà di conseguenza la tabella dell'affettatrice o la tabella pivot. Si prega di utilizzare[**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/)per selezionare o deselezionare gli elementi dell'affettatrice con Aspose.Cells for Python via .NET e poi chiamare[**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)metodo per aggiornare la tabella dei dati o la tabella pivot.

##  **Aggiornamento dell'affettatrice**

 Il codice di esempio seguente carica il file[file Excel di esempio](67338475.xlsx) che contiene un'affettatrice esistente. Deseleziona il 2° e il 3° elemento dell'affettatrice e aggiorna l'affettatrice. Quindi salva la cartella di lavoro come[file Excel di output](67338476.xlsx)La schermata seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nello screenshot, l'aggiornamento dell'affettatrice con gli elementi selezionati ha aggiornato di conseguenza anche la tabella pivot.

![cose da fare:immagine_alt_testo](updating-slicer_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
