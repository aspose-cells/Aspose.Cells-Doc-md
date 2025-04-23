---
title: Dati in Forma Non Primitiva
type: docs
weight: 300
url: /it/python-net/data-in-non-primitive-shape/
description: Questo articolo mostra dati in forma non primitiva attraverso l API Aspose.Cells per Python via .NET.
keywords: Biblioteca Python per Excel, Python dati in forma non primitiva, Python come accedere ai dati di forma non primitiva.
---

## **Accesso ai Dati di Forma Non-Primitiva**

A volte, è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelle che non lo sono vengono chiamate non primitive. Ad esempio, è possibile definire le proprie forme utilizzando diverse linee collegate da curve.

## **Una Forma Non-Primitiva**

In Aspose.Cells per Python via .NET, le forme non primitive sono assegnate al tipo [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). Puoi controllarne il tipo usando la proprietà [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type).

Accedere ai dati della forma utilizzando la proprietà [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths). Restituisce tutti i percorsi collegati che compongono la forma non primitiva. Questi percorsi sono del tipo [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ciascun segmento.

|**Mostra un esempio di una forma non primitiva**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
