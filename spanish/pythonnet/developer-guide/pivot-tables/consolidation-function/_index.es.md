---
title: Función de consolidación
type: docs
weight: 20
url: /es/python-net/consolidation-function/
description: Cómo aplicar ConsolidationFunction a los campos de datos de la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: ConsolidationFunction to Data Fields of Pivot Table.
---
##  **Función de consolidación**

 Aspose.Cells for Python via .NET se puede utilizar para aplicar ConsolidationFunction a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puede hacer clic derecho en el campo de valor y luego seleccionar**Configuración del campo de valor...** y luego seleccione la pestaña *Resumir valores por**. Desde allí, puede seleccionar cualquier función de consolidación de su elección, como suma, recuento, promedio, máximo, mínimo, producto, recuento distinto, etc.

 Aspose.Cells for Python via .NET proporciona[**Función de consolidación**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) enumeración para soportar las siguientes funciones de consolidación.

- Función de consolidación.PROMEDIO
- Función de consolidación.COUNT
- Función de consolidación.COUNT_NUMS
- Función de consolidación.DISTINCT_COUNT
- Función de consolidación.MAX
- Función de consolidación.MIN
- Función de consolidación.PRODUCTO
- Función de consolidación.STD_DEV
- Función de consolidación.STD_DEVP
- Función de consolidación.SUM
- FunciónConsolidación.VAR
- Función de consolidación.VARP

###  **Aplicación de la función de consolidación a los campos de datos de la tabla dinámica**

 Se aplica el siguiente código**AVERAGE** función de consolidación al primer campo de datos (o campo de valor) y**DISTINCT_COUNT** función de consolidación al segundo campo de datos (o campo de valor).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

La función de consolidación DISTINCT_COUNT solo es compatible con Microsoft Excel 2013.

{{% /alert %}}
