---
title: Formato de tabla dinámica
type: docs
weight: 60
url: /es/java/formatting-pivot-table/
---
## **Aspecto de la tabla dinámica**

[Cómo crear una tabla dinámica](/cells/es/java/create-pivot-table/) mostró cómo crear una tabla dinámica simple. Este artículo va más allá y analiza cómo personalizar la apariencia de una tabla dinámica mediante el establecimiento de propiedades.

### **Configuración de opciones de formato de tabla dinámica**

 los[**Tabla dinámica**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) class le permite configurar varias opciones de formato para una tabla dinámica.

#### **Configuración de los tipos de formato automático y estilo de tabla dinámica**

 El ejemplo de código que sigue ilustra cómo configurar el tipo de formato automático y el tipo de estilo de tabla dinámica usando el[**Tipo de formato automático**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) y[**PivotTableStyleTypePivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) propiedades.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Configuración de las opciones de formato**

El ejemplo de código que sigue ilustra cómo establecer una serie de opciones de formato para un informe de tabla dinámica, incluida la adición de totales generales para filas y columnas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Configuración de las opciones de formato de PivotFields**

Además de controlar el formato de la tabla dinámica general, Aspose.Cells for Java permite un control preciso del formato de los campos de fila, columna y página.

#### **Configuración del formato de campos de fila, columna y página**

El ejemplo de código que sigue muestra cómo acceder a los campos de fila, acceder a una fila en particular, establecer subtotales, aplicar la clasificación automática y usar la opción AutoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Configuración del formato de los campos de datos**

Las siguientes líneas de código ilustran cómo dar formato a los campos de datos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modificar el estilo rápido de una tabla dinámica**

Los ejemplos de código que siguen muestran cómo modificar el estilo rápido aplicado a una tabla dinámica.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Borrado de campos pivote**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) tiene un método llamado[**claro()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()que borra los campos pivote. Úselo para borrar campos dinámicos en todas las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos dinámicos en el área de datos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Función de consolidación**

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

 Aspose.Cells se puede usar para aplicar ConsolidationFunction a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puede hacer clic derecho en el campo de valor y luego seleccionar**Configuración de campo de valor...** opción y luego seleccione la pestaña**Resumir valores por**. Desde allí, puede seleccionar cualquier función de consolidación de su elección, como Suma, Recuento, Promedio, Máx., Mín., Producto, Recuento distinto, etc.

 Aspose.Cells proporciona[**Función de consolidación**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) enumeración para admitir las siguientes funciones de consolidación.

- [**Función de consolidación.PROMEDIO**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**Función de consolidación.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Función de consolidación.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**Función de consolidación.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**Función de consolidación.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**Función de consolidación.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**Función de consolidación.PRODUCTO**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**Función de consolidación.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**Función de consolidación.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**Función de consolidación.SUMA**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**Función de consolidación.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**Función de consolidación.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Se aplica el siguiente código**Promedio** función de consolidación al primer campo de datos (o campo de valor) y**DistinctCount** función de consolidación al segundo campo de datos (o campo de valor).

{{% alert color="primary" %}}

La función de consolidación DistinctCount solo es compatible con Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
