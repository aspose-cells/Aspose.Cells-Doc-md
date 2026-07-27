---
title: Agrupar campos de pivote en la tabla dinámica
type: docs
weight: 80
url: /es/python-net/group-pivot-fields-in-the-pivot-table/
description: Cómo agrupar campos de tabla dinámica en la tabla dinámica con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca de Excel en Python, Cómo agrupar campos de tabla dinámica en la tabla dinámica usando la biblioteca de Excel Aspose.Cells para Python.
---

## **Escenarios de uso posibles**

Microsoft Excel te permite agrupar campos de tabla dinámica de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo de tabla dinámica, a menudo es útil agruparlos en secciones. Aspose.Cells para Python via .NET también proporciona esta función mediante el método [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float).

## **Cómo agrupar campos de tabla dinámica en la tabla dinámica**

El siguiente código de muestra carga el [archivo Excel de muestra](64716818.xlsx) y realiza agrupaciones en el primer campo de tabla dinámica utilizando el método [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float). Luego actualiza y calcula los datos de la tabla dinámica y guarda la hoja de cálculo como [archivo Excel de salida](64716817.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, el primer campo de tabla dinámica está ahora agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
{{< app/cells/assistant language="python-net" >}}
