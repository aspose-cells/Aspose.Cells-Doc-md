---
title: Uso de marcadores inteligentes
type: docs
weight: 40
url: /es/java/using-smart-markers/
---
## **Introducción**

{{% alert color="primary" %}}

**Marcadores inteligentes** se utilizan para que Aspose.Cells sepa qué información colocar en un Microsoft Excel[hoja de cálculo del diseñador](/cells/es/java/what-is-a-designer-spreadsheet/). Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato relevantes.

{{% /alert %}}

## **Diseñador de hojas de cálculo y marcadores inteligentes**

Las hojas de cálculo de Designer son archivos estándar de Excel que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea información.

 Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, las siguientes filas se mueven hacia abajo automáticamente para dejar espacio para la nueva información. Por lo tanto, los subtotales y los totales se pueden colocar en la fila inmediatamente después del marcador de datos para realizar cálculos basados en los datos insertados. Para hacer cálculos en las filas insertadas, use[fórmulas dinámicas](/cells/es/java/using-smart-markers/#dynamic-formulas).

 Los marcadores inteligentes consisten en la**fuente de datos** y**nombre del campo**piezas para la mayoría de la información. También se puede pasar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Solo use un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

Un marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se presenta la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.

### **Opciones de marcador inteligente**

&=FuenteDeDatos.NombreDeCampo
&=[Fuente de datos].[Nombre de campo]&=$Nombre de variable
&=$VariableArray
&==Fórmula dinámica
&=&=Fórmula dinámica repetida

### **Parámetros**

Se permiten los siguientes parámetros:

- **no agregar** - No agregue filas adicionales para ajustar los datos.
- **saltar: n** - Saltar n número de filas para cada fila de datos.
- *ascendente:n o descendente:n - Ordenar datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del clasificador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo: &=Tabla1.Campo3(ascendente:1).
- **horizontal** - Escriba los datos de izquierda a derecha, en lugar de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **cambio** - Desplace hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro shift funciona de la misma manera que en Microsoft Excel. Por ejemplo, en Microsoft Excel, cuando selecciona un rango de celdas, haga clic con el botón derecho y seleccione**Insertar** y especificar**cambiar las celdas hacia abajo**, **desplazar celdas a la derecha** y otras opciones. En resumen, el parámetro de desplazamiento cumple la misma función para marcadores inteligentes verticales/normales (de arriba a abajo) u horizontales (de izquierda a derecha).
- **frijol** - Indica que la fuente de datos es un POJO simple. Solo se admite en el Java API.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Si tiene varios parámetros, sepárelos con una coma, pero sin espacios: parámetroA, parámetroB, parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en filas alternas.

![todo:imagen_alternativa_texto](using-smart-markers_1.png)

**se convierte...**

![todo:imagen_alternativa_texto](using-smart-markers_2.png)

### **Fórmulas dinámicas**

Las fórmulas dinámicas le permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r - Número de fila actual.
- 2, -1 - Desplazamiento al número de fila actual.

A continuación se ilustra una fórmula dinámica repetitiva y la hoja de cálculo de Excel resultante.

![todo:imagen_alternativa_texto](using-smart-markers_3.png)

**se convierte…**

![todo:imagen_alternativa_texto](using-smart-markers_4.png)

Cell C1 contiene la fórmula =A1*B1, C2 contiene = A2*B2 y C3 = A3*B3.

Es muy fácil procesar los marcadores inteligentes. El siguiente fragmento de código muestra cómo se hace.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Uso de matrices de variables**

El siguiente código de ejemplo muestra cómo usar matrices de variables en marcadores inteligentes. Colocamos un marcador de matriz variable en la celda A1 de la primera hoja de trabajo del libro de trabajo dinámicamente que contiene una cadena de valores que establecemos para el marcador, procesamos los marcadores para completar los datos en las celdas contra el marcador. Finalmente, guardamos el archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Agrupación de datos**

En algunos informes de Excel, es posible que deba dividir los datos en grupos para facilitar la lectura y el análisis. Uno de los principales propósitos de dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes Aspose.Cells le permiten agrupar datos por conjuntos de campos y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si agrupa datos por Customers.CustomerID, puede agregar un registro de resumen cada vez que cambie el grupo.

### **Parámetros**

Los siguientes son algunos parámetros de marcadores inteligentes utilizados para agrupar datos.

#### **grupo:normal/fusionar/repetir**

Admitimos tres tipos de grupos entre los que puede elegir.

- **normal** - El valor de agrupar por campo(s) no se repetirá para los registros correspondientes en la columna; en su lugar, se imprimen una vez por grupo de datos.
- **unir** - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en el grupo por campo(s) para cada conjunto de grupos.
- **repetir** - El valor de agrupar por campo(s) se repite para los registros correspondientes.

Por ejemplo: &=Clientes.IDCliente(grupo:combinar)

#### **saltar**

Salta un número específico de filas después de cada grupo.

Por ejemplo &=Empleados.EmployeeID(grupo:normal,saltar:1)

#### **subtotalN**

Realiza una operación de resumen para un campo de datos específico relacionado con un grupo por campo. La N representa números entre 1 y 11 que especifican la función utilizada al calcular subtotales dentro de una lista de datos. (1=PROMEDIO, 2=CUENTA, 3=CUENTAA, 4=MAX, 5=MIN,...9=SUMA, etc.) Consulte la referencia de subtotal en la ayuda de Excel Microsoft para obtener más detalles.

El formato en realidad dice como:
subtotalN:Ref donde Ref se refiere al grupo por columna.

Por ejemplo,

-  &=Productos.Unidades(subtotal9:Productos.ProductID) especifica la función de resumen en**Unidades** campo con respecto a la**Identificación de producto** campo en el**Productos** mesa.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) especifica la función de resumen en el**Col3** grupo de campo por**Col1** en la mesa**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) especifica la función de resumen en**columnaD** grupo de campo por**columnaA** y**columnaB** en mesa**Tabla 1**.

## **Uso de objetos anidados**

Aspose.Cells admite objetos anidados en marcadores inteligentes, los objetos anidados deben ser simples.

Usamos un archivo de plantilla simple. Consulte la hoja de cálculo del diseñador que contiene algunos marcadores inteligentes anidados.

**La primera hoja de trabajo del archivo del diseñador que muestra marcadores inteligentes anidados.**

![todo:imagen_alternativa_texto](using-smart-markers_5.png)

El ejemplo que sigue muestra cómo funciona esto. Ejecutar el siguiente código da como resultado el siguiente resultado.

**La primera hoja de cálculo del archivo de salida que muestra los datos resultantes.**

![todo:imagen_alternativa_texto](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Usar lista genérica como objeto anidado**

Aspose.Cells ahora también admite el uso de una lista genérica como objeto anidado. Verifique la captura de pantalla del archivo de salida de Excel generado con el siguiente código. Como puede ver en la captura de pantalla, un objeto Profesor contiene varios objetos de estudiante anidados.

![todo:imagen_alternativa_texto](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Uso de la propiedad HTML de marcadores inteligentes**

El siguiente código de ejemplo explica el uso de la propiedad HTML de los marcadores inteligentes. Cuando se procese, mostrará "Mundo" en "Hello World" en negrita debido a HTML \<b>etiqueta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Recibir notificaciones al fusionar datos con marcadores inteligentes**

 A veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el marcador inteligente en particular que se está procesando antes de la finalización. Esto se puede lograr usando el[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)propiedad y[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Para obtener un código de muestra y una explicación detallada, consulte este artículo.

- [Recibir notificaciones al fusionar datos con marcadores inteligentes](/cells/es/java/getting-notifications-while-merging-data-with-smart-markers/)
