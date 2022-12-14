---
title: Agrupar campos dinámicos en la tabla dinámica
type: docs
weight: 80
url: /es/net/group-pivot-fields-in-the-pivot-table/
---
## **Posibles escenarios de uso**

Microsoft Excel le permite agrupar campos dinámicos de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo dinámico, suele ser útil agruparlos en secciones. Aspose.Cells también ofrece esta función utilizando el[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)método.

## **Agrupar campos dinámicos en la tabla dinámica**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716818.xlsx) y realiza la agrupación en el primer campo pivote usando el[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)método. Luego actualiza y calcula los datos de la tabla dinámica y guarda el libro de trabajo como[archivo de salida de Excel](64716817.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, el primer campo dinámico ahora está agrupado por meses y trimestres.

![todo:imagen_alternativa_texto](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
