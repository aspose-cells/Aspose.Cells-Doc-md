---
title: Agrupación discreta de elementos de campos de tablas dinámicas
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tablas dinámicas en grupos personalizados con nombre, como frutas y verduras, mediante DiscreteGroupItem y pivot_field_group_options.discrete_group_items en Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de tablas dinámicas, grupos personalizados, PivotField.group, Python, tabla dinámica de Excel
type: docs
weight: 90
url: /es/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- La agrupación automática reúne los elementos según el tipo de datos, como las fechas por meses y trimestres o los números por rangos. La agrupación discreta resuelve el problema opuesto: reúne elementos específicos y no relacionados en grupos personalizados con nombre; por ejemplo, productos en frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells ofrece la agrupación discreta mediante la clase `DiscreteGroupItem` y la propiedad `pivot_field_group_options.discrete_group_items`.
- Un `DiscreteGroupItem` representa un nombre de grupo y los elementos que pertenecen a él. Los elementos se pueden identificar de dos maneras: por sus nombres (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) o por sus posiciones basadas en cero en los datos de origen (`DiscreteGroupItem("fruit", [0, 3])`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo del área de filas o de columnas de la tabla dinámica al pasar las opciones a `pivot_field.group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tablas dinámicas por nombres de elementos**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha e importe), genera una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos; a continuación, define dos grupos personalizados por nombres de elementos: frutas (uva, cereza) y verduras (zanahoria, patata). El resultado muestra una estructura de filas de dos niveles, con el nombre del grupo como nivel exterior y los elementos originales anidados debajo, lo que permite analizar las tendencias por grupo personalizado y por elemento.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

Después de `calculate_data()`, el área de filas de la tabla dinámica muestra frutas (uva 50, cereza 80) y verduras (zanahoria 60, patata 70), con un total general de 260, y las etiquetas de las columnas mantienen las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tablas dinámicas por índices de elementos**
Cuando los nombres de los elementos son largos o están localizados, el segundo constructor de `DiscreteGroupItem` los identifica por índice. Los índices son posiciones basadas en cero de los elementos en el orden en que aparecen en los datos de origen, no en orden alfabético. En los datos de muestra anteriores, la uva es el elemento 0, la zanahoria es el elemento 1, la patata es el elemento 2 y la cereza es el elemento 3; por lo tanto, las frutas son `{ 0, 3 }` y las verduras son `{ 1, 2 }`. El resultado es idéntico al del ejemplo basado en nombres.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no se asignan a ningún grupo personalizado no se pierden. Permanecen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno como una entrada independiente de un solo elemento. En el ejemplo anterior, al definir solo el grupo de frutas, la zanahoria y la patata permanecen en el área de filas como entradas independientes junto al grupo de frutas.
- La propiedad `pivot_field_group_options.new_pivot_field` controla la estructura de la agrupación discreta. De forma predeterminada, tiene el valor `True`, lo que agrega el campo agrupado como un nuevo campo exterior junto al original y produce la estructura de dos niveles mostrada anteriormente (`row_fields` aumenta a 2). Si se establece en `False`, el campo original se sustituye y el área de filas muestra un único nivel que contiene solo los nombres de los grupos y sus valores agregados: frutas 130 (50 + 80) y verduras 130 (60 + 70).
- Los constructores de `DiscreteGroupItem` basados en nombres y en índices se pueden combinar dentro de la misma lista `discrete_group_items`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de tablas dinámicas en la tabla dinámica](/cells/es/python-net/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de filas y columnas a una tabla dinámica](/cells/es/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-net/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a una tabla dinámica](/cells/es/python-net/apply-style-to-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}