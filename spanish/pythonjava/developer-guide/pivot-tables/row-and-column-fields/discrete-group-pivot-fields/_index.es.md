---
title: Agrupación discreta de elementos de campos de tabla dinámica
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tabla dinámica en grupos personalizados con nombre, como frutas y verduras, mediante DiscreteGroupItem y PivotFieldGroupOptions.getDiscreteGroupItems en Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de campos de tabla dinámica, grupos personalizados, PivotField.group, Python via Java, tabla dinámica de Excel
type: docs
weight: 90
url: /es/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- La agrupación automática recopila elementos por tipo de datos, como las fechas en meses y trimestres o los números en rangos. La agrupación discreta resuelve el problema contrario: agrupa elementos concretos no relacionados en grupos personalizados con nombre, como los productos en frutas y verduras, las tiendas por regiones o las cuentas por zonas. Aspose.Cells ofrece agrupación discreta mediante la clase `DiscreteGroupItem` y el método `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` consta de un nombre de grupo y de los elementos que pertenecen a él. Los elementos se pueden identificar de dos maneras: por sus nombres (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) o por sus posiciones indexadas desde cero en los datos de origen (`DiscreteGroupItem("fruit", [0, 3])`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo del área de filas o de columnas de la tabla dinámica al pasar las opciones a `PivotField.group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tabla dinámica por nombres de elementos**
El siguiente ejemplo construye una pequeña lista de ventas (producto, fecha e importe), crea una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos; a continuación, define dos grupos personalizados por nombres de elementos: `fruit` (`grape`, `cherry`) y `vegetables` (`carrot`, `potato`). El resultado muestra una estructura de filas de dos niveles, con el nombre del grupo como nivel exterior y los elementos originales anidados debajo, lo que permite analizar las tendencias por grupo personalizado y por elemento.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

Tras `calculateData()`, el área de filas de la tabla dinámica muestra `fruit` (`grape` 50, `cherry` 80) y `vegetable` (`carrot` 60, `potato` 70), con un total general de 260; las etiquetas de columna conservan las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tabla dinámica por índices de elementos**
Cuando los nombres de los elementos son largos o están localizados, el segundo constructor de `DiscreteGroupItem` identifica los elementos por índice. Los índices son las posiciones de los elementos en los datos de origen, indexadas desde cero y en el orden en que aparecen, no en orden alfabético. En los datos de ejemplo anteriores, `grape` es el elemento 0, `carrot` es el elemento 1, `potato` es el elemento 2 y `cherry` es el elemento 3; por lo tanto, `fruit` es `{ 0, 3 }` y `vegetable` es `{ 1, 2 }`. El resultado es idéntico al del ejemplo basado en nombres.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no están asignados a ningún grupo personalizado no se pierden. Permanecen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno en su propia entrada independiente de un solo elemento. En el ejemplo anterior, al definir solo el grupo `fruit`, `carrot` y `potato` permanecen en el área de filas como entradas independientes junto al grupo `fruit`.
- Los métodos `PivotFieldGroupOptions.getNewPivotField()` y `setNewPivotField()` controlan la estructura de la agrupación discreta. `getNewPivotField()` tiene el valor predeterminado `true`, lo que añade el campo agrupado como un nuevo campo exterior junto al original y produce la estructura de dos niveles mostrada antes (`getRowFields()` aumenta a 2). Utilice `setNewPivotField(false)` para sustituir el campo original; en este caso, el área de filas muestra un único nivel que contiene únicamente los nombres de los grupos y sus valores agregados: `fruit` 130 (50 + 80) y `vegetable` 130 (60 + 70).
- Los constructores de `DiscreteGroupItem` basados en nombres y en índices pueden combinarse dentro de la misma colección `getDiscreteGroupItems()`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de la tabla dinámica](/cells/es/python-java/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de fila y columna en la tabla dinámica](/cells/es/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-java/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a la tabla dinámica](/cells/es/python-java/apply-style-to-pivot-table/)
- [Actualizar la tabla dinámica](/cells/es/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}