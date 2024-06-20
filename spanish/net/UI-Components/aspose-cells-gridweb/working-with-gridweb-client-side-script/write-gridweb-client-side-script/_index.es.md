---
title: Escribir script del lado del cliente de GridWeb
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Este artículo introduce cómo trabajar con APIs de JS cliente en GridWeb.
---

{{% alert color="primary" %}} 

Los desarrolladores pueden escribir scripts del lado del cliente para el control Aspose.Cells.GridWeb. Esto significa que es posible invocar una función de JavaScript del lado del cliente para realizar una tarea específica relacionada con el control GridWeb. Por ejemplo, los desarrolladores pueden escribir funciones de JavaScript para enviar datos de GridWeb a un servidor o mostrar un mensaje de alerta cuando ocurre un error de validación, etc.

Este tema explica esta característica con la ayuda de ejemplos.

{{% /alert %}} 
## **Escribir scripts del lado del cliente para Aspose.Cells.GridWeb**
### **Información básica**
Aspose.Cells.GridWeb proporciona dos propiedades creadas específicamente para admitir scripts del lado del cliente:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Cree funciones JavaScript en una página ASPX y asígneles los nombres de estas funciones a las propiedades OnSubmitClientFunction y OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

La función JavaScript asignada a la propiedad OnSubmitClientFunction debe definirse correctamente como se muestra a continuación:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

donde el parámetro [arg] representa el comando generado por el control. El comando puede ser "Guardar", "Enviar", "Deshacer", etc., y el parámetro [cancelEdit] es un valor booleano, que indica si se cancela o no la entrada del usuario.

Cualquier función JavaScript asignada a la propiedad OnSubmitClientFunction se llama cada vez por el control GridWeb antes de enviar los datos de GridWeb a un servidor. De manera similar, si se asigna una función a la propiedad OnValidationErrorClientFunction, entonces esa función se invocará cada vez que ocurra un error de validación.

{{% /alert %}} 
### **Funciones para la escritura de scripts del lado del cliente**
Aspose.Cells.GridWeb también expone funciones especialmente para la escritura de scripts del lado del cliente. Estas funciones se pueden usar dentro de las funciones JavaScript para obtener un mayor control de Aspose.Cells.GridWeb. Estas funciones del lado del cliente incluyen las siguientes:

|**Funciones**|**Descripción**|
| :- | :- |
|updateData(bool cancelEdit)|Actualiza todos los datos del lado del cliente de Aspose.Cells.GridWeb antes de enviarlos al servidor. Si el parámetro cancelEdit es true, entonces GridWeb descarta toda la entrada del usuario.|
|validateAll()|Se utiliza para verificar si hay errores de validación en la entrada del usuario. Si hay un error, la función devuelve falso, de lo contrario verdadero.|
|submit(string arg, bool cancelEdit)|Llama a esta función para enviar datos al servidor. Esta función realiza ambas tareas, es decir, actualiza los datos y valida la entrada del usuario. Esta función también puede activar un evento de comando en el lado del servidor. Utilice el parámetro arg para pasar su comando. Por ejemplo: el comando SAVE se usa para hacer clic en el botón **Guardar** en la barra de comandos del control GridWeb y el comando CCMD:MYCOMMAND dispara un evento CustomCommand.|
|setActiveCell(int row, int column)|Se utiliza para activar una celda específica.|
|setCellValue(int row, int column, string value)|Se utiliza para poner un valor en cualquier celda especificada mediante sus números de fila y columna.|
|getCellValue(int row, int column)|Devuelve el valor de cualquier celda especificada.|
|getActiveRow()|Se utiliza en conjunto con la función getActiveColumn() para determinar la posición de una celda activa.|
|getActiveColumn()|Se utiliza en conjunto con la función getActiveRow() para determinar la posición de una celda activa.|
|getSelectRange()|Devuelve el último rango seleccionado.|
|setSelectRange()|Selecciona el rango dado.|
|clearSelections()|Borra toda la selección excluyendo la celda activa actual.|
|getCellsArray()|Se utiliza con otras funciones relacionadas como getCellName(), getCellValueByCell(), getCellRow() y getCellColumn(). Por favor, lea este artículo para obtener más información sobre el uso de esta función: [Leer los valores de las celdas de GridWeb en el lado del cliente](/cells/es/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Para crear una aplicación de prueba que contenga scripts del lado del cliente que funcionen con Aspose.Cells.GridWeb, siga los siguientes pasos:

1. Cree funciones JavaScript que serán invocadas por GridWeb.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. Asigne los nombres de las funciones a las propiedades OnSubmitClientFunction y OnValidationErrorClientFunction.

El resultado del ejemplo de código se muestra a continuación:

**Una validación agregada a la celda C1** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Agregue un valor no válido y haga clic en **Guardar**. Ocurre un error de validación y se ejecuta la función ValidationErrorFunction.

**ValidationErrorFunction invocado en caso de error de validación** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Hasta que ingrese un valor válido, no se enviarán datos al servidor. Ingrese un valor válido y haga clic en **Guardar**. Se ejecuta la ConfirmFunction.

**Se ha invocado la función ConfirmFunction antes de enviar los datos de GridWeb al servidor** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
