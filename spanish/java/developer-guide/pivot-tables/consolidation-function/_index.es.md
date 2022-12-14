---
title: Función de consolidación
type: docs
weight: 20
url: /es/java/consolidation-function/
description: Aplicar ConsolidationFunction a los campos de datos de la tabla dinámica.
---
## **Función de consolidación**

 Aspose.Cells se puede usar para aplicar ConsolidationFunction a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puede hacer clic derecho en el campo de valor y luego seleccionar**Configuración de campo de valor...** opción y luego seleccione la pestaña**Resumir valores por**. Desde allí, puede seleccionar cualquier función de consolidación de su elección, como Suma, Conteo, Promedio, Máx., Mín., Producto, Conteo distinto, etc.

 Aspose.Cells proporciona[**Función de consolidación**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) enumeración para admitir las siguientes funciones de consolidación.

- Función de consolidación.SUMA
- Función de consolidación.COUNT
- Función de consolidación.PROMEDIO
- Función de consolidación.MAX
- Función de consolidación.MIN
- Función de consolidación.PRODUCTO
- Función de consolidación.COUNT_NUMS
- Función de consolidación.STD_DEV
- Función de consolidación.STD_DEVP
- Función de consolidación.VAR
- Función de consolidación.VARP
- Función de consolidación.DISTINCT_COUNT

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

 Se aplica el siguiente código**PROMEDIO** función de consolidación al primer campo de datos (o campo de valor) y**STD_DEV** función de consolidación al segundo campo de datos (o campo de valor).

El archivo fuente de muestra y los archivos de salida se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](source.xlsx)

[Archivo de Excel de salida](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

La función de consolidación DistinctCount solo es compatible con Microsoft Excel 2013.

{{% /alert %}}

