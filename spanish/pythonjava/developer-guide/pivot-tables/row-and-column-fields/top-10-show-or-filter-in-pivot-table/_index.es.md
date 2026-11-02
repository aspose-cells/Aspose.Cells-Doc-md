---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con la clasificación más alta o más baja de un campo de tabla dinámica en Aspose.Cells for Python via Java. Este artículo explica el método top10AutoShow de Excel 97-2003, cómo leer las opciones con Top10AutoShowSettings y el filtro de los 10 principales de Excel 2007-365 mediante filterTop10.
keywords: Aspose.Cells for Python via Java, tabla dinámica, 10 principales, mostrar automáticamente, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /es/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede ser difícil de leer cuando el campo tiene decenas de miembros. Un informe de los 10 principales conserva únicamente los elementos mejor o peor clasificados, que es exactamente lo que necesitan los informes de clasificación, como «los 5 productos principales por ingresos» o «las 3 regiones inferiores por número de ventas». Aspose.Cells admite dos mecanismos para esta finalidad, que corresponden a dos generaciones de Microsoft Excel.
- **AutoShow de Excel 97-2003** — el método `PivotField.top10AutoShow()`. Esta es la opción clásica «Mostrar los N elementos principales o inferiores», almacenada directamente en el campo de tabla dinámica. Funciona en todas las versiones de Excel, antiguas y modernas, porque forma parte del formato original de tabla dinámica.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.filterTop10()`. Este es el filtro moderno de valores «10 principales», disponible en «Filtros de valores» en el menú del campo. Se almacena como un objeto `PivotFilter` adjunto al campo y ofrece una clasificación basada en la cantidad de elementos y en porcentajes.

## **Mostrar los 10 principales en Excel 97-2003 (top10AutoShow)**
El AutoShow clásico se configura con una única llamada a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — habilita o deshabilita la opción AutoShow del campo.
- `isTop` — `True` conserva los elementos con la clasificación más alta (Principales), mientras que `False` conserva los de clasificación más baja (Inferiores).
- `count` — indica cuántos elementos conservar; por ejemplo, 10 para un informe clásico de los 10 principales.
- `rankBy` — índice basado en cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos según el campo en sí.
La clasificación puede basarse en un campo de valores o en el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar según un campo de valores**
Clasifique los elementos de un campo de fila según un campo de valores común, como Suma de ventas. El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y después muestra los 2 deportes con mayores ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos en el índice 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Clasificar por el propio campo**
Un campo también puede clasificarse por sí mismo; para ello, pase -1 como `rankBy`. Esta variante no necesita ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con la clasificación más baja según el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `Top10AutoShowSettings.getRankBy()` devuelve -1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Mostrar los 3 elementos inferiores clasificados por el propio campo (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Leer las opciones actuales (Top10AutoShowSettings)**
El método `PivotField.getTop10AutoShowSettings()` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de AutoShow almacenadas actualmente en el campo. Utilícelo para inspeccionar cómo se presentan los elementos de un libro de trabajo existente o de una tabla dinámica que acaba de configurar, incluidos los libros de trabajo cargados desde un archivo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

Las cuatro propiedades se corresponden con los atributos clásicos de AutoShow escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores recuperados son los que se aplican en todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Los accesores directos de `PivotField`, `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` y `getAutoShowField()` están marcados como obsoletos. Utilice el objeto `Top10AutoShowSettings` en su lugar: `PivotField.isAutoShow()` se sustituye por `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` se sustituye por `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` se sustituye por `Top10AutoShowSettings.getAutoShowCount()` y `PivotField.getAutoShowField()` se sustituye por `Top10AutoShowSettings.getRankBy()`. El método `top10AutoShow()` es la forma admitida de cambiar la configuración.
- `top10AutoShow` funciona con campos de fila y de columna. Un campo que se encuentre únicamente en el área de página (filtro) no se puede clasificar de esta manera porque sus elementos no se distribuyen en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (filterTop10)**
Las versiones modernas de Excel ofrecen el filtro de los 10 principales como filtro de valores en el menú del campo (Filtros de valores, 10 principales...). Aspose.Cells lo modela mediante el método `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, que devuelve el `PivotFilter` creado:
- `valueFieldIndex` — índice basado en cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — determina el significado de `itemCount`. `PivotFilterType.COUNT` conserva un número fijo de elementos (la opción Elementos del cuadro de diálogo). `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, de modo que `itemCount` es el propio porcentaje: 30 conserva el 30 % superior. `PivotFilterType.SUM` clasifica según la cobertura acumulada de valores.
- `isTop` — `True` para Principales, `False` para Inferiores.
- `itemCount` — el valor N en «N principales»; su unidad depende de `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Filtro Top 10 — conservar los 2 elementos principales por "Suma de ventas" (índice del campo de datos 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # Para usar en su lugar un filtro basado en porcentaje, conservar el 30 por ciento superior de los elementos:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` y `filterTop10` son dos funciones distintas. AutoShow escribe en el campo de tabla dinámica el conjunto clásico de atributos, incluido `autoShow`, y se respeta en todas las versiones de Excel desde Excel 97. `filterTop10` escribe una entrada `PivotFilter` moderna, que requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utilice el filtro moderno vuelve a mostrar todos los elementos. Para los documentos que deben conservar su contenido al pasar por herramientas heredadas, prefiera `top10AutoShow`; para los libros de trabajo modernos, prefiera `filterTop10`, ya que se combina con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-java/filter-by-label-or-value-of-pivot-table/)
- [Agregar campos de fila y de columna a una tabla dinámica](/cells/es/python-java/pivot-table-add-row-and-column-fields/)
- [Agrupar campos de una tabla dinámica](/cells/es/python-java/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/python-java/refresh-pivot-table/)
- [Agregar un campo de página a una tabla dinámica](/cells/es/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}