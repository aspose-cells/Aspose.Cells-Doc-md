---
title: Uso de Marcadores Inteligentes
type: docs
weight: 40
url: /es/java/using-smart-markers/
---

## **Introducción**

{{% alert color="primary" %}}

**Los marcadores inteligentes** se utilizan para que Aspose.Cells sepa qué información colocar en una [hoja de cálculo de diseñador](/cells/es/java/what-is-a-designer-spreadsheet/) de Microsoft Excel. Los marcadores inteligentes le permiten crear plantillas que contienen solo información relevante y formato.

{{% /alert %}}

## **Hoja de cálculo de diseño y Marcadores inteligentes**

Las hojas de cálculo de diseñador son archivos de Excel estándar que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información para contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de un marcador de datos es &=Party.FullName. Si el marcador de datos resulta en más de un elemento, por ejemplo, una fila completa, entonces las filas siguientes se mueven automáticamente para dejar espacio para la nueva información. De esta forma, los subtotales y totales se pueden colocar en la fila inmediatamente después del marcador de datos para realizar cálculos basados en los datos insertados. Para realizar cálculos en las filas insertadas, use [fórmulas dinámicas](/cells/es/java/using-smart-markers/#dynamic-formulas).

Los marcadores inteligentes consisten en las partes de **fuente de datos** y **nombre del campo** para la mayoría de la información. También se puede enviar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Utilice solo un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

Un marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se organiza la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.

### **Opciones de Marcador Inteligente**

&=DataSource.FieldName
&=[Data Source].[Field Name]
&=$VariableName
&=$VariableArray
&==DynamicFormula
&=&=RepeatDynamicFormula

### **Parámetros**

Se permiten los siguientes parámetros:

- **noadd** - No agregar filas adicionales para ajustar los datos.
- **skip:n** - Omitir n filas por cada fila de datos.
- *ascendente:n o descendente:n* - Ordena los datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del ordenador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo: &=Table1.Field3(ascendente:1).
- **horizontal** - Escribir datos de izquierda a derecha, en lugar de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **shift** - Desplaza hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro de cambio funciona de la misma manera que en Microsoft Excel. Por ejemplo en Microsoft Excel, cuando seleccionas un rango de celdas, haces clic con el botón derecho y seleccionas **Insertar** y especificas **desplazar celdas hacia abajo**, **desplazar celdas hacia la derecha** y otras opciones. En resumen, el parámetro de cambio cumple la misma función para los marcadores inteligentes verticales/normales (de arriba a abajo) o horizontales (de izquierda a derecha).
- **bean** - Indica que la fuente de datos es un POJO simple. Solo compatible en la API de Java.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternada.

Si tiene varios parámetros, sepárelos con una coma, pero sin espacio: parámetroA, parámetroB, parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en cada otra fila.

![todo:image_alt_text](using-smart-markers_1.png)

**se convierte en...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Fórmulas dinámicas**

Las fórmulas dinámicas te permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r - Número de fila actual.
- 2, -1 - Desplazamiento al número de fila actual.

Lo siguiente ilustra una fórmula dinámica repetida y la hoja de cálculo de Excel resultante.

![todo:image_alt_text](using-smart-markers_3.png)

**se convierte en…**

![todo:image_alt_text](using-smart-markers_4.png)

La celda C1 contiene la fórmula =A1*B1, C2 contiene = A2*B2 y C3 = A3*B3.

Es muy fácil procesar los marcadores inteligentes. El siguiente ejemplo de código muestra cómo usar fórmulas dinámicas en marcadores inteligentes. Cargamos el [archivo de plantilla](templateDynamicFormulas.xlsx) y creamos datos de prueba, procesamos los marcadores para llenar datos en las celdas del marcador. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Usar Arrays Variables**

El siguiente código de ejemplo muestra cómo utilizar matrices de variables en Smart Markers. Colocamos un marcador de matriz de variables en la celda A1 de la primera hoja de cálculo del libro de trabajo dinámicamente, que contiene una cadena de valores que establecemos para el marcador, procesamos los marcadores para llenar datos en las celdas contra el marcador. Finalmente, guardamos el archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Agrupación de datos**

En algunos informes de Excel es posible que necesite dividir los datos en grupos para que sea más fácil de leer y analizar. Uno de los propósitos principales para dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes de Aspose.Cells te permiten agrupar datos por campos establecidos y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si agrupas datos por Clientes.CustomerID, puedes agregar un registro de resumen cada vez que cambie el grupo.

### **Parámetros**

A continuación se muestran algunos parámetros de marcadores inteligentes utilizados para agrupar datos.

#### **group:normal/merge/repeat**

Soportamos tres tipos de grupos entre los que puede elegir.

- **normal** - El valor del campo o campos de agrupación no se repite para los registros correspondientes en la columna; en su lugar se imprimen una vez por grupo de datos.
- **merge** - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en los campos de agrupación para cada conjunto de grupos.
- **repeat** - El valor del campo o campos de agrupación se repite para los registros correspondientes.

Por ejemplo: &=Clientes.IDCliente(grupo:merge)

#### **skip**

Salta un número específico de filas después de cada grupo.

Por ejemplo, &=Employees.EmployeeID(group:normal,skip:1)

#### **subtotalN**

Realiza una operación de resumen para un campo de datos especificado relacionado con un campo de agrupación. La N representa números del 1 al 11 que especifican la función utilizada al calcular los subtotales dentro de una lista de datos. (1=PROMEDIO, 2=CONTAR, 3=CONTARA, 4=MÁXIMO, 5=MÍNIMO,...9=SUMA, etc.) Consulta la referencia de subtotales en la ayuda de Microsoft Excel para más detalles.

El formato realmente se declara como:
subtotalN:Ref donde Ref se refiere a la columna de agrupación.

Por ejemplo,

- &=Productos.Unidades(subtotal9:Productos.IDProducto) especifica la función de resumen sobre el campo **Unidades** con respecto al campo **IDProducto** en la tabla **Productos**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) especifica la función de resumen sobre el campo **Col3** agrupado por **Col1** en la tabla **Tabx**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) especifica la función de resumen en el campo **ColumnD** agrupado por **ColumnA** y **ColumnB** en la tabla **Table1**.

## **Usar objetos anidados**

Aspose.Cells admite objetos anidados en marcadores inteligentes, los objetos anidados deben ser simples.

Usamos un archivo de plantilla simple. Vea la hoja de cálculo de diseño que contiene algunos marcadores inteligentes anidados.

**La primera hoja de cálculo del archivo de diseño muestra marcadores inteligentes anidados.**

![todo:image_alt_text](using-smart-markers_5.png)

El ejemplo que sigue muestra cómo funciona esto. Ejecutar el código a continuación da como resultado la salida a continuación.

**La primera hoja de cálculo del archivo de salida muestra los datos resultantes.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Usando una Lista Genérica como Objeto Anidado**

Ahora Aspose.Cells también admite el uso de una lista genérica como un objeto anidado. Consulte la captura de pantalla del archivo de Excel de salida generado con el siguiente código. Como se puede ver en la captura de pantalla, un objeto Teacher contiene múltiples objetos estudiantes anidados.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Usar la propiedad HTML de Marcadores Inteligentes**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Recibir notificaciones mientras se fusionan datos con Marcadores Inteligentes**

A veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el marcador inteligente particular que se está procesando antes de la finalización. Esto se puede lograr usando la propiedad [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) y [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Para el código de ejemplo y la explicación detallada, consulte este artículo.

- [Recibir notificaciones mientras se fusionan datos con Marcadores Inteligentes](/cells/es/java/getting-notifications-while-merging-data-with-smart-markers/)
