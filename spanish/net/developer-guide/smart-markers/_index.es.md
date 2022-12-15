---
title: Importar y colocar datos de forma inteligente con marcadores inteligentes
linktitle: Marcadores inteligentes
type: docs
weight: 190
url: /es/net/using-smart-markers/
description: Importación y colocación inteligente de datos según la plantilla de archivos de Excel con la biblioteca Aspose.Cells.
---
## **Introducción**
**Marcadores inteligentes**se utilizan para que Aspose.Cells sepa qué información colocar en una hoja de cálculo de Microsoft diseñador de Excel. Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato específicos.
## **Diseñador de hojas de cálculo y marcadores inteligentes**
Las hojas de cálculo de Designer son archivos estándar de Excel que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

 Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, las siguientes filas se mueven hacia abajo automáticamente para dejar espacio para la nueva información. Por lo tanto, los subtotales y los totales se pueden colocar en la fila inmediatamente después del marcador de datos para realizar cálculos basados en los datos insertados. Para hacer cálculos en las filas insertadas, use**fórmulas dinámicas**.

 Los marcadores inteligentes consisten en la**fuente de datos** y**nombre del campo**piezas para la mayoría de la información. También se puede pasar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Solo use un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

El marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se presenta la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.
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
- **ascendente:n** o**descendente:n** - Ordenar datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del clasificador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo: &=Tabla1.Campo3(ascendente:1).
- **horizontal** - Escriba los datos de izquierda a derecha, en lugar de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **cambio** - Desplace hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro shift funciona de la misma manera que en Microsoft Excel. Por ejemplo, en Microsoft Excel, cuando selecciona un rango de celdas, haga clic con el botón derecho y seleccione**Insertar** y especificar**cambiar las celdas hacia abajo**, **desplazar celdas a la derecha** y otras opciones. En resumen, el**cambio** El parámetro cumple la misma función para marcadores inteligentes verticales/normales (de arriba a abajo) u horizontales (de izquierda a derecha).
- **estilo de copia** - Copie el estilo de la celda base a todas las celdas de esa columna.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Si tiene varios parámetros, sepárelos con comas, pero sin espacios: parámetroA, parámetroB, parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en filas alternas.

|**Archivo de plantilla**|**Archivo de salida**|
|:- |:- |
|![todo:imagen_alternativa_texto](using-smart-markers_1.jpg)|![todo:imagen_alternativa_texto](using-smart-markers_2.jpg)|
### **Fórmulas dinámicas**
Las fórmulas dinámicas le permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r - Número de fila actual.
- 2, -1 - Desplazamiento al número de fila actual.

Por ejemplo:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

En el marcador de fórmula dinámica, "-1" indica el desplazamiento de la fila actual en las columnas B y C, respectivamente, que se configurará para la operación de división, el parámetro de omisión es una fila. Además, debemos especificar el siguiente carácter:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

como carácter separador para aplicar más parámetros en fórmulas dinámicas.

Las siguientes capturas de pantalla ilustran una fórmula dinámica repetitiva y la hoja de cálculo de Excel resultante.

|**Archivo de plantilla**|**Archivo de salida**|
|:- |:- |
|![todo:imagen_alternativa_texto](using-smart-markers_3.jpg)|![todo:imagen_alternativa_texto](using-smart-markers_4.jpg)|
 Cell "C1" contiene la fórmula**= A1*B1** , la celda "C2" contiene**= A2*B2** y la celda "C3" contiene**= A3*B3**.

Es muy fácil procesar los marcadores inteligentes. Lo que sigue son dos fragmentos de código, uno en C# y otro en VB, que muestra cómo se hace.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **Uso de matrices de variables**
El siguiente código de ejemplo muestra cómo usar matrices de variables en marcadores inteligentes. Colocamos un marcador de matriz variable en la celda A1 de la primera hoja de trabajo del libro de trabajo dinámicamente que contiene una cadena de valores que establecemos para el marcador, procesamos los marcadores para completar los datos en las celdas contra el marcador. Finalmente guardamos el archivo de Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Agrupación de datos**
En algunos informes de Excel, es posible que deba dividir los datos en grupos para facilitar la lectura y el análisis. Uno de los principales propósitos de dividir los datos en grupos es ejecutar cálculos (realizar operaciones de resumen) en cada grupo de registros.

Los marcadores inteligentes Aspose.Cells le permiten agrupar datos por campos y colocar filas de resumen entre conjuntos de datos o grupos de datos. Por ejemplo, si agrupa datos por Customers.CustomerID, puede agregar un registro de resumen cada vez que cambie el grupo.
### **Parámetros**
Los siguientes son algunos de los parámetros de marcadores inteligentes utilizados para agrupar datos.
#### **grupo:normal/fusionar/repetir**
Admitimos tres tipos de grupos entre los que puede elegir.

- **normal** - El valor de agrupar por campo(s) no se repetirá para los registros correspondientes en la columna; en su lugar, se imprimen una vez por grupo de datos.
- **unir** - El mismo comportamiento que para el parámetro normal, excepto que fusiona las celdas en el grupo por campo(s) para cada conjunto de grupos.
- **repetir** - El valor de agrupar por campo(s) se repite para los registros correspondientes.

Por ejemplo: &=Clientes.IDCliente(grupo:combinar)
#### **saltar**
Salta un número específico de filas después de cada grupo.

Por ejemplo, &=Empleados.IDEmpleado(grupo:normal,saltar:1)
#### **subtotalN**
Realiza una operación de resumen para un campo de datos específico relacionado con un grupo por campo. La N representa números entre 1 y 11 que especifican la función utilizada al calcular subtotales dentro de una lista de datos. (1=PROMEDIO, 2=CUENTA, 3=CUENTAA, 4=MAX, 5=MIN,...9=SUMA, etc.) Consulte la referencia de subtotal en la ayuda de Excel Microsoft para obtener más detalles.

El formato en realidad dice como:
subtotalN:Ref donde Ref se refiere al grupo por columna.

Por ejemplo,

-  &=Productos.Unidades(subtotal9:Productos.ProductID) especifica la función de resumen en**Unidades** campo con respecto a la**Identificación de producto** campo en el**Productos** mesa.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) especifica la función de resumen en el**Col3** grupo de campo por**Col1** en la mesa**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) especifica la función de resumen en**columnaD** grupo de campo por**columnaA** y**columnaB** en la mesa**Tabla 1**.

Este ejemplo muestra algunos de los parámetros de agrupación en acción. Utiliza la base de datos de acceso Northwind.mdb Microsoft y extrae datos de la tabla denominada "Detalles del pedido". Creamos un archivo de diseñador llamado SmartMarker_Designer.xls en Microsoft Excel y colocamos marcadores inteligentes en varias celdas de las hojas de trabajo. Los marcadores se procesan para llenar las hojas de trabajo. Los datos se colocan y organizan por un campo de grupo.

El archivo del diseñador tiene dos hojas de trabajo. En el primero, colocamos marcadores inteligentes con parámetros de agrupación como se muestra en la captura de pantalla a continuación. Se colocan tres marcadores inteligentes (con parámetros de agrupación):
&=[Detalles del pedido].IDPedido(grupo:combinar,saltar:1),
&=[Detalles del pedido].Cantidad(subtotal9:Detalles del pedido.ID del pedido), y
&=[Detalles del pedido].PrecioUnitario(subtotal9:Detalles del pedido.ID del pedido) entre en A5, B5 y C5 respectivamente.

|**La primera hoja de trabajo en el archivo SmartMarker_Designer.xls, completa con marcadores inteligentes**|
|:- |
|![todo:imagen_alternativa_texto](using-smart-markers_5.png)|
En la segunda hoja de trabajo del archivo del diseñador, colocamos algunos marcadores inteligentes más, como se muestra en la figura a continuación. Colocamos los siguientes marcadores inteligentes:
&=[Detalles del pedido].IDPedido(grupo:normal),
&=[Detalles del pedido].Cantidad,
&=[Detalles del pedido].PrecioUnitario,
&=&=B(r)*C(r), y
&=subtotal9:Detalles del pedido.ID del pedido en A5, B5, C5, D5 y C6 respectivamente.

|**La segunda hoja de trabajo del archivo SmartMarker_Designer.xls, que muestra marcadores inteligentes mixtos.**|
|:- |
|![todo:imagen_alternativa_texto](using-smart-markers_6.png)|
Aquí está el código fuente utilizado en el ejemplo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Si necesita agregar sus propias etiquetas personalizadas a las filas de resumen o si desea concatenar el nombre del campo con una etiqueta, por ejemplo, "Subtotal de pedidos", Aspose.Cells le proporciona atributos de etiqueta y posición de etiqueta, por lo que puede colocar sus etiquetas personalizadas en Smart Marcadores al concatenar con las filas de Subtotal en datos de agrupación. Consulte el documento sobre cómo agregar etiquetas personalizadas para concatenar con las filas de subtotales en marcadores inteligentes para su referencia.

{{% /alert %}} 
## **Uso de tipos anónimos u objetos personalizados**
Aspose.Cells también admite tipos anónimos u objetos personalizados en marcadores inteligentes. El siguiente ejemplo muestra cómo funciona esto. Para importar datos de objetos dinámicos usando Smart Markers, visite el siguiente artículo:

[Importación desde un objeto dinámico como fuente de datos](/cells/es/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Marcadores de imagen**
Los marcadores inteligentes Aspose.Cells también admiten marcadores de imagen. Esta sección le muestra cómo insertar imágenes usando marcadores inteligentes.
### **Parámetros de imagen**
Parámetros de marcadores inteligentes para la gestión de imágenes.

- **Imagen:FitToCell** - Ajuste automático de la imagen a la altura de la fila y al ancho de la columna de la celda.
- **Imagen:EscalaN** - Escalar alto y ancho al N por ciento.
- **Imagen:Ancho:NinAltura:Nin** - Renderice la imagen N pulgadas de alto y N pulgadas de ancho. También puede especificar las posiciones Izquierda y Superior (en puntos).

Aquí está el código fuente utilizado en el ejemplo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Uso de objetos anidados**
Aspose.Cells admite objetos anidados en marcadores inteligentes, los objetos anidados deben ser simples. Usamos un archivo de plantilla simple. Consulte la hoja de cálculo del diseñador que contiene algunos marcadores inteligentes anidados.

|**La primera hoja de trabajo del archivo SM_NestedObjects.xlsx que muestra marcadores inteligentes anidados.**|
|:- |
|![todo:imagen_alternativa_texto](using-smart-markers_7.png)|
El ejemplo que sigue muestra cómo funciona esto.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Usar lista genérica como objeto anidado**
Aspose.Cells ahora también admite el uso de una lista genérica como un objeto anidado. Verifique la captura de pantalla del archivo de salida de Excel generado con el siguiente código. Como puede ver en la captura de pantalla, un objeto Profesor contiene varios objetos Estudiante anidados.

|![todo:imagen_alternativa_texto](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Uso de la propiedad HTML de marcadores inteligentes**
 El siguiente código de ejemplo explica el uso de la propiedad HTML de los marcadores inteligentes. Cuando se procese, mostrará "Mundo" en "Hello World" en negrita debido a HTML<b>etiqueta.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **No línea por línea**
 El método de procesamiento predeterminado actual es procesar smartmaker línea por línea. Pero a veces los marcadores inteligentes de la misma tabla de datos deben procesarse juntos, sin importar
si están en la misma fila o no, debe especificar un rango con nombre "_CellsSmartMarkers" y especificar WorkbookDesigner.LineByLine como falso antes de llamar al procesamiento.

|![todo:imagen_alternativa_texto](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Recibir notificaciones al fusionar datos con marcadores inteligentes**
veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el marcador inteligente en particular que se está procesando antes de la finalización. Esto se puede lograr usando la propiedad WorkbookDesigner.CallBack e ISmartMarkerCallBack

## **Temas avanzados**
- [Adición de objetos anónimos o personalizados en SmartMarkers](/cells/es/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Autocompletar datos de marcador inteligente en otras hojas de trabajo si los datos son demasiado grandes](/cells/es/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Dar formato a marcadores inteligentes](/cells/es/net/formatting-smart-markers/)
- [Recibir notificaciones al fusionar datos con marcadores inteligentes](/cells/es/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Establecer fuente de datos personalizada para WorkbookDesigner](/cells/es/net/set-custom-datasource-for-workbookdesigner/)
- [Mostrar el apóstrofo inicial en las celdas](/cells/es/net/show-leading-apostrophe-in-cells/)
- [Uso del parámetro Fórmula en el campo Marcador inteligente](/cells/es/net/using-formula-parameter-in-smart-marker-field/)
- [Uso de marcadores de imagen al agrupar datos en marcadores inteligentes](/cells/es/net/using-image-markers-while-grouping-data-in-smart-markers/)


