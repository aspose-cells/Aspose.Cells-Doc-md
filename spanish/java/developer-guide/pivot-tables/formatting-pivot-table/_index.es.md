---
title: Dar formato a la tabla dinámica
type: docs
weight: 60
url: /es/java/formatting-pivot-table/
---

## **Apariencia de la tabla dinámica**

[Cómo crear una tabla dinámica](/cells/es/java/create-pivot-table/) mostró cómo crear una tabla dinámica simple. Este artículo va más allá y discute cómo personalizar la apariencia de una tabla dinámica configurando propiedades.

### **Configuración de opciones de formato de tabla dinámica**

La clase [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) te permite establecer varias opciones de formato para una tabla dinámica.

#### **Configuración de los tipos de AutoFormato y PivotTableStyle**

El ejemplo de código que sigue ilustra cómo establecer el tipo de autoformato y el tipo de estilo de tabla dinámica utilizando las propiedades [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) y [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Configuración de opciones de formato**

El ejemplo de código que sigue ilustra cómo establecer varias opciones de formato para un informe de tabla dinámica, incluyendo la adición de totales generales para filas y columnas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Configuración de opciones de formato de PivotFields**

Además de controlar el formato de la tabla dinámica en general, Aspose.Cells for Java permite un control detallado del formato para campos de fila, campos de columna y campos de página.

#### **Configuración de formato de campos de fila, columna y página**

El ejemplo de código que sigue muestra cómo acceder a campos de fila, acceder a una fila en particular, establecer subtotales, aplicar ordenamiento automático y usar la opción autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Configuración de formato de campos de datos**

Las siguientes líneas de código ilustran cómo dar formato a campos de datos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modificar el estilo rápido de una tabla dinámica**

Los ejemplos de código que siguen muestran cómo modificar el estilo rápido aplicado a una tabla dinámica.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Borrado de campos de tabla dinámica**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) tiene un método llamado [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) que borra los campos de tabla dinámica. Úsalo para limpiar los campos de tabla dinámica en todas las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos de la tabla dinámica en el área de datos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Función de consolidación**

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

Aspose.Cells se puede usar para aplicar la función de consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puedes hacer clic derecho en el campo de valor y luego seleccionar la opción **Configuración del campo de valor** y después seleccionar la pestaña **Resumir valores por**. Desde allí, puedes seleccionar cualquier función de consolidación de tu elección, como Suma, Contar, Promedio, Máx, Mín, Producto, Contar valores distintos, etc.

Aspose.Cells proporciona la enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) para admitir las siguientes funciones de consolidación.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

El siguiente código aplica la función de consolidación **Promedio** al primer campo de datos (o campo de valor) y la función de consolidación **Recuento único** al segundo campo de datos (o campo de valor).

{{% alert color="primary" %}}

La función de consolidación Recuento único es compatible solo con Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
