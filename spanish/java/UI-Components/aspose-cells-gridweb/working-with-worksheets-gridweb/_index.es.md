---
title: Trabajar con hojas de trabajo GridWeb
type: docs
weight: 30
url: /es/java/working-with-worksheets-gridweb/
---
## **Acceder a las hojas de trabajo**

Este tema trata sobre el acceso a las hojas de trabajo del control GridWeb. También podemos llamar a estas hojas de trabajo hojas de trabajo web porque pertenecen a GridWeb y se utilizan en aplicaciones web.

Todas las hojas de cálculo contenidas en el control GridWeb se almacenan en una GridWorksheetCollection del control GridWeb. Es fácil acceder a una hoja de trabajo en particular por su índice de hoja.

Los desarrolladores pueden acceder a una hoja de trabajo específica especificando su índice de hoja como se muestra a continuación en el fragmento de código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Quitar una hoja de trabajo**

Este tema proporciona información breve sobre cómo eliminar hojas de cálculo de archivos de Excel Microsoft mediante GridWeb API. Eliminar una hoja de cálculo especificando su índice de hoja.

Los desarrolladores pueden eliminar una hoja de trabajo específica especificando su índice de hoja mediante el método removeAt de la colección GridWorksheetCollection, como se muestra a continuación en el fragmento de código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Agregar hojas de trabajo**

Las hojas de trabajo son una parte integral de GridWeb. Todos los datos se gestionan y almacenan en forma de hojas de cálculo. GridWeb permite a los desarrolladores agregar una o más hojas de trabajo al control Aspose.Cells.GridWeb. Este tema muestra enfoques simples para agregar hojas de trabajo a GridWeb.

### **Sin especificar el nombre de la hoja**

La forma más sencilla de agregar una hoja de cálculo a Aspose.Cells.GridWeb es llamar al método de adición de la clase GridWorksheetCollection en el control GridWeb. Esto crea hojas de cálculo que usan nombres predeterminados (es decir, Hoja1, Hoja2, Hoja3, etc.) y las agrega al control GridWeb.

**Salida: se ha agregado una hoja de trabajo con un nombre predeterminado a GridWeb** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Con nombre de hoja especificado**

Para agregar una hoja de trabajo con un nombre específico al control GridWeb en lugar de usar el esquema de nombres predeterminado, llame a una versión sobrecargada del método add que toma la cadena SheetName especificada. Por ejemplo, el siguiente ejemplo agrega una hoja de cálculo llamada Factura.

**Salida: se ha agregado una hoja de trabajo con un nombre específico a GridWeb** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 El método add() devuelve el índice de la nueva hoja de trabajo que se puede usar para acceder a la instancia de esta hoja de trabajo. Para obtener más detalles sobre cómo acceder a las hojas de trabajo, lea[Acceder a las hojas de trabajo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Cambiar el nombre de una hoja de trabajo**

Cambiar el nombre de una hoja de trabajo puede ser muy útil cuando se trabaja con muchas hojas de trabajo en GridWeb y se decide cambiar sus nombres para que sean más significativas. Por ejemplo, se puede cambiar el nombre de una hoja de trabajo que contiene una factura a Factura en lugar de Hoja1. Este tema describe esta característica simple pero útil.

### **Cambiar el nombre de una hoja de trabajo**

Todas las hojas de trabajo contienen una propiedad Nombre que permite a los desarrolladores acceder o modificar los nombres de las hojas de trabajo. Para cambiar el nombre de una hoja de trabajo:

1. Acceda a una hoja de trabajo desde GridWorksheetCollection.
1. Cambiar el nombre de la hoja de cálculo seleccionada.

{{% alert color="primary" %}}

 Para obtener más detalles sobre cómo acceder a las hojas de trabajo en Aspose.Cells.GridWeb, consulte[Acceder a las hojas de trabajo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Antes de ejecutar el código, la hoja de cálculo tiene un nombre predeterminado, como Hoja1.

**Archivo de entrada: una hoja de trabajo con un nombre predeterminado Hoja1** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_3.png)

Después de ejecutar el código, la hoja de cálculo pasa a llamarse Factura.

**Salida: la hoja de cálculo pasa a llamarse Factura** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Copiar una hoja de trabajo**

[Agregar hojas de trabajo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)describe cómo agregar nuevas hojas de trabajo a GridWeb. También es posible agregar una copia (o réplica) de otra hoja de cálculo al control Aspose.Cells.GridWeb. Esta característica puede ser útil cuando también se requieren datos idénticos o similares en una hoja de trabajo en otra hoja de trabajo. Cuando ese es el caso, es más fácil copiar una hoja de trabajo existente y agregarla a Aspose.Cells.GridWeb como una nueva hoja de trabajo en lugar de crearla desde cero.

### **Uso del índice de hoja**

El siguiente código de ejemplo muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el índice de la hoja de cálculo en el método addCopy de GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Usando el nombre de la hoja**
El siguiente código de ejemplo muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el nombre de la hoja de cálculo en el método addCopy de GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 El método addCopy devuelve el índice de la hoja de trabajo recién agregada que se puede usar para acceder a la instancia de la hoja de trabajo. Para obtener más detalles sobre cómo acceder a las hojas de trabajo, lea[Acceder a las hojas de trabajo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Trabajar con rangos con nombre**

Normalmente, las etiquetas de columna y fila se utilizan para hacer referencia de forma única a las celdas. Pero puede crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes.

 La palabra**nombre** puede hacer referencia a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Por ejemplo, use nombres fáciles de entender, como Productos, para hacer referencia a rangos difíciles de entender, como Ventas!C20:C30.

 Las etiquetas se pueden usar en fórmulas que se refieren a datos en la misma hoja de trabajo; si desea representar un rango en otra hoja de trabajo, puede usar un nombre.**Rangos con nombre** es una de las características más poderosas de Microsoft Excel.

Los usuarios pueden asignar un nombre a un rango y usar ese nombre en fórmulas. Aspose.Cells. GridWeb admite esta función.

### **Agregar/Hacer referencia a rangos con nombre en fórmulas**

El control GridWeb proporciona dos clases (GridName y GridNameCollection) para trabajar con rangos con nombre.

El siguiente fragmento de código lo ayudará a comprender cómo usarlos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Gestión de comentarios en la hoja de trabajo**

Este tema trata sobre la adición, el acceso y la eliminación de comentarios de las hojas de trabajo. Los comentarios son útiles para agregar notas o información útil para los usuarios que trabajarán con la hoja. Los desarrolladores tienen la flexibilidad de agregar comentarios a cualquier celda de la hoja de trabajo.

### **Trabajar con comentarios**

#### **Adición de comentarios**

Para agregar un comentario a la hoja de trabajo, siga los pasos a continuación:

1. Agregue el control Aspose.Cells.GridWeb al formulario web.
1. Acceda a la hoja de trabajo a la que está agregando comentarios.
1. Agregar un comentario a una celda.
1. Establezca una nota para el nuevo comentario.

**Se ha añadido un comentario a la hoja de cálculo.** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Acceso a comentarios**

Para acceder a un comentario:

1. Accede a la celda que contiene el comentario.
1. Obtenga la referencia de la celda.
1. Pase la referencia a la colección de comentarios para acceder al comentario.
1. Ahora es posible modificar las propiedades del comentario.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Eliminar comentarios**

Para eliminar un comentario:

1. Acceda a la celda como se explicó anteriormente.
1. Utilice el método removeAt de la colección de comentarios para eliminar el comentario.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Administrar hipervínculos en la hoja de trabajo**

Este tema analiza qué tipos de hipervínculos se admiten en Aspose.Cells.GridWeb y cómo administrarlos mediante programación. Los hipervínculos se pueden usar para crear enlaces a direcciones URL web o para realizar una devolución de datos a un servidor.

### **Tipos de hipervínculos**

Los siguientes hipervínculos son compatibles con Aspose.Cells.GridWeb:

- Hipervínculos de URL de texto, hipervínculos de URL aplicados al texto.
- Hipervínculos de URL de imagen, hipervínculos de URL aplicados a imágenes.

#### **Hipervínculos de URL de texto**

 El siguiente ejemplo agrega dos hipervínculos a una hoja de trabajo. uno tiene un_ objetivo en blanco mientras que el otro está configurado para_padre.

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_6.png)

**Salida: hipervínculos de texto agregados a la hoja de trabajo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Hipervínculos de URL de imagen**

El siguiente ejemplo agrega un hipervínculo de URL de imagen a una hoja de trabajo.

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_7.png)

**Salida: hipervínculo de imagen agregado a la hoja de trabajo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Clasificación de datos**

La clasificación es una característica muy valiosa cuando se trata de procesamiento de datos. Los datos desordenados son una molestia para los usuarios cuando buscan información específica. Aspose.Cells.GridWeb admite potentes funciones de clasificación. Este tema trata sobre la clasificación de datos mediante Aspose.Cells.GridWeb API.

Aspose.Cells.GridWeb permite a los desarrolladores ordenar los datos horizontal y verticalmente para que los desarrolladores puedan ordenar los datos de arriba a abajo o de izquierda a derecha.

### **De arriba a abajo**

Para ordenar los datos de arriba a abajo:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Acceda a la hoja de trabajo que desea ordenar.
1. Ordene el rango de datos en cualquier orden (ascendente o descendente). Asegúrese de seleccionar la orientación de arriba hacia abajo.

El siguiente ejemplo ordena los datos en dos columnas (ID del estudiante y Nombre del estudiante) de una hoja de trabajo en orden ascendente. Solo doce filas de dos columnas se ordenan en la orientación de arriba a abajo.

Antes de aplicar el código, la hoja de trabajo contiene datos desordenados.

**Entrada: datos sin clasificar** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_8.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

**Salida: datos ordenados de arriba a abajo en orden ascendente** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **De izquierda a derecha**

Para ordenar los datos de izquierda a derecha:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Acceda a la hoja de trabajo que desea ordenar.
1. Ordene el rango de datos en cualquier orden (ascendente o descendente). Asegúrese de seleccionar de izquierda a derecha.

El siguiente ejemplo ordena los datos en dos filas (ID del estudiante y Nombre del estudiante) en orden ascendente. Solo se ordenan de izquierda a derecha dos filas de cuatro columnas.

Antes de aplicar el código, la hoja de trabajo contiene datos desordenados.

**Entrada: datos sin clasificar antes de ejecutar el fragmento de código** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_10.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

**Salida: datos ordenados de izquierda a derecha en orden ascendente** 

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Buscando y Reemplazando**

Una de las formas más rápidas de realizar cambios repetitivos en una hoja de cálculo grande es usar la función de buscar y reemplazar. Find lo ayuda a ubicar una cadena de texto o datos y replace los sustituye con un nuevo valor. Aspose.Cells. GridWeb proporciona esta característica. Le permite buscar y reemplazar con una cadena de texto o valor específico en el lado del cliente de la hoja de trabajo a través de un cuadro de diálogo simple. Incluso te permite buscar datos parciales.

### **El cuadro de diálogo Buscar/Reemplazar**

Hay dos formas de abrir el cuadro de diálogo Buscar/Reemplazar:

1.  Cuando el control esté activo, presione**CTRL+F** para abrir el cuadro de diálogo, o presione**CTRL+R** tecla para abrir el cuadro de diálogo con la**Reemplazar** botón habilitado.
1.  Mueva el cursor al área de la celda en la hoja de trabajo, luego haga clic con el botón derecho. Seleccione**Encontrar** o**Reemplazar** del menú.

**Seleccionando Buscar**

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_12.png)

Se muestra un cuadro de diálogo de buscar y reemplazar.

**El cuadro de diálogo Buscar/Reemplazar**

![todo:imagen_alternativa_texto](working-with-worksheets-gridweb_13.png)

**Uso de Buscar**

Buscar:

1. Abra el cuadro de diálogo Buscar/Reemplazar.
1. Escriba la cadena que desea buscar en el campo Buscar.
1. Haga clic en Buscar siguiente para buscar.

Se resalta la siguiente celda que coincide con su condición de búsqueda.

{{% alert color="primary" %}}

Si no se encuentra su criterio de búsqueda, se muestra un cuadro de diálogo para informarle.

{{% /alert %}}

### **Opciones de búsqueda**

Hay algunas opciones de búsqueda que puede personalizar en el cuadro de diálogo. La siguiente tabla los enumera.

|**No.**|**Nombre de la opción**|**Descripción**|
|:- |:- |:- |
|1|Caso de partido|Indica si se debe distinguir entre mayúsculas y minúsculas en la búsqueda.|
|2|Compare la palabra completa|Indica si se debe hacer coincidir la palabra completa en la búsqueda.|
|3|buscar|Indica si la búsqueda se realizará de abajo hacia arriba.|
|4|Expresión regular|Cuando está marcado, el control tratará la cadena en el cuadro de texto Buscar como una expresión regular en el proceso de búsqueda.|
|5|Buscar en fórmulas/valores|Cuando se selecciona Fórmulas, el control coincidirá con la fórmula o el valor sin formato de las celdas si la fórmula o el valor sin formato están presentes. Cuando se seleccionan los valores, el control solo coincidirá con el valor mostrado de las celdas.|

### **Usando Reemplazar**

Para reemplazar texto o valores:

1.  Abra el cuadro de diálogo Buscar/Reemplazar presionando**CTRL+F** , o seleccione haga clic con el botón derecho en una celda y seleccione**Encontrar** antes de hacer clic**Reemplazar**.
1.  Escriba la cadena de reemplazo en el**Reemplazar con**campo.
1.  Hacer clic**Reemplazar**.

Para reemplazar texto:

1. Abra el cuadro de diálogo.
1.  Introduzca el texto que desea buscar en el**Encontrar que** campo, y el texto que desea reemplazarlo dentro del**Reemplazar con** campo.
1.  Reemplace una aparición a la vez haciendo clic en**Buscar siguiente** seguido por**Reemplazar**.
1.  Si está muy seguro de lo que contiene la hoja de cálculo, haga clic en**Reemplaza todo**.

{{% alert color="primary" %}}

 Si la hoja de cálculo no está en modo de edición, el**Reemplazar** el botón no se muestra.

{{% /alert %}}

## Agregar/eliminar hipervínculos del lado del cliente

Aspose.Cells GridWeb ahora admite agregar y eliminar hipervínculos del lado del cliente. Para ello, el API proporciona las funciones "addCelllink" y "delCelllink". Los siguientes fragmentos de código muestran cómo agregar y eliminar hipervínculos del lado del cliente en GridWeb.

### Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

También puede vincular a la hoja usando el siguiente fragmento de código.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Actualizar la configuración de fuentes desde el lado del cliente

Aspose.Cells GridWeb ahora admite cambiar la configuración de fuente desde el lado del cliente. Para ello, el API proporciona las siguientes funciones

- **actualizarCellFontStyle**: Parámetros - r/i/b/ib para normal/cursiva/negrita/cursiva&&negrita
- **actualizarCellFontSize**: Params - nombre de fuente, etc. 'Sistema'
- **actualizarCellFontName**: Parámetros - tamaño de fuente, etc. '12 puntos'
- **actualizarCellFontColor**: Parámetros - ninguno/u/l/ul/ para ninguno/subrayado/tachado/subrayado&&tachado
- **actualizarCellFontLine**: Params - color html como #aa22ee o nombre de color conocido como verde, rojo,...
- **actualizarCellBackGroundColor**: Params - color html como #aa22ee o nombre de color conocido como verde, rojo,...

El siguiente fragmento de código muestra cómo cambiar la configuración de fuente desde el lado del cliente en GridWeb.

### Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Agregar/eliminar comentarios del lado del cliente

Aspose.Cells GridWeb ahora admite agregar y eliminar comentarios del lado del cliente. Para ello, el API proporciona las funciones "addcomments" y "delcomments". El siguiente fragmento de código muestra cómo agregar y quitar comentarios del lado del cliente en GridWeb.

### Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Mostrar botones para Agregar/Eliminar hojas de trabajo

 Aspose.Cells GridWeb ahora admite agregar y eliminar hojas mediante el uso de botones en la barra de herramientas. Para que los botones sean visibles en la interfaz, debe configurar**GridWeb1.ShowAddButton** a**verdadero**. El siguiente fragmento de código muestra cómo agregar botones Agregar o quitar a la barra de herramientas de GridWeb.

### Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
