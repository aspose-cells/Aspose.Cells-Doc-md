---
title: Función de consolidación
type: docs
weight: 20
url: /es/net/consolidation-function/
---
## **Función de consolidación**

 Aspose.Cells se puede usar para aplicar ConsolidationFunction a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puede hacer clic derecho en el campo de valor y luego seleccionar**Configuración de campo de valor...** opción y luego seleccione la pestaña**Resumir valores por**. Desde allí, puede seleccionar cualquier función de consolidación de su elección, como Suma, Conteo, Promedio, Máx., Mín., Producto, Conteo distinto, etc.

 Aspose.Cells proporciona[**Función de consolidación**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) enumeración para admitir las siguientes funciones de consolidación.

- Función de consolidación.Promedio
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- Función de consolidación.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Suma
- Función de consolidación.Var
- ConsolidationFunction.Varp

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

 Se aplica el siguiente código**Promedio** función de consolidación al primer campo de datos (o campo de valor) y**DistinctCount** función de consolidación al segundo campo de datos (o campo de valor).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

La función de consolidación DistinctCount solo es compatible con Microsoft Excel 2013.

{{% /alert %}}
