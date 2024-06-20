---
title: Rimozione del filtro
type: docs
weight: 40
url: /it/python-java/removing-slicer/
---

## **Rimozione dello slicer**
Per rimuovere il filtro in Microsoft Excel, è sufficiente selezionare il filtro e premere il pulsante *Elimina*. Per ottenere lo stesso risultato utilizzando Aspose.Cells for Python via Java, utilizzare il metodo Worksheet.getSlicers().remove(). Rimuoverà il filtro dal foglio di lavoro. 

Il seguente frammento di codice carica il [file Excel di esempio](106364970.xlsx) che contiene un filtro esistente. Accede al filtro, lo rimuove e salva il [file Excel di output](106364971.xlsx). La schermata seguente mostra il filtro che verrà rimosso.

![todo:image_alt_text](Removing-Slicer-using-Aspose.Cells.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
