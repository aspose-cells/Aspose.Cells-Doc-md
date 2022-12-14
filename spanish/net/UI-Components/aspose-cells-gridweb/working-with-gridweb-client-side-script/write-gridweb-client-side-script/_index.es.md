---
title: Escribir secuencia de comandos del lado del cliente de GridWeb
type: docs
weight: 10
url: /es/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

Los desarrolladores pueden escribir secuencias de comandos del lado del cliente para el control Aspose.Cells.GridWeb. Esto significa que es posible invocar una función JavaScript del lado del cliente para realizar una tarea específica relacionada con el control GridWeb. Por ejemplo, los desarrolladores pueden escribir funciones de JavaScript para enviar datos de GridWeb a un servidor o mostrar un mensaje de alerta cuando ocurre un error de validación, etc.

Este tema explica esta característica con la ayuda de ejemplos.

{{% /alert %}} 
## **Escritura de secuencias de comandos del lado del cliente para Aspose.Cells.GridWeb**
### **Información básica**
Aspose.Cells.GridWeb proporciona dos propiedades creadas específicamente para admitir scripts del lado del cliente:

- OnSubmitClientFunctionOnSubmitClientFunction
- OnValidationErrorClientFunction

Cree funciones JavaScript en una página ASPX y asigne los nombres de estas funciones a las propiedades OnSubmitClientFunction y OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

La función de JavaScript que se asignará a la propiedad OnSubmitClientFunction debe definirse correctamente como se muestra a continuación:

**JavaScript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

donde el parámetro [arg] representa el comando generado por el control. El comando puede ser "Guardar", "Enviar", "Deshacer", etc. y el parámetro [cancelarEditar] es un valor booleano, que indica si la entrada del usuario se cancela o no.

Cualquier función de JavaScript asignada a la propiedad OnSubmitClientFunction es llamada cada vez por el control GridWeb antes de enviar datos de GridWeb a un servidor. De manera similar, si se asigna una función a la propiedad OnValidationErrorClientFunction, esa función se invocará cada vez que ocurra un error de validación.

{{% /alert %}} 
### **Funciones para secuencias de comandos del lado del cliente**
Aspose.Cells.GridWeb también expone funciones especialmente para secuencias de comandos del lado del cliente. Estas funciones se pueden usar dentro de las funciones de JavaScript para obtener más control de Aspose.Cells.GridWeb. Estas funciones del lado del cliente incluyen lo siguiente:

|**Funciones**|**Descripción**|
|:- |:- |
|updateData(bool cancelarEditar)|Actualiza todos los datos del cliente de Aspose.Cells.GridWeb antes de publicarlo en el servidor. Si el parámetro cancelEdit es verdadero, GridWeb descarta todas las entradas del usuario.|
|validarTodo()|Se utiliza para verificar si hay algún error de validación en la entrada del usuario. Si hay un error, la función devuelve falso, de lo contrario, verdadero.|
|enviar (cadena arg, bool cancelarEditar)|Llame a esta función para devolver o enviar datos al servidor. Esta función realiza ambas tareas, actualizar datos y validar la entrada del usuario. Esta función también puede disparar un evento de comando en el lado del servidor. Use el parámetro arg para pasar su comando. Por ejemplo: el comando GUARDAR se utiliza para hacer clic en el**Ahorrar** en la barra de comandos del control GridWeb y el comando CCMD:MYCOMMAND activa un evento CustomCommand.|
|setActiveCell(fila int, columna int)|Se utiliza para activar una celda específica.|
|setCellValue(fila int, columna int, valor de cadena)|Se usa para poner un valor a cualquier celda especificada usando sus números de fila y columna.|
|getCellValue(fila int, columna int)|Devuelve el valor de cualquier celda especificada.|
|obtenerFilaActiva()|Se usa junto con la función getActiveColumn() para determinar la posición de una celda activa.|
|getActiveColumn()|Se usa junto con la función getActiveRow() para determinar la posición de una celda activa.|
|getSelectRange()|Devuelve el último rango seleccionado.|
|establecerSeleccionarRango()|Selecciona el rango dado.|
|borrar selecciones ()|Borra toda la selección excepto la celda activa actual.|
|getCellsArray()| Se usa con otras funciones relacionadas como getCellName(), getCellValueByCell(), getCellRow() y getCellColumn(). Lea este artículo para obtener más información sobre el uso de esta función:[Lea los valores de las celdas de GridWeb en el lado del cliente](/cells/es/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
Para crear una aplicación de prueba que contenga scripts del lado del cliente que funcionen con Aspose.Cells.GridWeb, siga los pasos a continuación:

1. Cree funciones JavaScript para ser invocadas por GridWeb.
 Estas funciones se agregarán a la página ASP.NET<script></script>etiqueta.
1. Asigne los nombres de las funciones a las propiedades OnSubmitClientFunction y OnValidationErrorClientFunction.

El resultado del ejemplo de código se muestra a continuación:

**Una validación agregada a la celda C1** 

![todo:imagen_alternativa_texto](write-gridweb-client-side-script_1.png)

 Agregue un valor no válido y haga clic en**Ahorrar**. Se produce un error de validación y se ejecuta ValidationErrorFunction.

**ValidationErrorFunction invocada en el error de validación** 

![todo:imagen_alternativa_texto](write-gridweb-client-side-script_2.png)

 Hasta que ingrese un valor válido, no se envía ningún dato al servidor. Introduzca un valor válido y haga clic en**Ahorrar**. Se ejecuta ConfirmFunction.

**ConfirmFunction invocada antes de enviar datos de GridWeb al servidor** 

![todo:imagen_alternativa_texto](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
