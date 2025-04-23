---
title: Detectar hojas de cálculo vacías
type: docs
weight: 710
url: /es/java/detecting-empty-worksheets/
---

## **Buscar celdas pobladas**
Las hojas de cálculo pueden tener una o más celdas pobladas con valores donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En este caso, es fácil detectar si una hoja de cálculo dada está vacía o no. Todo lo que tenemos que comprobar es las propiedades [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) o [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn). Si las propiedades mencionadas devuelven valores cero o positivos, eso significa que una o más celdas han sido pobladas. Sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas ha sido poblada en la hoja de cálculo dada.

{{% alert color="primary" %}} 

Las colecciones de filas y columnas tienen un índice basado en cero, por lo tanto, una celda en la fila 0 y la columna 0 significa la primera celda en la hoja de cálculo, que es A1.

{{% /alert %}} 
## **Comprobar celdas inicializadas vacías**
Todas las celdas que tienen valores se inicializan automáticamente, sin embargo, existe la posibilidad de que una hoja de cálculo tenga celdas con solo formato aplicado. En dicho escenario, las propiedades [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) o [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) devolverán -1, lo que indica la ausencia de valores poblados pero las celdas inicializadas debido al formato de las celdas no se pueden detectar mediante este enfoque. Para comprobar si una hoja de cálculo tiene celdas inicializadas vacías, se recomienda usar el método *Iterator.hasNext* en el iterador adquirido de la colección Cells. Si el método *iterator.hasNext* devuelve true, entonces eso significa que hay una o más celdas inicializadas en la hoja de cálculo dada.

{{% alert color="primary" %}} 

Existen varias maneras de adquirir el enumerador de celdas como se detalla en [Cómo y dónde usar los iteradores](/cells/es/java/como-y-donde-usar-iteradores/).

{{% /alert %}} 
## **Comprobar formas**
Es posible que una hoja de cálculo dada no tenga celdas pobladas, sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos comprobar si una hoja de cálculo contiene alguna forma, podemos hacerlo inspeccionando la propiedad [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count). Cualquier valor positivo indica la presencia de una o más formas en la hoja de cálculo.
## **Ejemplo de Programación**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
