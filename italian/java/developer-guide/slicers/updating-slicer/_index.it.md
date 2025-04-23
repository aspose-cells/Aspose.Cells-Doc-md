---
title: Aggiornamento Slicer
type: docs
weight: 50
url: /it/java/updating-slicer/
---

## **Possibili Scenari di Utilizzo**
Se si desidera aggiornare uno slicer in Microsoft Excel, selezionare o deselezionare le sue voci, e si aggiornerà di conseguenza la tabella dello slicer o la tabella pivot. Utilizzare [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) per selezionare o deselezionare le voci dello slicer con Aspose.Cells e poi chiamare il metodo [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) per aggiornare la tabella dello slicer o la tabella pivot. 
## **Aggiornamento dello slicer**
Il seguente codice di esempio carica il [file di Excel di esempio](67338506.xlsx) che contiene uno slicer esistente. Deseleziona il 2° e il 3° elemento dello slicer e aggiorna lo slicer. Quindi salva il workbook come [file di Excel di output](67338505.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file di Excel di esempio. Come puoi vedere nella schermata, l'aggiornamento dello slicer con elementi selezionati ha anche aggiornato correttamente la tabella pivot di conseguenza.

![todo:image_alt_text](updating-slicer_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
