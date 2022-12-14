---
title: Dati in forma non primitiva
type: docs
weight: 500
url: /it/java/data-in-non-primitive-shape/
---
## **Accesso ai dati di forma non primitiva**

A volte è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelli che non lo sono sono chiamati non primitivi. Ad esempio, puoi definire le tue forme utilizzando diverse linee curve collegate.

## **Una forma non primitiva**

 In Aspose.Cells, alle forme non primitive viene assegnato il tipo[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . Puoi controllare il loro tipo usando il file[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)metodo.

 Accedere ai dati della forma utilizzando il file[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)metodo. Restituisce tutti i percorsi collegati che costituiscono la forma non primitiva. Questi percorsi sono del tipo ShapePath che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ciascun segmento.

Il seguente frammento di codice illustra l'uso di[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)metodo per accedere alle informazioni sul percorso di forma non primitiva.

**Mostra un esempio di forma non primitiva** 

![cose da fare:immagine_alt_testo](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
