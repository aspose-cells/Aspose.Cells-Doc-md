---
title: Agrupar campos de pivote en la tabla dinámica
type: docs
weight: 90
url: /es/java/group-pivot-fields-in-the-pivot-table/
---

## **Escenarios de uso posibles**

Microsoft Excel te permite agrupar campos de pivote de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo de pivote, a menudo es útil agruparlos en secciones. Aspose.Cells también proporciona esta función mediante el método [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-).

## **Agrupar campos de la tabla dinámica**

El siguiente código de muestra carga el [archivo de Excel de ejemplo](64716838.xlsx) y realiza la agrupación en el primer campo de pivote utilizando el método [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-). Luego actualiza y calcula los datos de la tabla dinámica y guarda el libro de trabajo como el [archivo de Excel de salida](64716837.xlsx). La captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de muestra. Como se puede ver en la captura de pantalla, el primer campo de pivote ahora está agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
