---
title: Detectar hojas de cálculo vacías
type: docs
weight: 410
url: /es/net/detecting-empty-worksheets/
description: Este artículo muestra código explicando cómo detectar hojas de cálculo vacías de los libros de trabajo de Excel de forma programática utilizando la API de C# con la biblioteca .NET.
keywords: detectar hoja de cálculo vacía c#, encontrar hoja de cálculo de excel vacía c#
---

## **Buscar celdas pobladas**

Las hojas de cálculo pueden tener una o más celdas rellenadas con valores, donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En tal caso, es fácil detectar si una hoja de cálculo dada está vacía o no. Todo lo que tenemos que comprobar son las propiedades [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn). Si las propiedades mencionadas devuelven cero o valores positivos, eso significa que una o más celdas han sido rellenadas, sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas ha sido rellenada en la hoja de cálculo dada.

{{% alert color="primary" %}}

Las colecciones de filas y columnas tienen un índice basado en cero, por lo tanto, una celda en la fila 0 y columna 0 significa la primera celda en la hoja de cálculo, que es A1.

{{% /alert %}}

## **Comprobar celdas inicializadas vacías**

Todas las celdas que tienen valores se inicializan automáticamente, sin embargo, existe la posibilidad de que una hoja de cálculo tenga celdas con solo formato aplicado. En un escenario así, las propiedades [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) devolverán -1, indicando la ausencia de cualquier valor rellenado pero celdas inicializadas debido a que el formato de las celdas no puede ser detectado usando este enfoque. Para comprobar si una hoja de cálculo tiene celdas vacías inicializadas, se recomienda usar el método IEnumerator.MoveNext en el enumerador adquirido de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Si el método IEnumerator.MoveNext devuelve **true**, eso significa que hay una o más celdas inicializadas en la hoja de cálculo dada.

## **Comprobar formas**

Es posible que una hoja de cálculo dada no tenga ninguna celda rellenada, sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos comprobar si una hoja de cálculo contiene alguna forma, podemos hacerlo inspeccionando la propiedad [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection). Cualquier valor positivo indica la presencia de forma(s) en la hoja de cálculo.

## **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
