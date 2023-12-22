---
title: Deshabilitar las cintas de la tabla dinámica
type: docs
weight: 90
url: /es/python-net/disable-pivot-table-ribbons/
description: Cómo deshabilitar las cintas de tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles pero propensos a errores si los usuarios de destino no tienen conocimientos detallados de Excel para configurar estos informes. En estas circunstancias, las organizaciones querrán impedir que los usuarios puedan cambiar un informe basado en una tabla dinámica. Las funciones comunes de las tablas dinámicas, como agregar filtros adicionales, segmentaciones de datos, campos o cambiar el orden de ciertas cosas en el informe, no se recomiendan para todos los usuarios. Por otro lado, estos usuarios también podrán actualizar el informe y utilizar filtros o segmentaciones existentes. Aspose.Cells for Python via .NET ha proporcionado esta capacidad a los desarrolladores para impedir que los usuarios cambien estos informes mientras los crean. Para este propósito, Excel proporciona una función para deshabilitar la cinta de la tabla dinámica y la misma la proporciona Aspose.Cells for Python via .NET, es decir, el desarrollador puede deshabilitar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

##  **Deshabilite la cinta de tabla dinámica usando PivotTable.EnableWizard**

 El siguiente código demuestra esta característica accediendo a una tabla dinámica desde una hoja y luego configurando[**habilitar_asistente**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) a *falso**. Se puede descargar un archivo de tabla dinámica de muestra desde este[enlace](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
