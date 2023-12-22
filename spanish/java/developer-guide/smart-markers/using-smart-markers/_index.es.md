---
title: Usando marcadores inteligentes
type: docs
weight: 40
url: /es/java/using-smart-markers/
---
##  **Introducción**

{{% alert color="primary" %}}

**Marcadores inteligentes** se utilizan para que Aspose.Cells sepa qué información colocar en un Microsoft Excel[hoja de cálculo del diseñador](/cells/es/java/what-is-a-designer-spreadsheet/). Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato relevantes.

{{% /alert %}}

##  **Hoja de cálculo de diseñador y marcadores inteligentes**

Las hojas de cálculo de Designer son archivos estándar de Excel que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hagan referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, las siguientes filas se mueven hacia abajo automáticamente para dejar espacio para la nueva información. Por lo tanto, los subtotales y totales se pueden colocar en la fila inmediatamente después del marcador de datos para realizar cálculos basados en los datos insertados. Para realizar cálculos en las filas insertadas, utilice[fórmulas dinámicas](/cells/es/java/using-smart-markers/#dynamic-formulas).

 Los marcadores inteligentes consisten en**fuente de datos** y**nombre del campo** partes para obtener la mayor parte de la información. También se puede pasar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Utilice únicamente un marcador de datos por celda. Se eliminan los marcadores inteligentes no utilizados.

Un marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se presenta la información. Se añaden al final del marcador inteligente entre paréntesis como una lista separada por comas.

###  **Opciones de marcador inteligente**

&=Origen de datos.Nombre de campo
&=[Fuente de datos].[Nombre de campo]
&=$Nombre de variable
&=$matrizvariable
&==Fórmula dinámica
&=&=Repetir fórmula dinámica

###  **Parámetros**

Se permiten los siguientes parámetros:

- **no agregar** - No agregue filas adicionales para ajustar los datos.
- **saltar: n** - Saltar n número de filas para cada fila de datos.
- *ascendente:n o descendente:n - Ordena datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del clasificador. Los datos se clasifican después de procesar la fuente de datos. Por ejemplo: &=Table1.Field3(ascendente:1).
- **horizontal** - Escribe datos de izquierda a derecha, en lugar de de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **cambio** - Desplazarse hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro de cambio funciona de la misma manera que en Microsoft Excel. Por ejemplo, en Microsoft Excel, cuando selecciona un rango de celdas, haga clic derecho y seleccione**Insertar** y especificar**desplazar celdas hacia abajo**, **desplazar celdas hacia la derecha** y otras opciones. En resumen, el parámetro de desplazamiento cumple la misma función para los marcadores inteligentes verticales/normales (de arriba a abajo) u horizontales (de izquierda a derecha).
- **frijol** - Indica que la fuente de datos es un POJO simple. Solo se admite en el Java API.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Si tiene varios parámetros, sepárelos con una coma, pero sin espacios: parámetroA, parámetroB, parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en filas alternas.

![todo:image_alt_text](using-smart-markers_1.png)

**se convierte...**

![todo:image_alt_text](using-smart-markers_2.png)

###  **Fórmulas dinámicas**

Las fórmulas dinámicas le permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r: número de fila actual.
- 2, -1: desplazamiento al número de fila actual.

A continuación se ilustra una fórmula dinámica repetida y la hoja de cálculo de Excel resultante.

![todo:image_alt_text](using-smart-markers_3.png)

**se convierte…**

![todo:image_alt_text](using-smart-markers_4.png)

Cell C1 contiene la fórmula =A1*B1, C2 contiene = A2*B2 y C3 = A3*B3.

 Es muy fácil procesar los marcadores inteligentes. El siguiente código de ejemplo muestra cómo utilizar fórmulas dinámicas en marcadores inteligentes. cargamos el[archivo de plantilla](templateDynamicFormulas.xlsx) y crear datos de prueba, procesar los marcadores para completar los datos en las celdas contra el marcador.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **Usando matrices de variables**

El siguiente código de ejemplo muestra cómo utilizar matrices de variables en marcadores inteligentes. Colocamos dinámicamente un marcador de matriz variable en la celda A1 de la primera hoja de trabajo del libro de trabajo que contiene una cadena de valores que configuramos para el marcador, procesamos los marcadores para completar los datos en las celdas contra el marcador. Finalmente guardamos el archivo Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **Agrupación de datos**

En algunos informes de Excel, es posible que necesite dividir los datos en grupos para que sean más fáciles de leer y analizar. Uno de los propósitos principales para dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes Aspose.Cells le permiten agrupar datos por campos establecidos y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si agrupa datos por Clientes.ID de cliente, puede agregar un registro de resumen cada vez que cambie el grupo.

###  **Parámetros**

A continuación se muestran algunos parámetros de marcador inteligente utilizados para agrupar datos.

####  **grupo:normal/fusionar/repetir**

Admitimos tres tipos de grupos entre los que puede elegir.

- **normal** - El valor de agrupar por campo(s) no se repetirá para los registros correspondientes en la columna; en lugar de eso, se imprimen una vez por grupo de datos.
- **unir** - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas del grupo por campo(s) para cada conjunto de grupos.
- **repetir** - El valor de agrupar por campo(s) se repite para los registros correspondientes.

Por ejemplo: &=Clientes.CustomerID(grupo:fusionar)

####  **saltar**

Salta un número específico de filas después de cada grupo.

Por ejemplo &=Empleados.ID de empleado(grupo:normal,saltar:1)

####  **subtotalN**

Realiza una operación de resumen para los datos de un campo específico relacionados con un grupo por campo. La N representa números entre 1 y 11 que especifican la función utilizada al calcular los subtotales dentro de una lista de datos. (1=PROMEDIO, 2=CONTAR, 3=CONTAR, 4=MÁX, 5=MIN,...9=SUM, etc.) Consulte la referencia de Subtotal en la ayuda de Excel Microsoft para obtener más detalles.

El formato en realidad dice como:
subtotalN:Ref donde Ref se refiere al grupo por columna.

Por ejemplo,

-  &=Products.Units(subtotal9:Products.ProductID) especifica la función de resumen sobre**Unidades** campo con respecto a la**ID del Producto** campo en el**Productos** mesa.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) especifica la función de resumen en el**Col3** grupo de campos por**Col1** en la tabla *Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) especifica la función de resumen sobre**ColumnaD** grupo de campos por**ColumnaA** y**Columna B** en la tabla *Tabla1**.

##  **Usar objetos anidados**

Aspose.Cells admite objetos anidados en marcadores inteligentes; los objetos anidados deben ser simples.

Usamos un archivo de plantilla simple. Consulte la hoja de cálculo del diseñador que contiene algunos marcadores inteligentes anidados.

**La primera hoja de trabajo del archivo del diseñador que muestra marcadores inteligentes anidados.**

![todo:image_alt_text](using-smart-markers_5.png)

El siguiente ejemplo muestra cómo funciona esto. Al ejecutar el código siguiente se obtiene el siguiente resultado.

**La primera hoja de trabajo del archivo de salida que muestra los datos resultantes.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **Usar lista genérica como objeto anidado**

Aspose.Cells ahora también admite el uso de una lista genérica como objeto anidado. Consulte la captura de pantalla del archivo Excel de salida generado con el siguiente código. Como puede ver en la captura de pantalla, un objeto Profesor contiene varios objetos de estudiantes anidados.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **Usando la propiedad HTML de Smart Markers**

El siguiente código de muestra explica el uso de la propiedad HTML de los marcadores inteligentes. Cuando se procese, mostrará "Mundo" en "Hello World" en negrita debido a HTML \<b> etiqueta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **Recibir notificaciones mientras se fusionan datos con marcadores inteligentes**

 A veces, puede ser necesario recibir notificaciones sobre la referencia de la celda o el marcador inteligente en particular que se está procesando antes de su finalización. Esto se puede lograr utilizando el[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)propiedad y[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Para obtener un código de muestra y una explicación detallada, consulte este artículo.

- [Recibir notificaciones mientras se fusionan datos con marcadores inteligentes](/cells/es/java/getting-notifications-while-merging-data-with-smart-markers/)
