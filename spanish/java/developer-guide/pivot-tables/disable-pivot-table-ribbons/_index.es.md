---
title: Deshabilitar cintas de tabla dinámica
type: docs
weight: 40
url: /es/java/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles pero propensos a errores si los usuarios objetivo no tienen un conocimiento detallado de Excel para configurar estos informes. En estas circunstancias, las organizaciones querrán restringir que los usuarios puedan cambiar un informe basado en tablas dinámicas. Las funciones comunes de la tabla dinámica, como agregar filtros adicionales, segmentaciones, campos o cambiar el orden de ciertas cosas en el informe, en su mayoría no se recomiendan para todos los usuarios. Por otro lado, estos usuarios también podrán actualizar el informe y utilizar filtros o segmentaciones existentes. Aspose.Cells ha brindado esta capacidad a los desarrolladores para restringir que los usuarios cambien estos informes mientras los crean. Para este propósito, Excel proporciona una función para deshabilitar la cinta de la tabla dinámica y Aspose.Cells proporciona lo mismo, es decir, el desarrollador puede deshabilitar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

## **Deshabilite la cinta de opciones de la tabla dinámica mediante PivotTable.setEnableWizard**

El siguiente código demuestra esta característica accediendo a una tabla dinámica desde una hoja y luego llamando al[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) para establecer esta bandera**falso** . El archivo de tabla dinámica de muestra se puede descargar desde este[Enlace](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
