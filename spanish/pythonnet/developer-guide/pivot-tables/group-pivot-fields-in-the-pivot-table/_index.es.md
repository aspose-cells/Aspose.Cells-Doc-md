---
title: Agrupar campos dinámicos en la tabla dinámica
type: docs
weight: 80
url: /es/python-net/group-pivot-fields-in-the-pivot-table/
description: Cómo agrupar campos dinámicos en la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Group Pivot Fields in the Pivot Table.
---
##  **Posibles escenarios de uso**

Microsoft Excel le permite agrupar campos dinámicos de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo dinámico, suele resultar útil agruparlos en secciones. Aspose.Cells for Python via .NET también proporciona esta función utilizando el[**Tabla dinámica.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)método.

##  **Agrupar campos dinámicos en la tabla dinámica**

 El siguiente código de muestra carga el[archivo de Excel de muestra](64716818.xlsx) y realiza la agrupación en el primer campo dinámico utilizando el[**Tabla dinámica.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float) método. Luego actualiza y calcula los datos de la tabla dinámica y guarda el libro como[archivo de salida de Excel](64716817.xlsx)La captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, el primer campo dinámico ahora está agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
