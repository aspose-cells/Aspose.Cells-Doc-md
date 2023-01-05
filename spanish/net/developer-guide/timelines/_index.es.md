---
title: Insertar línea de tiempo
linktitle: Cronologías
type: docs
weight: 170
url: /es/net/create-timeline/
description: Aprende a crear una línea de tiempo con Aspose.Cells.
---
## **Posibles escenarios de uso**

 En lugar de ajustar los filtros para mostrar las fechas, puede usar una línea de tiempo de tabla dinámica, una opción de filtro dinámico que le permite filtrar fácilmente por fecha/hora y acercar el período que desee con un control deslizante. Microsoft Excel le permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en el*Insertar > Línea de tiempo*. Aspose.Cells también le permite crear una línea de tiempo usando el[**Hoja de trabajo.Líneas de tiempo.Agregar()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index)método.

## **Crear línea de tiempo en una tabla dinámica**

 Consulte el siguiente código de ejemplo. carga el[ejemplo de archivo de Excel](input.xlsx) que contiene la tabla dinámica. A continuación, crea la línea de tiempo basada en el campo pivote de la primera base. Finalmente, guarda el libro de trabajo en[salida XLSX](output.xlsx) formato. La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](create-timeline-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

