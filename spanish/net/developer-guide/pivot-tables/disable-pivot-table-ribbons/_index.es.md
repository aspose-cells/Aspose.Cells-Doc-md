---
title: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 90
url: /es/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Los informes basados en tabla dinámica son útiles pero propensos a errores si los usuarios destinatarios no tienen un conocimiento detallado de Excel para configurar estos informes. En estas circunstancias, las organizaciones desearán restringir a los usuarios para que no puedan cambiar un informe basado en tabla dinámica. No se recomienda que la mayoría de los usuarios realicen cambios comunes en la tabla dinámica, como agregar filtros adicionales, segmentadores, campos o cambiar el orden de ciertas cosas en el informe. Por otro lado, estos usuarios también deberían poder actualizar el informe y usar filtros o segmentadores existentes. Aspose.Cells ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios de cambiar estos informes mientras los crean. Para este propósito, Excel proporciona una función para desactivar el panel de control de la tabla dinámica y lo mismo es proporcionado por Aspose.Cells, es decir, el desarrollador puede desactivar el panel que contiene controles para modificar estos informes.

{{% /alert %}}

## **Deshabilitar la cinta de opciones de la tabla dinámica utilizando PivotTable.EnableWizard**

El siguiente código demuestra esta característica accediendo a una tabla dinámica de una hoja y luego estableciendo [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) en **falso**. El archivo de tabla dinámica de ejemplo se puede descargar desde este [enlace](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
