---
title: Especificar la posición absoluta del ítem de tabla dinámica
type: docs
weight: 40
url: /es/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

A veces, el usuario necesita especificar la posición absoluta de los ítems de tabla dinámica, la API de Aspose.Cells ha expuesto algunas nuevas propiedades y un método para cumplir con este requisito del usuario.

- Se agregó la propiedad [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) que se puede usar para especificar el índice de posición en todos los PivotItems independientemente del nodo padre. Se agregó la propiedad [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) que se puede utilizar para especificar el índice de posición en los PivotItems bajo el mismo nodo padre.
- Se agregó el método [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) para mover el ítem hacia arriba o hacia abajo en función del valor del contador, donde el contador es el número de posiciones para mover el PivotItem hacia arriba o hacia abajo. Si el valor del contador es menor que cero, el ítem se moverá hacia arriba, mientras que si el valor del contador es mayor que cero, el PivotItem se moverá hacia abajo, el parámetro de tipo Boolean isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo padre o no.
- Se ha vuelto obsoleto el método *PivotItem.move(int count)*, por lo tanto, se sugiere usar el nuevo método [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) en su lugar.

Tenga en cuenta que es necesario llamar a los métodos [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) y [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) antes de usar las propiedades [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) y [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-).

{{% /alert %}}

## Código de Muestra

El siguiente código de muestra crea una tabla dinámica y luego especifica las posiciones de los ítems de tabla dinámica en el mismo nodo padre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
{{< app/cells/assistant language="java" >}}
