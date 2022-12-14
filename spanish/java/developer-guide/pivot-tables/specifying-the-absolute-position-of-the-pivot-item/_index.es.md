---
title: Especificación de la posición absoluta del elemento pivote
type: docs
weight: 40
url: /es/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

A veces, el usuario necesita especificar la posición absoluta de los elementos pivote, Aspose.Cells API ha expuesto algunas propiedades nuevas y un método para lograr este requisito del usuario.

-  Adicional[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) propiedad que se puede usar para especificar el índice de posición en todos los PivotItems independientemente del nodo principal. Adicional[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) propiedad que se puede usar para especificar el índice de posición en PivotItems en el mismo nodo principal.
-  Adicional[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)para mover el elemento hacia arriba o hacia abajo en función del valor de conteo, donde el conteo es el número de posiciones para mover el PivotItem hacia arriba o hacia abajo. Si el valor de conteo es menor que cero, el elemento se moverá hacia arriba, mientras que si el valor de conteo es mayor que cero, PivotItem se moverá hacia abajo, el parámetro de tipo booleano isSameParent especifica si la operación de movimiento debe realizarse en el mismo nodo principal o no.
-  Obsoleto el*PivotItem.move (recuento int)* método, por lo tanto, se sugiere utilizar el método recién agregado[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) en cambio.

 Tenga en cuenta que es necesario llamar al[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) y[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) métodos antes de usar[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) propiedades y[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) método.

{{% /alert %}}

## Código de muestra

El siguiente código de ejemplo crea una tabla dinámica y luego especifica las posiciones de los elementos dinámicos en el mismo nodo principal.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
