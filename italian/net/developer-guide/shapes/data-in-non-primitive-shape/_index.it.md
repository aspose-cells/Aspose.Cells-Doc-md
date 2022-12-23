---
title: Dati in forma non primitiva
type: docs
weight: 300
url: /it/net/data-in-non-primitive-shape/
---
## **Accesso ai dati di forma non primitiva**

A volte è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelli che non lo sono sono chiamati non primitivi. Ad esempio, puoi definire le tue forme utilizzando diverse linee curve collegate.

## **Una forma non primitiva**

In Aspose.Cells, alle forme non primitive viene assegnato il tipo[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . Puoi controllare il loro tipo usando il file[**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)proprietà.

 Accedere ai dati della forma utilizzando il file[**Shape.Percorsi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)proprietà. Restituisce tutti i percorsi collegati che costituiscono la forma non primitiva. Questi percorsi sono del tipo[**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ciascun segmento.

|**Mostra un esempio di forma non primitiva**|
|:- |
|![cose da fare:immagine_alt_testo](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
