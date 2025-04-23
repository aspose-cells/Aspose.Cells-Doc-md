---
title: Función de consolidación
type: docs
weight: 20
url: /es/java/consolidation-function/
description: Aplicar la función de consolidación a los campos de datos de la tabla dinámica.
---

## **Función de consolidación**

Aspose.Cells se puede utilizar para aplicar la Función de Consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puedes hacer clic derecho en el campo de valor y luego seleccionar la opción **Configuración del campo de valor...**, y luego seleccionar la pestaña **Resumir valores mediante**. Desde allí, puedes seleccionar cualquier Función de Consolidación de tu elección, como Suma, Conteo, Promedio, Máx, Mín, Producto, Conteo único, etc.

Aspose.Cells proporciona la enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) para admitir las siguientes funciones de consolidación.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

El siguiente código aplica la función de consolidación **PROMEDIO** al primer campo de datos (o campo de valor) y la función de consolidación **DESV_EST** al segundo campo de datos (o campo de valor).

El archivo fuente de ejemplo y los archivos de salida se pueden descargar desde aquí para probar el código de ejemplo:

[Archivo Excel de origen](source.xlsx)

[Archivo Excel de salida](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

La función de consolidación Recuento único es compatible solo con Microsoft Excel 2013.

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
