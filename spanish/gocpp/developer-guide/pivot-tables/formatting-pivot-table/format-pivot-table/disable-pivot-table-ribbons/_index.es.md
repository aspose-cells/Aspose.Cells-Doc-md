---
title: Desactivar las cintas de la tabla dinámica con Golang vía C++
linktitle: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 90
url: /es/go-cpp/disable-pivot-table-ribbons/
description: Aprende cómo desactivar las cintas de la tabla dinámica en archivos de Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles, pero propensos a errores si los usuarios destinatarios no tienen conocimientos detallados de Excel para configurarlos. En estas circunstancias, las organizaciones querrán restringir a los usuarios la capacidad de modificar estos informes. Funciones comunes de la tabla dinámica, como agregar filtros adicionales, segmentos, campos o cambiar el orden de ciertos elementos en el informe, generalmente no se recomiendan para todos los usuarios. Por otro lado, estos usuarios también deberían poder actualizar el informe y usar filtros o segmentos existentes. Aspose.Cells ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios la modificación de estos informes durante su creación. Para ello, Excel ofrece una función para desactivar la cinta de la tabla dinámica, y la misma opción la ofrece Aspose.Cells. Los desarrolladores pueden desactivar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

## **Deshabilitar la cinta de opciones de la tabla dinámica utilizando PivotTable.EnableWizard**

El siguiente código demuestra esta función accediendo a una tabla dinámica de una hoja y luego estableciendo [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) en **falso**. Un archivo de ejemplo de tabla dinámica se puede descargar desde este [enlace](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisablePivotTableRibbons.go" >}}
