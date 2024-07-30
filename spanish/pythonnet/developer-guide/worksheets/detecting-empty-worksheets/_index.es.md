---
title: Detectar hojas de cálculo vacías
type: docs
weight: 410
url: /es/python-net/detecting-empty-worksheets/
description: Este artículo muestra código que explica cómo detectar hojas de Excel vacías de forma programática utilizando la biblioteca de Aspose.Cells for Python via .NET.
keywords: Biblioteca de Python Excel, detectar hoja de cálculo vacía utilizando python, encontrar hoja de cálculo de Excel vacía en python.
---

## **Buscar celdas pobladas**

Las hojas de cálculo pueden tener una o más celdas rellenadas con valores, donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En tal caso, es fácil detectar si una hoja de cálculo dada está vacía o no. Todo lo que tenemos que comprobar son las propiedades [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) o [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/). Si las propiedades mencionadas devuelven cero o valores positivos, eso significa que una o más celdas han sido rellenadas, sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas ha sido rellenada en la hoja de cálculo dada.

{{% alert color="primary" %}}

Las colecciones de filas y columnas tienen un índice basado en cero, por lo tanto, una celda en la fila 0 y columna 0 significa la primera celda en la hoja de cálculo, que es A1.

{{% /alert %}}

## **Comprobar celdas inicializadas vacías**

Todas las celdas que tienen valores se inicializan automáticamente, sin embargo, existe la posibilidad de que una hoja tenga celdas con solo formato aplicado. En dicho escenario, las propiedades [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) o [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) devolverán -1, lo que indica la ausencia de valores poblados pero las celdas inicializadas debido a que el formato de celda no se puede detectar utilizando este enfoque. Para verificar si una hoja de cálculo tiene celdas inicializadas vacías, se recomienda utilizar el método IEnumerator.MoveNext en el enumerador adquirido de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Si el método IEnumerator.MoveNext devuelve **true** eso significa que hay una o más celdas inicializadas en la hoja de cálculo dada.

## **Comprobar formas**

Es posible que una hoja de cálculo dada no tenga celdas pobladas, sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos verificar si una hoja de cálculo contiene alguna forma, podemos hacerlo inspeccionando los elementos [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection). Cualquier valor positivo indica la presencia de forma(s) en la hoja de cálculo.

## **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
