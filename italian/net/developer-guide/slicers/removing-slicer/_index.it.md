---
title: Rimozione del filtro
type: docs
weight: 30
url: /it/net/removing-slicer/
---

## **Possibili Scenari di Utilizzo**

Se si desidera rimuovere uno slicer in Microsoft Excel, è sufficiente selezionarlo e premere il pulsante *Elimina*. Allo stesso modo, se si desidera rimuoverlo utilizzando l'API di Aspose.Cells in modo programmato, si prega di utilizzare il metodo [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/remove). Rimuoverà lo slicer dal foglio di lavoro.

## **Rimozione dello slicer**

Il seguente codice di esempio carica il [file Excel di esempio](67338478.xlsx) che contiene un filtro esistente. Accede ai filtri e li rimuove. Infine, salva il lavoro come [file Excel di output](67338477.xlsx). La seguente schermata mostra il filtro che verrà rimosso dopo l'esecuzione del codice di esempio.

![todo:image_alt_text](removing-slicer_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-RemovingSlicer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
