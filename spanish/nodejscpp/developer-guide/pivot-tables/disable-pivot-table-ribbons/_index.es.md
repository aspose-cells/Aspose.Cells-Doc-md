---
title: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 90
url: /es/nodejs-cpp/disable-pivot-table-ribbons/
description: Cómo desactivar las cintas de la tabla dinámica con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells para Node.js Excel, biblioteca de Excel para Node.js, desactivar cintas de la tabla dinámica usando la biblioteca de Excel Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles, pero propensos a errores si los usuarios destinatarios no tienen conocimientos detallados de Excel para configurar estos informes. En estas circunstancias, las organizaciones querrán restringir a los usuarios para que no puedan modificar estos informes de tablas dinámicas. Funciones comunes de las tablas dinámicas, como agregar filtros adicionales, segmentaciones, campos o cambiar el orden de ciertas cosas en el informe, en su mayoría no son recomendables para todos los usuarios. Por otro lado, estos usuarios también podrán actualizar el informe y usar filtros o segmentaciones existentes. Aspose.Cells for Node.js via C++ ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios de cambiar estos informes al crearlos. Para este propósito, Excel proporciona una función para desactivar la cinta de opciones de la tabla dinámica y la misma es proporcionada por Aspose.Cells for Node.js via C++, es decir, el desarrollador puede desactivar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

## **Cómo desactivar la cinta de la tabla dinámica usando Aspose.Cells for Node.js via C++**

El siguiente código demuestra esta característica accediendo a una tabla dinámica de una hoja y luego estableciendo [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) en **falso**. El archivo de tabla dinámica de ejemplo se puede descargar desde este [enlace](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
