---
title: Formateo del Objeto de Lista
type: docs
weight: 30
url: /es/python-java/formatting-list-object/
---

## **Formateo del Objeto de Lista**
Una tabla es una serie de filas y columnas que contienen datos relacionados y se gestionan de forma independiente de los datos en otras filas y columnas. Por defecto, cada columna en la tabla tiene habilitado el filtrado en la fila del encabezado para que pueda filtrar o ordenar rápidamente los datos del objeto de lista. Puede agregar una fila de totales (una fila especial en una lista que proporciona una selección de funciones de agregado útiles para trabajar con datos numéricos) al objeto de lista que proporciona una lista desplegable de funciones de agregado para cada celda de la fila de totales.

Aspose.Cells admite el formateo de objetos de lista. Para esto, la API proporciona las clases [ListObject](https://reference.aspose.com/cells/python/asposecells.api/ListObject) y [TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType). La clase [TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType) contiene constantes que representan los estilos de tabla integrados. El siguiente fragmento de código crea un nuevo Objeto de Lista y establece su tipo de estilo de tabla en [TABLE_STYLE_MEDIUM_10](https://reference.aspose.com/cells/python/asposecells.api/tablestyletype#TABLE_STYLE_MEDIUM_10).



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-FormatListObject.py" >}}
