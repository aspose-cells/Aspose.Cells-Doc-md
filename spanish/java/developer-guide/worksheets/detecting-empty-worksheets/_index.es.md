---
title: Detectar hojas de trabajo vacías
type: docs
weight: 710
url: /es/java/detecting-empty-worksheets/
---
## **Consultar por Poblado Cells**
Las hojas de trabajo pueden tener una o más celdas con valores donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En tal caso, es fácil detectar si una hoja de cálculo determinada está vacía o no. Todo lo que tenemos que comprobar es el[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) o[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)propiedades. Si las propiedades antes mencionadas devuelven cero o valores positivos, eso significa que se han llenado una o más celdas; sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas se ha llenado en la hoja de trabajo dada.

{{% alert color="primary" %}} 

Las colecciones de filas y columnas tienen un índice basado en cero, por lo tanto, una celda en la fila 0 y la columna 0 significa la primera celda de la hoja de trabajo, que es A1.

{{% /alert %}} 
## **Compruebe si hay vacío Inicializado Cells**
 Todas las celdas que tienen valores se inicializan automáticamente, sin embargo, existe la posibilidad de que una hoja de trabajo tenga celdas con solo formato aplicado. En tal escenario, el[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) o[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)properties devolverá -1, lo que indica la ausencia de valores completos, pero las celdas inicializadas debido al formato de celda no se pueden detectar con este enfoque. Para verificar si una hoja de cálculo tiene celdas inicializadas vacías, se recomienda utilizar el*Iterator.hasNext* método en el iterador adquirido de la colección Cells. Si el*iterator.hasNext*El método devuelve verdadero, entonces eso significa que hay una o más celdas inicializadas en la hoja de trabajo dada.

{{% alert color="primary" %}} 

 Hay varias formas de adquirir el enumerador de células como se detalla en[Cómo y dónde usar iteradores](/cells/es/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Buscar formas**
 Es posible que una hoja de trabajo determinada no tenga celdas completas; sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos verificar si una hoja de trabajo contiene alguna forma, podemos hacerlo inspeccionando el[ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count)propiedad. Cualquier valor positivo indica la presencia de formas en la hoja de trabajo.
## **Ejemplo de programación**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
