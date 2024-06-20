---
title: Insertar línea de tiempo
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/java/create-timeline/
description: Aprenda cómo crear una línea de tiempo con Aspose.Cells para Java.
---

## **Escenarios de uso posibles**

En lugar de ajustar filtros para mostrar fechas, puede usar una línea de tiempo de tabla dinámica: una opción de filtro dinámico que le permite filtrar fácilmente por fecha/hora y hacer zoom sobre el período que desee con un control deslizante. Microsoft Excel le permite crear una línea de tiempo seleccionando una tabla dinámica y haciendo clic en *Insertar > Línea de tiempo*. Aspose.Cells para Java también le permite crear líneas de tiempo usando el método [**Worksheet.getTimelines.add()**].

## **Crear una línea de tiempo para una Tabla Dinámica**

Por favor, consulta el siguiente código de muestra. Carga el [archivo Excel de muestra](input.xlsx) que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el primer campo pivote base. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](output.xlsx). La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells en el archivo Excel de salida.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

