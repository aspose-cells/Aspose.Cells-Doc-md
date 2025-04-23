---
title: Función de consolidación
type: docs
weight: 20
url: /es/nodejs-cpp/consolidation-function/
description: Cómo aplicar la función de consolidación (ConsolidationFunction) a los campos de datos de una tabla dinámica con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, biblioteca de Node.js para Excel, ConsolidationFunction en los campos de datos de la tabla dinámica usando la biblioteca Excel Aspose.Cells for Node.js via C++.
---

## **Función de consolidación**

Aspose.Cells for Node.js via C++ se puede usar para aplicar la función de consolidación (ConsolidationFunction) a los campos de datos (o campos de valores) de la tabla dinámica. En Microsoft Excel, puedes hacer clic derecho en el campo de valor y seleccionar la opción **Configuración de campo de valor...** y luego elegir la pestaña **Resumir valores por**. Desde allí, puedes seleccionar cualquier función de consolidación de tu elección como Suma, Cuenta, Promedio, Máximo, Mínimo, Producto, Cuenta distinta, etc.

Aspose.Cells for Node.js via C++ proporciona [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) enumeración para soportar las siguientes funciones de consolidación.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Cómo aplicar la función de consolidación (ConsolidationFunction) a los campos de datos de una tabla dinámica usando Aspose.Cells for Node.js via C++**

El siguiente código aplica la función de consolidación **Promedio** al primer campo de datos (o campo de valor) y la función de consolidación **Conteo de valores distintos** al segundo campo de datos (o campo de valor).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

La función de consolidación CUENTA_DISTINTA es compatible solo con Microsoft Excel 2013.

{{% /alert %}}
