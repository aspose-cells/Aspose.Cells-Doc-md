---
title: Función de consolidación con Golang vía C++
linktitle: Función de consolidación
type: docs
weight: 20
url: /es/go-cpp/consolidation-function/
description: Aprende cómo aplicar la FunciónDeConsolidación a campos de datos de una tabla dinámica usando Aspose.Cells con Golang vía C++.
---

## **Función de consolidación**

Aspose.Cells se puede utilizar para aplicar la Función de Consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puedes hacer clic derecho en el campo de valor y luego seleccionar la opción **Configuración del campo de valor...**, y luego seleccionar la pestaña **Resumir valores mediante**. Desde allí, puedes seleccionar cualquier Función de Consolidación de tu elección, como Suma, Conteo, Promedio, Máx, Mín, Producto, Conteo único, etc.

Aspose.Cells proporciona la enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/) para admitir las siguientes funciones de consolidación.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

El siguiente código aplica la función de consolidación **Promedio** al primer campo de datos (o campo de valor) y la función de consolidación **Conteo de valores distintos** al segundo campo de datos (o campo de valor).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

La función de consolidación Recuento único es compatible solo con Microsoft Excel 2013.

{{% /alert %}}
