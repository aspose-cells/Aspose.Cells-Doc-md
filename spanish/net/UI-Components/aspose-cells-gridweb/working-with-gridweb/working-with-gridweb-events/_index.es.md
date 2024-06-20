---
title: Trabajando con Eventos de GridWeb
type: docs
weight: 70
url: /es/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb,eventos,evento
description: Este artículo introduce cómo trabajar con tipos de eventos en GridWeb.
---

{{% alert color="primary" %}} 

Todos los programadores deben estar familiarizados con los eventos y su propósito. Los eventos se utilizan para enviar notificaciones de los cambios que pueden ocurrir en un control o clase. Aspose.Cells.GridWeb tiene varios eventos que se pueden utilizar para realizar tareas específicas cuando ocurren ciertos cambios en el control.

Este tema proporciona una introducción a todos los eventos admitidos por el control Aspose.Cells.GridWeb junto con algunos detalles sobre cómo manejar estos eventos.

{{% /alert %}} 
## **Trabajando con Eventos de Grid**
### **Introducción a los Eventos de la Rejilla**
El control Aspose.Cells.GridWeb admite varios eventos que proporcionan más control para realizar operaciones cuando se desencadenan eventos específicos en el control. Se puede encontrar una lista completa de eventos admitidos por el control Aspose.Cells.GridWeb a continuación.

{{% alert color="primary" %}} 

Esta lista no incluye eventos heredados por Aspose.Cells.GridWeb de la clase Control.

{{% /alert %}} 

|**Eventos** |**Descripción** |
| :- | :- |
|CellCommand |Ocurre cuando se hace clic en el hipervínculo de comando de una celda. Cuando se dispara este evento, su parámetro e.Argument proporciona el nombre del comando. |
|CellDoubleClick |Ocurre cuando se hace doble clic en la celda. |
|CellError |Ocurre cuando el valor de entrada de una celda tiene algún error. |
|ColumnDeleted |Ocurre cuando un usuario elimina una columna de una hoja de cálculo usando el menú del lado del cliente. |
|ColumnDeleting |Ocurre cuando un usuario intenta eliminar una columna de una hoja de cálculo usando el menú del lado del cliente. |
|ColumnDoubleClick |Ocurre cuando se hace doble clic en el encabezado de columna. |
|ColumnInserted |Ocurre cuando un usuario inserta una columna en la hoja de cálculo usando el menú del lado del cliente. |
|CustomCommand |Ocurre cuando un usuario hace clic en un botón de comando personalizado. |
|LoadCustomData |Ocurre cuando la propiedad EnableSession del control está establecida en false y es necesario cargar datos de la hoja de cálculo. Puede manejar este evento en modo sin sesión para cargar datos de la hoja de cálculo desde un archivo o una base de datos. |
|PageIndexChanged |Ocurre cuando se cambia el índice de la página de hoja del control. |
|RowDeleted |Ocurre cuando un usuario elimina una fila de una hoja de cálculo usando el menú del lado del cliente. |
|RowDeleting |Ocurre cuando un usuario intenta eliminar una fila de una hoja de cálculo usando el menú del lado del cliente. |
|RowDoubleClick |Ocurre cuando se hace doble clic en el encabezado de fila. |
|RowInserted |Ocurre cuando un usuario inserta una fila en la hoja de cálculo usando el menú del lado del cliente. |
|SaveCommand |Ocurre cuando se hace clic en el botón **Guardar**. |
|SheetDataUpdated |Ocurre cuando el control ha cargado los datos enviados y actualizado los datos de la hoja de cálculo.
|SheetTabClick |Ocurre cuando se hace clic en una pestaña de hoja.
|SubmitCommand |Ocurre cuando se hace clic en el botón **Enviar**. |
|UndoCommand |Ocurre cuando se hace clic en el botón **Deshacer**. |
|AjaxCallFinished |Se dispara cuando la actualización AJAX del control ha finalizado. (EnableAJAX debe estar configurado en true). |
|CellModifiedOnAjax |Se dispara cuando la celda se modifica en una llamada AJAX. |
|OnAfterColumnFilter |Se dispara después de aplicar el filtro a una columna. |
|OnBeforeColumnFilter |Se activa antes de que se aplique el filtro en una columna.
## **Manejo de Eventos de la Cuadrícula**
Para realizar una operación específica al activar un evento específico, tenemos que crear un controlador de eventos. Un controlador de eventos realiza la tarea deseada cuando se activa un cierto evento. Los pasos ilustrados a continuación muestran cómo manejar un evento de cuadrícula simple utilizando Visual Studio.
### **Paso 1: Seleccionar un evento del control Aspose.Cells.GridWeb**
1. Seleccione el control Aspose.Cells.GridWeb y abra su cuadro de diálogo Propiedades en el lado derecho.
1. Haga clic en el botón **Eventos**.
1. Seleccione un evento.
   Para este ejemplo, se selecciona el evento SaveCommand.
### **Paso 2: Crear un controlador de eventos**
1. Haga doble clic en un evento en el cuadro de diálogo Propiedades. 

   **Hacer doble clic en un evento seleccionado** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




Cuando se hace doble clic en el evento, Visual Studio crea automáticamente un controlador de eventos. 

**Un controlador de eventos creado por Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Agregue código para realizar alguna acción dentro del controlador de eventos.

Aquí, se ha agregado una sola línea de código que guarda el contenido de la cuadrícula en un archivo de Excel cuando se hace clic en el botón **Guardar**.

Para obtener más información, mueva el cursor arriba para ver algo de código y descubrirá que Visual Studio es lo suficientemente inteligente como para añadir un controlador de eventos al evento SaveCommand de GridWeb.
### **Paso 3: Ejecutar su aplicación**
1. Compile y ejecute la aplicación.
1. Haga clic en **Guardar**.

El contenido de la cuadrícula se guarda en un archivo de Excel. 

**Aplicación en modo de ejecución** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
