---
title: Mostrar o filtrar los 10 elementos principales o inferiores en una tabla dinámica
linktitle: Mostrar o filtrar los 10 elementos principales o inferiores en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con mayor o menor clasificación de un campo pivote en Aspose.Cells for Python via .NET. Este artículo explica el método top_10_auto_show de Excel 97-2003, cómo leer las opciones con top_10_auto_show_settings y cómo utilizar el filtro de los 10 principales de Excel 2007-365 mediante filter_top10.
keywords: Aspose.Cells, Python mediante .NET, tabla dinámica, 10 principales, visualización automática, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /es/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede ser difícil de leer cuando el campo tiene decenas de miembros. Un informe de los 10 principales conserva únicamente los elementos con mayor o menor clasificación, precisamente lo que necesitan los informes de clasificación: «5 productos principales por ingresos» o «3 regiones con el menor número de ventas». Aspose.Cells admite dos mecanismos para ello, que corresponden a dos generaciones de Microsoft Excel.
- **Visualización automática de Excel 97-2003**: el método `PivotField.top_10_auto_show()`. Esta es la configuración clásica «Mostrar los N elementos principales o inferiores», almacenada directamente en el campo pivote. Funciona en todas las versiones de Excel, tanto antiguas como nuevas, porque forma parte del formato original de tabla dinámica.
- **Filtro de los 10 principales de Excel 2007-365**: el método `PivotField.filter_top10()`. Es el filtro moderno de los 10 principales disponible en el menú del campo, en Filtros de valores. Se almacena como un objeto `PivotFilter` asociado al campo y ofrece opciones de clasificación por número de elementos o por porcentaje.

## **Mostrar los 10 principales en Excel 97-2003 (top_10_auto_show)**
La visualización automática clásica se configura con una única llamada a `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`:
- `is_auto_show`: habilita o deshabilita la opción de visualización automática en el campo.
- `is_top`: `True` conserva los elementos con mayor clasificación («Superiores»), mientras que `False` conserva los de menor clasificación («Inferiores»).
- `count`: la cantidad de elementos que se conservarán; por ejemplo, 10 para un informe clásico de los 10 principales.
- `rank_by`: el índice de base cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos según el propio campo.
La clasificación puede determinarse a partir de un campo de valores o del propio campo. A continuación se muestran dos variantes.

### **Clasificar por un campo de valores**
Clasifique los elementos del campo de fila según un campo de valores común, como Suma de ventas. El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y a continuación muestra los 2 deportes con mayor clasificación por ventas. `rank_by` es 0 porque «Suma de ventas» es el campo de datos situado en el índice 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Mostrar los 2 elementos principales clasificados por "Suma de ventas" (índice 0 del campo de datos)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Clasificar por el propio campo**
Un campo también puede clasificarse por sí mismo: pase -1 como `rank_by`. Esta variante no requiere ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con menor clasificación según el propio campo. Al guardar esta configuración, el atributo `rank_by` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `top_10_auto_show_settings.rank_by` devuelve -1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Leer las opciones actuales (top_10_auto_show_settings)**
La propiedad `PivotField.top_10_auto_show_settings` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de visualización automática almacenadas actualmente en el campo. Utilícela para inspeccionar cómo se mostrarán los elementos en un libro de trabajo existente o en una tabla dinámica recién configurada. Esto incluye los libros de trabajo cargados desde un archivo.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

Las cuatro propiedades se corresponden con los atributos clásicos de visualización automática escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores recuperados son los que respetan todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Las propiedades directas `is_auto_show`, `is_ascend_show`, `auto_show_count` y `auto_show_field` de `PivotField` están marcadas como obsoletas. Utilice el objeto `top_10_auto_show_settings` en su lugar: `is_auto_show` se sustituye por `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` se sustituye por `top_10_auto_show_settings.is_top`, `auto_show_count` se sustituye por `top_10_auto_show_settings.auto_show_count` y `auto_show_field` se sustituye por `top_10_auto_show_settings.rank_by`. El método `top_10_auto_show()` es la forma admitida de cambiar la configuración.
- `top_10_auto_show` funciona con campos de fila y columna. Un campo que solo esté en el área de página (filtro) no puede clasificarse de esta forma porque sus elementos no se muestran en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: Filtro de los 10 principales (filter_top10)**
Las versiones modernas de Excel ofrecen el filtro de los 10 principales en el menú del campo (Filtros de valores, 10 principales...). Aspose.Cells lo modela mediante el método `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)`, que devuelve el `PivotFilter` creado:
- `value_field_index`: el índice de base cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type`: el significado de `item_count`. `PivotFilterType.COUNT` conserva un número fijo de elementos (la opción Elementos del diálogo). `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, de modo que `item_count` es el propio porcentaje; 30 conserva el 30 % de los elementos con mayor clasificación. `PivotFilterType.SUM` determina la clasificación según la cobertura acumulada de los valores.
- `is_top`: `True` para «Superiores», `False` para «Inferiores».
- `item_count`: el valor N de «N principales»; su unidad depende de `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Filtro Top 10: conservar los 2 elementos principales según "Suma de ventas" (índice del campo de datos 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# Para un filtro basado en porcentaje, conservar el 30 % superior de los elementos:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` y `filter_top10` son dos funcionalidades distintas. La visualización automática escribe el atributo clásico `autoShow` en el campo pivote, y todas las versiones de Excel desde Excel 97 respetan esta configuración. `filter_top10` escribe una entrada `PivotFilter` moderna, que requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utilice el filtro moderno recurre a la visualización de todos los elementos. Para los documentos que deban abrirse y volver a guardarse con herramientas heredadas, se recomienda `top_10_auto_show`; para los libros de trabajo modernos, se recomienda `filter_top10` porque se combina con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-net/filter-by-label-or-value-of-pivot-table/)
- [Agregar campos de fila y columna a una tabla dinámica](/cells/es/python-net/pivot-table-add-row-and-column-fields/)
- [Agrupar campos pivote en una tabla dinámica](/cells/es/python-net/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/python-net/refresh-pivot-table/)
- [Agregar un campo de página a una tabla dinámica](/cells/es/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}