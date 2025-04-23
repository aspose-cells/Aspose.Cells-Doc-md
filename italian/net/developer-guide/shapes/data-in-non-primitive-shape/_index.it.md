---
title: Dati in Forma Non Primitiva
type: docs
weight: 300
url: /it/net/data-in-non-primitive-shape/
---

## **Accesso ai Dati di Forma Non-Primitiva**

A volte, è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelle che non lo sono vengono chiamate non primitive. Ad esempio, è possibile definire le proprie forme utilizzando diverse linee collegate da curve.

## **Una Forma Non-Primitiva**

In Aspose.Cells, alle forme non primitive viene assegnato il tipo [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). È possibile controllare il loro tipo utilizzando la proprietà [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype).

Accedere ai dati della forma utilizzando la proprietà [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths). Restituisce tutti i percorsi collegati che compongono la forma non primitiva. Questi percorsi sono del tipo [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ciascun segmento.

|**Mostra un esempio di una forma non primitiva**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
