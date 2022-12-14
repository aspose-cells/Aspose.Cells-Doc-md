---
title: Aggiornamento affettatrice
type: docs
weight: 50
url: /it/java/updating-slicer/
---
## **Possibili scenari di utilizzo**
Se desideri aggiornare l'affettatrice in Microsoft Excel, seleziona o deseleziona i suoi elementi, quindi aggiornerà la tabella affettatrice o la tabella pivot di conseguenza. Si prega di utilizzare[Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems)per selezionare o deselezionare gli articoli affettatrice con Aspose.Cells e poi chiamare[Affettatrice.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) per aggiornare la tabella slicer o la tabella pivot.
## **Aggiornamento affettatrice**
Il codice di esempio seguente carica il file[esempio di file Excel](67338506.xlsx)che contiene un'affettatrice esistente. Deseleziona il 2° e il 3° elemento dell'affettatrice e aggiorna l'affettatrice. Quindi salva la cartella di lavoro come file[file Excel di output](67338505.xlsx). Lo screenshot seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nello screenshot, l'aggiornamento dell'affettatrice con gli elementi selezionati ha aggiornato anche la tabella pivot di conseguenza.

![cose da fare:immagine_alt_testo](updating-slicer_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
