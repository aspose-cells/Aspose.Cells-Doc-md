---
title: Agrupar campos de pivote en la tabla dinámica
type: docs
weight: 80
url: /es/net/group-pivot-fields-in-the-pivot-table/
---

## **Escenarios de uso posibles**

Microsoft Excel te permite agrupar campos de tabla dinámica de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo de tabla dinámica, a menudo es útil agruparlos en secciones. Aspose.Cells también proporciona esta función utilizando el método [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/).

## **Agrupar campos de la tabla dinámica**

El siguiente código de muestra carga el [archivo Excel de muestra](64716818.xlsx) y realiza agrupaciones en el primer campo de tabla dinámica utilizando el método [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/). Luego actualiza y calcula los datos de la tabla dinámica y guarda la hoja de cálculo como [archivo Excel de salida](64716817.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, el primer campo de tabla dinámica está ahora agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
