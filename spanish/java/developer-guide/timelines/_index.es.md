---
title: Insertar línea de tiempo
linktitle: Cronologías
type: docs
weight: 170
url: /es/java/create-timeline/
description: Aprenda a crear una línea de tiempo con Aspose.Cells para java.
---
## **Posibles escenarios de uso**

 En lugar de ajustar los filtros para mostrar las fechas, puede usar una línea de tiempo de tabla dinámica, una opción de filtro dinámico que le permite filtrar fácilmente por fecha/hora y acercar el período que desee con un control deslizante. Microsoft Excel le permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en el*Insertar > Línea de tiempo*. Aspose.Cells para java también le permite crear una línea de tiempo utilizando el método [**Worksheet.getTimelines.add()**].

## **Crear línea de tiempo en una tabla dinámica**

 Consulte el siguiente código de ejemplo. carga el[ejemplo de archivo de Excel](input.xlsx) que contiene la tabla dinámica. A continuación, crea la línea de tiempo basada en el campo pivote de la primera base. Finalmente, guarda el libro de trabajo en[salida XLSX](output.xlsx) formato. La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells en el archivo de salida de Excel.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

