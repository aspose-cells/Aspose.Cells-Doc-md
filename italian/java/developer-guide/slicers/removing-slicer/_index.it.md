---
title: Rimozione del filtro
type: docs
weight: 30
url: /it/java/removing-slicer/
---

## **Possibili Scenari di Utilizzo**
Se si desidera rimuovere lo slicer in Microsoft Excel, basta selezionarlo e premere il pulsante *Elimina*. Per rimuoverlo programmaticamente usando l’API di Aspose.Cells, utilizzare il metodo [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove-com.aspose.cells.Slicer-) . Rimuoverà lo slicer dal foglio di lavoro. 
## **Rimozione dello slicer**
Il seguente codice di esempio carica il [file di Excel di esempio](67338504.xlsx) che contiene uno slicer esistente. Accede agli slicer e quindi li rimuove. Infine, salva il workbook come [file di Excel di output](67338502.xlsx). La schermata seguente mostra lo slicer che verrà rimosso dopo l'esecuzione del codice di esempio.

![todo:image_alt_text](removing-slicer_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
