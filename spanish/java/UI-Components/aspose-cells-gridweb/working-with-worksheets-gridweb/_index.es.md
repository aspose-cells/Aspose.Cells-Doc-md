---
title: Trabajando con hojas de cálculo de GridWeb
type: docs
weight: 30
url: /es/java/working-with-worksheets-gridweb/
---

## **Accediendo a hojas de cálculo**

Este tema trata sobre cómo acceder a las hojas de cálculo del control GridWeb. También podemos llamar a estas hojas de cálculo hojas de trabajo web porque pertenecen a GridWeb y se utilizan en aplicaciones web.

Todas las hojas de cálculo contenidas en el control GridWeb se almacenan en una GridWorksheetCollection del control GridWeb. Es sencillo acceder a una hoja de cálculo en particular mediante su índice de hoja.

Los desarrolladores pueden acceder a una hoja de cálculo específica al especificar su índice de hoja como se muestra a continuación en el fragmento de código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Eliminación de una hoja de cálculo**

Este tema proporciona información breve sobre cómo eliminar hojas de cálculo de archivos de Microsoft Excel utilizando la API de GridWeb. Elimine una hoja de cálculo especificando su índice de hoja.

Los desarrolladores pueden eliminar una hoja de cálculo específica al especificar su índice de hoja utilizando el método removeAt de la colección GridWorksheetCollection como se muestra a continuación en el fragmento de código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Agregar hojas de cálculo**

Las hojas de cálculo son una parte integral de GridWeb. Todos los datos se gestionan y almacenan en forma de hojas de cálculo. GridWeb permite a los desarrolladores añadir una o más hojas de cálculo al control Aspose.Cells.GridWeb. Este tema muestra enfoques simples para agregar hojas de cálculo a GridWeb.

### **Sin especificar nombre de hoja**

La forma más sencilla de agregar una hoja de cálculo a Aspose.Cells.GridWeb es llamar al método add de la clase GridWorksheetCollection en el control GridWeb. Esto crea hojas de cálculo que utilizan nombres predeterminados (es decir, Hoja1, Hoja2, Hoja3, etc.) y las añade al control GridWeb.

**Salida: se ha añadido una hoja de cálculo con nombre predeterminado a GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Con nombre de hoja especificado**

Para agregar una hoja de cálculo con un nombre específico al control GridWeb en lugar de usar el esquema de nombres predeterminado, llame a una versión sobrecargada del método add que toma el nombre de hoja especificado. Por ejemplo, el siguiente ejemplo agrega una hoja de cálculo llamada Factura.

**Salida: se ha añadido una hoja de cálculo con un nombre especificado a GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

El método add() devuelve el índice de la nueva hoja de cálculo que se puede utilizar para acceder a la instancia de esta hoja de cálculo. Para obtener más detalles sobre cómo acceder a hojas de cálculo, lea [Acceso a las hojas de cálculo](/cells/es/java/trabajar-con-hojas-de-cálculo-gridweb/#trabajarconhojasdecálculogridweb-accesoa...

{{% /alert %}}

## **Cambiar el nombre de una hoja de cálculo**

Cambiar el nombre de una hoja de cálculo puede ser muy útil al trabajar con muchas hojas de cálculo en GridWeb y decidir cambiar sus nombres para hacerlos más significativos. Por ejemplo, una hoja de cálculo que contiene una factura se puede renombrar como Factura en lugar de Hoja1. Este tema describe esta característica simple pero útil.

### **Cambiar el nombre de una hoja de cálculo**

Todas las hojas de cálculo contienen una propiedad Nombre que permite a los desarrolladores acceder o modificar los nombres de las hojas de cálculo. Para cambiar el nombre de una hoja de cálculo:

1. Acceda a una hoja de cálculo desde GridWorksheetCollection.
1. Cambiar el nombre de la hoja de cálculo seleccionada.

{{% alert color="primary" %}}

Para obtener más detalles sobre cómo acceder a las hojas de cálculo en Aspose.Cells.GridWeb, consulte [Acceso a hojas de cálculo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Antes de ejecutar el código, la hoja de cálculo tiene un nombre predeterminado, como Sheet1.

**Archivo de entrada: una hoja de cálculo con el nombre predeterminado Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Después de ejecutar el código, la hoja de cálculo se renombra como Invoice.

**Salida: la hoja de cálculo se renombra como Invoice** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Copiando una hoja de cálculo**

[Agregar hojas de cálculo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets) describe cómo agregar nuevas hojas de cálculo a GridWeb. También es posible agregar una copia (o réplica) de otra hoja de cálculo al control Aspose.Cells.GridWeb. Esta función puede ser útil cuando se requieren datos idénticos o similares en una hoja de cálculo y otra. En ese caso, es más fácil copiar una hoja de cálculo existente y agregarla a Aspose.Cells.GridWeb como una nueva hoja de cálculo en lugar de crearla desde cero.

### **Usando el índice de hoja**

El código de ejemplo a continuación muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el índice de la hoja de cálculo en el método addCopy de GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Usando el nombre de la hoja**
El código de ejemplo a continuación muestra cómo agregar una copia de una hoja de cálculo al control GridWeb especificando el nombre de la hoja de cálculo en el método addCopy de GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

El método addCopy devuelve el índice de la hoja de cálculo recién agregada que se puede usar para acceder a la instancia de la hoja de cálculo. Para obtener más detalles sobre cómo acceder a las hojas de cálculo, lea [Acceso a hojas de cálculo](/cells/es/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Trabajando con rangos nombrados**

Normalmente, las etiquetas de columna y fila se utilizan para hacer referencia de forma única a las celdas. Pero se pueden crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes.

La palabra **nombre** puede referirse a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Por ejemplo, use nombres fáciles de entender, como Productos, para referirse a rangos difíciles de entender, como Ventas!C20:C30.

Las etiquetas se pueden utilizar en fórmulas que hacen referencia a datos en la misma hoja de cálculo; si desea representar un rango en otra hoja de cálculo, puede usar un nombre. **Los rangos nombrados** es una de las características más potentes de Microsoft Excel.

Los usuarios pueden asignar un nombre a un rango y usar ese nombre en fórmulas. Aspose.Cells.GridWeb admite esta función.

### **Agregar/Hacer referencia a los rangos con nombre en las fórmulas**

El control GridWeb proporciona dos clases (GridName y GridNameCollection) para trabajar con rangos nombrados.

El siguiente fragmento de código te ayudará a comprender cómo usarlos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Gestión de Comentarios en la Hoja de Cálculo**

Este tema trata sobre cómo agregar, acceder y eliminar comentarios de las hojas de cálculo. Los comentarios son útiles para agregar notas o información útil para los usuarios que trabajarán con la hoja. Los desarrolladores tienen la flexibilidad de agregar comentarios a cualquier celda de la hoja de cálculo.

### **Trabajando con Comentarios**

#### **Añadir Comentarios**

Para agregar un comentario a la hoja de cálculo, por favor sigue los siguientes pasos:

1. Agrega el control Aspose.Cells.GridWeb al Formulario Web.
1. Accede a la hoja de cálculo a la que estás agregando comentarios.
1. Agregar un comentario a una celda.
1. Establece una nota para el nuevo comentario.

**Se ha agregado un comentario a la hoja de cálculo** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Acceso a Comentarios**

Para acceder a un comentario:

1. Accede a la celda que contiene el comentario.
1. Obten la referencia de la celda.
1. Pasa la referencia a la colección de Comentarios para acceder al comentario.
1. Ahora es posible modificar las propiedades del comentario.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Eliminación de Comentarios**

Para eliminar un comentario:

1. Accede a la celda como se explicó anteriormente.
1. Utilice el método removeAt de la colección de comentarios para eliminar el comentario.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Gestionar hipervínculos en la hoja de cálculo**

Este tema discute qué tipos de hipervínculos son admitidos en Aspose.Cells.GridWeb y cómo gestionarlos programáticamente. Los hipervínculos se pueden utilizar para crear enlaces a URL web o para realizar una devolución de llamada a un servidor.

### **Tipos de hipervínculos**

Los siguientes hipervínculos son admitidos por Aspose.Cells.GridWeb:

- Hipervínculos de URL de texto, hipervínculos de URL aplicados al texto.
- Hipervínculos de URL de imagen, hipervínculos de URL aplicados a imágenes.

#### **Hipervínculos de URL de texto**

El siguiente ejemplo agrega dos hipervínculos a una hoja de cálculo. Uno tiene un objetivo _blank mientras que el otro está definido como _parent.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Resultado: hipervínculos de texto agregados a la hoja de cálculo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Hipervínculos de URL de imagen**

El siguiente ejemplo agrega un hipervínculo de URL de imagen a una hoja de cálculo.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Resultado: hipervínculo de imagen agregado a la hoja de cálculo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Ordenar datos**

Ordenar es una característica muy valiosa cuando se trata de procesamiento de datos. Los datos no ordenados son una molestia para los usuarios al buscar información específica. Aspose.Cells.GridWeb soporta potentes características de ordenación. Este tema discute la ordenación de datos usando la API de Aspose.Cells.GridWeb.

Aspose.Cells.GridWeb permite a los desarrolladores ordenar datos horizontal y verticalmente para que puedan ordenar datos de arriba abajo o de izquierda a derecha.

### **De arriba abajo**

Para ordenar datos de orientación de arriba abajo:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Accede a la hoja de cálculo que deseas ordenar.
1. Ordena el rango de datos en cualquier orden (ascendente o descendente). Asegúrate de seleccionar la orientación de arriba hacia abajo.

El ejemplo a continuación ordena los datos en dos columnas (ID de Estudiante y Nombre de Estudiante) de una hoja de cálculo en orden ascendente. Solo se ordenan doce filas de dos columnas en la orientación de arriba hacia abajo.

Antes de aplicar el código, la hoja de cálculo contiene datos desordenados.

**Entrada: datos no ordenados** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

**Salida: datos ordenados de arriba hacia abajo en orden ascendente** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **De Izquierda a Derecha**

Para ordenar los datos de izquierda a derecha:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Accede a la hoja de cálculo que deseas ordenar.
1. Ordena el rango de datos en cualquier orden (ascendente o descendente). Asegúrate de seleccionar de izquierda a derecha.

El ejemplo a continuación ordena datos en dos filas (ID de Estudiante y Nombre de Estudiante) en orden ascendente. Solo se ordenan dos filas de cuatro columnas de izquierda a derecha.

Antes de aplicar el código, la hoja de cálculo contiene datos desordenados.

**Entrada: datos no ordenados antes de ejecutar el fragmento de código** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

**Salida: datos ordenados de izquierda a derecha en orden ascendente** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Búsqueda y Reemplazo**

Una de las formas más rápidas de realizar cambios repetitivos en una hoja de cálculo grande es utilizar la función de buscar y reemplazar. Encontrar te ayuda a localizar una cadena de texto o datos y reemplazarla por un nuevo valor. Aspose.Cells.GridWeb proporciona esta función. Te permite buscar y reemplazar una cadena de texto específica o un valor en la hoja de cálculo del lado del cliente a través de un diálogo sencillo. Incluso te permite buscar datos parciales.

### **Diálogo de Buscar/Reemplazar**

Hay dos formas de abrir el diálogo de Buscar/Reemplazar:

1. Cuando el control está activo, presiona **CTRL+F** para abrir el diálogo, o presiona la tecla **CTRL+R** para abrir el diálogo con el botón **Reemplazar** habilitado.
1. Mueve el cursor al área de la celda en la hoja de cálculo, luego haz clic derecho. Selecciona **Buscar** o **Reemplazar** en el menú.

**Seleccionar Buscar**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

Se muestra un cuadro de diálogo de buscar y reemplazar.

**El cuadro de diálogo Buscar/Reemplazar**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Usar Buscar**

Para buscar:

1. Abrir el cuadro de diálogo Buscar/Reemplazar.
1. Escribe la cadena que deseas buscar en el campo Buscar.
1. Haz clic en Buscar siguiente para buscar.

Se resalta la siguiente celda que coincide con tu condición de búsqueda.

{{% alert color="primary" %}}

Si tu criterio de búsqueda no se encuentra, se muestra un cuadro de diálogo para informarte.

{{% /alert %}}

### **Opciones de búsqueda**

Hay algunas opciones de búsqueda que puedes personalizar en el cuadro de diálogo. La tabla a continuación las enumera.

|**No.**|**Nombre de la opción**|**Descripción**|
| :- | :- | :- |
|1|Coincidir mayúsculas y minúsculas|Indica si se debe usar sensibilidad a mayúsculas y minúsculas en la búsqueda.|
|2|Coincidir palabra completa|Indica si se debe coincidir con toda la palabra en la búsqueda.|
|3|Buscar hacia arriba|Indica si la búsqueda se hará de abajo hacia arriba.|
|4|Expresión regular|Cuando está marcada, el control tratará la cadena en el cuadro de texto Buscar como una expresión regular en el proceso de búsqueda.|
|5|Buscar en Fórmulas/Valores|Cuando se selecciona Fórmulas, el control coincidirá con la fórmula o el valor sin formato de las celdas si la fórmula o el valor sin formato están presentes. Cuando se selecciona Valores, el control solo coincidirá con el valor mostrado de las celdas.|

### **Usando Reemplazar**

Para reemplazar texto o valores:

1. Abra el cuadro de diálogo Buscar/Reemplazar presionando **CTRL+F**, o seleccione hacer clic con el botón derecho en una celda y luego seleccione **Buscar** antes de hacer clic en **Reemplazar**.
1. Escriba la cadena de reemplazo en el campo **Reemplazar con**.
1. Haga clic en **Reemplazar**.

Para reemplazar texto:

1. Abra el cuadro de diálogo.
1. Ingrese el texto que desea encontrar en el campo **Buscar qué**, y el texto que desea reemplazar en el campo **Reemplazar con**.
1. Reemplace una ocurrencia a la vez haciendo clic en **Buscar siguiente** seguido de **Reemplazar**.
1. Si está seguro de lo que contiene la hoja de cálculo, haga clic en **Reemplazar todo**.

{{% alert color="primary" %}}

Si la hoja de cálculo no está en modo de edición, el botón **Reemplazar** no se muestra.

{{% /alert %}}

## Agregar/Quitar hipervínculos desde el lado del cliente

Aspose.Cells GridWeb ahora admite agregar y eliminar hipervínculos desde el lado del cliente. Para esto, la API proporciona las funciones "addCelllink" y "delCelllink". Los siguientes fragmentos de código demuestran cómo agregar y quitar hipervínculos desde el lado del cliente en GridWeb.

### Código de Ejemplo

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

También puede vincular a la hoja mediante el siguiente fragmento de código.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Actualizar la configuración de fuente desde el lado del cliente

Aspose.Cells GridWeb ahora admite cambiar la configuración de fuente desde el lado del cliente. Para esto, la API proporciona las siguientes funciones

- **updateCellFontStyle**: Parámetros - r/i/n/negrita/cursiva&&negrita
- **updateCellFontSize**: Parámetros - nombreFuente, etc. 'System'
- **updateCellFontName**: Parámetros - tamañofuente, etc. '12pt'
- **updateCellFontColor**: Parámetros - ninguno/u/l/ul/ para ninguno/subrayado/tachado/subrayado y tachado
- **updateCellFontLine**: Parámetros - color html como #aa22ee o nombre de color conocido como verde, rojo,...
- **updateCellBackGroundColor**: Parámetros - color html como #aa22ee o nombre de color conocido como verde, rojo,...

El siguiente fragmento de código demuestra el cambio de la configuración de fuente desde el lado del cliente en GridWeb.

### Código de Ejemplo

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Agregar/Quitar comentarios desde el lado del cliente

Ahora Aspose.Cells GridWeb admite agregar y quitar comentarios desde el lado del cliente. Para esto, la API proporciona las funciones "addcomments" y "delcomments". El siguiente fragmento de código demuestra cómo agregar y quitar comentarios desde el lado del cliente en GridWeb.

### Código de Ejemplo

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Mostrar botones para Agregar/Quitar Hojas de cálculo

Ahora Aspose.Cells GridWeb admite agregar y quitar hojas de cálculo mediante botones en la barra de herramientas. Para que los botones sean visibles en el frontend, es necesario establecer **GridWeb1.ShowAddButton** a **true**. El siguiente fragmento de código demuestra cómo agregar botones de agregar/quitar a la barra de herramientas de GridWeb.

### Código de Ejemplo

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
