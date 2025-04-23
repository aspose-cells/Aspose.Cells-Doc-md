---
title: Dati in Forma Non Primitiva
type: docs
weight: 500
url: /it/java/data-in-non-primitive-shape/
---

## **Accesso ai Dati di Forma Non-Primitiva**

A volte, è necessario accedere ai dati da una forma non incorporata. Le forme incorporate sono chiamate forme primitive; quelle che non lo sono vengono chiamate non primitive. Ad esempio, è possibile definire le proprie forme utilizzando diverse linee collegate da curve.

## **Una Forma Non-Primitiva**

In Aspose.Cells, le forme non primitive vengono assegnate il tipo [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT-PRIMITIVE). È possibile controllare il tipo utilizzando il metodo [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType).

Accedi ai dati della forma utilizzando il metodo [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths). Restituisce tutti i percorsi connessi che compongono la forma non primitiva. Questi percorsi sono del tipo ShapePath che contiene un elenco di tutti i segmenti che a loro volta contengono i punti in ogni segmento.

Il seguente frammento di codice dimostra l'uso del metodo [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) per accedere alle informazioni sul percorso della forma non primitiva.

**Mostra un esempio di una forma non primitiva** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
{{< app/cells/assistant language="java" >}}
