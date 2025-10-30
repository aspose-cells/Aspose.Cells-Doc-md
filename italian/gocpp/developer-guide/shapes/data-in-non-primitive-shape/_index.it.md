---
title: Dati in forma non primitiva con Golang tramite C++
linktitle: Dati in Forma Non Primitiva
type: docs
weight: 300
url: /it/go-cpp/data-in-non-primitive-shape/
description: Accedi e manipola i dati nelle forme non primitive usando Aspose.Cells con Golang tramite C++.
---

## **Accesso ai Dati di Forma Non-Primitiva**

A volte, è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelle che non lo sono vengono chiamate non primitive. Ad esempio, è possibile definire le proprie forme utilizzando diverse linee collegate da curve.

## **Una Forma Non-Primitiva**

In Aspose.Cells, alle forme non primitive viene assegnato il tipo [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). È possibile controllare il loro tipo utilizzando la proprietà [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/).

Accedere ai dati della forma utilizzando la proprietà [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/). Restituisce tutti i percorsi collegati che compongono la forma non primitiva. Questi percorsi sono del tipo [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ciascun segmento.

|**Mostra un esempio di una forma non primitiva**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
