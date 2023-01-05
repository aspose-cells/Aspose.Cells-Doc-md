---
title: Agrupar campos dinámicos en la tabla dinámica
type: docs
weight: 90
url: /es/java/group-pivot-fields-in-the-pivot-table/
---
## **Posibles escenarios de uso**

Microsoft Excel le permite agrupar campos dinámicos de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo dinámico, suele ser útil agruparlos en secciones. Aspose.Cells también ofrece esta función utilizando el[**Tabla dinámica.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) método.

## **Agrupar campos dinámicos en la tabla dinámica**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716838.xlsx)realiza la agrupación en el primer campo pivote usando el[**Tabla dinámica.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) método. Luego actualiza y calcula los datos de la tabla dinámica y guarda el libro de trabajo como el[archivo de salida de Excel](64716837.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, el primer campo dinámico ahora está agrupado por meses y trimestres.

![todo:imagen_alternativa_texto](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
