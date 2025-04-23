---
title: Agrupar campos de pivote en la tabla dinámica
type: docs
weight: 80
url: /es/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: Cómo agrupar los campos de la tabla dinámica en la tabla dinámica con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, biblioteca de Excel para Node.js, cómo agrupar campos de la tabla dinámica en la tabla dinámica usando la biblioteca de Excel Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Microsoft Excel permite agrupar los campos de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo de la tabla dinámica, suele ser útil agruparlos en secciones. Aspose.Cells for Node.js via C++ también proporciona esta función usando el método [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **Cómo agrupar campos de tabla dinámica en la tabla dinámica**

El siguiente código de muestra carga el [archivo Excel de muestra](64716818.xlsx) y realiza agrupaciones en el primer campo de tabla dinámica utilizando el método [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). Luego actualiza y calcula los datos de la tabla dinámica y guarda la hoja de cálculo como [archivo Excel de salida](64716817.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, el primer campo de tabla dinámica está ahora agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
