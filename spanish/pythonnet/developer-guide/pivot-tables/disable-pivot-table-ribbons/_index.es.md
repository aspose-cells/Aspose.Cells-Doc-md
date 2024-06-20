---
title: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 90
url: /es/python-net/disable-pivot-table-ribbons/
description: Cómo deshabilitar las Cintas de la Tabla Dinámica con Aspose.Cells for Python via .NET
keywords: Aspose.Cells for Python Excel, biblioteca de Python de Excel, Deshabilitar las Cintas de la Tabla Dinámica Usando la Biblioteca Aspose.Cells para Python de Excel
---

{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles pero propensos a errores si los usuarios objetivos no tienen un conocimiento detallado de Excel para configurar estos informes. En estas circunstancias, las organizaciones desearán restringir a los usuarios para que no puedan cambiar un informe basado en tabla dinámica. Características comunes de la tabla dinámica como agregar filtros adicionales, segmentadores, campos o cambiar el orden de ciertas cosas en el informe generalmente no son recomendados para todos los usuarios. Por otro lado, estos usuarios también deben poder actualizar el informe y usar filtros o segmentadores existentes. Aspose.Cells for Python via .NET ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios de cambiar estos reportes mientras se crean estos reportes. Para este propósito, Excel proporciona una función para deshabilitar la cinta de la tabla dinámica y lo mismo es proporcionado por Aspose.Cells for Python via .NET es decir, el desarrollador puede deshabilitar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

## **Cómo Deshabilitar la Cinta de la Tabla Dinámica Usando la Biblioteca Aspose.Cells para Python de Excel**

El siguiente código demuestra esta característica accediendo a una tabla dinámica de una hoja y luego estableciendo [**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) en **falso**. El archivo de tabla dinámica de ejemplo se puede descargar desde este [enlace](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
