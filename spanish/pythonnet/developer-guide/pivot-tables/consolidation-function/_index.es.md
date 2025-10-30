---
title: Función de consolidación
type: docs
weight: 20
url: /es/python-net/consolidation-function/
description: Cómo aplicar la Función de Consolidación a los Campos de Datos de la Tabla Dinámica con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca de Excel de Python, Función de Consolidación a Campos de Datos de Tabla Dinámica Usando la Biblioteca de Excel Aspose.Cells para Python.
---

## **Función de consolidación**

Aspose.Cells para Python via .NET se puede utilizar para aplicar la Función de Consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puede hacer clic con el botón derecho en el campo de valor y luego seleccionar la opción **Configuración del campo de valor...** y luego seleccionar la pestaña **Resumir valores por**. A partir de ahí, puede seleccionar cualquier Función de Consolidación de su elección, como Suma, Conteo, Promedio, Máx, Mín, Producto, Conteo distinto, etc.

Aspose.Cells para Python via .NET proporciona una enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) para admitir las siguientes funciones de consolidación.

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

## **Cómo aplicar la Función de Consolidación a los Campos de Datos de la Tabla Dinámica Usando la Biblioteca de Excel Aspose.Cells para Python**

El siguiente código aplica la función de consolidación **PROMEDIO** al primer campo de datos (o campo de valor) y la función de consolidación **CUENTA_DISTINTA** al segundo campo de datos (o campo de valor).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

La función de consolidación CUENTA_DISTINTA es compatible solo con Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
