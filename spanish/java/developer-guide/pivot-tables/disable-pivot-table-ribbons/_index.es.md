---
title: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 40
url: /es/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Los informes basados en tabla dinámica son útiles pero propensos a errores si los usuarios destinatarios no tienen un conocimiento detallado de Excel para configurar estos informes. En estas circunstancias, las organizaciones desearán restringir a los usuarios para que no puedan cambiar un informe basado en tabla dinámica. No se recomienda que la mayoría de los usuarios realicen cambios comunes en la tabla dinámica, como agregar filtros adicionales, segmentadores, campos o cambiar el orden de ciertas cosas en el informe. Por otro lado, estos usuarios también deberían poder actualizar el informe y usar filtros o segmentadores existentes. Aspose.Cells ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios de cambiar estos informes mientras los crean. Para este propósito, Excel proporciona una función para desactivar el panel de control de la tabla dinámica y lo mismo es proporcionado por Aspose.Cells, es decir, el desarrollador puede desactivar el panel que contiene controles para modificar estos informes.

{{% /alert %}}

## **Desactivar el panel de control de la tabla dinámica mediante PivotTable.setEnableWizard**

El siguiente código demuestra esta función accediendo a una tabla dinámica desde una hoja y luego llamando a [**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) para establecer este indicador como **falso**. Se puede descargar un archivo de tabla dinámica de ejemplo desde este [enlace](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
