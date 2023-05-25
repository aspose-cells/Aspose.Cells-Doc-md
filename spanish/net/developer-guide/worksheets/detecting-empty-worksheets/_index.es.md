---
title: Detectar hojas de trabajo vacías
type: docs
weight: 410
url: /es/net/detecting-empty-worksheets/
description: Este artículo muestra un código que explica cómo detectar hojas de cálculo vacías de libros de Excel mediante programación utilizando C# API con la biblioteca .NET.
keywords: detect empty worksheet c#, find empty excel worksheet c#
---
##  **Consultar por Poblado Cells**

Las hojas de trabajo pueden tener una o más celdas con valores donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En tal caso, es fácil detectar si una hoja de cálculo determinada está vacía o no. Todo lo que tenemos que comprobar es el[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) o[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)propiedades. Si las propiedades antes mencionadas devuelven cero o valores positivos, significa que se han llenado una o más celdas; sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas se ha llenado en la hoja de trabajo dada.

{{% alert color="primary" %}}

Las colecciones de filas y columnas tienen un índice basado en cero, por lo tanto, una celda en la fila 0 y la columna 0 significa la primera celda de la hoja de trabajo, que es A1.

{{% /alert %}}

##  **Compruebe si hay vacío Inicializado Cells**

 Todas las celdas que tienen valores se inicializan automáticamente, sin embargo, existe la posibilidad de que una hoja de trabajo tenga celdas con solo formato aplicado. En tal escenario, el[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)o[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)properties devolverá -1, lo que indica la ausencia de valores completos, pero las celdas inicializadas debido al formato de celda no se pueden detectar con este enfoque. Para verificar si una hoja de trabajo tiene celdas inicializadas vacías, se recomienda utilizar el método IEnumerator.MoveNext en el enumerador adquirido de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Si el método IEnumerator.MoveNext devuelve**verdadero** eso significa que hay una o más celdas inicializadas en la hoja de trabajo dada.

##  **Buscar formas**

 Es posible que una hoja de trabajo determinada no tenga celdas completas; sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos verificar si una hoja de trabajo contiene alguna forma, podemos hacerlo inspeccionando el[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)propiedad. Cualquier valor positivo indica la presencia de formas en la hoja de trabajo.

##  **Ejemplo de programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
