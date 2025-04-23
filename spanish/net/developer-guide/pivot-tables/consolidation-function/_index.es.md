---
title: Función de consolidación
type: docs
weight: 20
url: /es/net/consolidation-function/
---

## **Función de consolidación**

Aspose.Cells se puede utilizar para aplicar la Función de Consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puedes hacer clic derecho en el campo de valor y luego seleccionar la opción **Configuración del campo de valor...**, y luego seleccionar la pestaña **Resumir valores mediante**. Desde allí, puedes seleccionar cualquier Función de Consolidación de tu elección, como Suma, Conteo, Promedio, Máx, Mín, Producto, Conteo único, etc.

Aspose.Cells proporciona la enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) para admitir las siguientes funciones de consolidación.

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

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

El siguiente código aplica la función de consolidación **Promedio** al primer campo de datos (o campo de valor) y la función de consolidación **Conteo de valores distintos** al segundo campo de datos (o campo de valor).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

La función de consolidación Recuento único es compatible solo con Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
