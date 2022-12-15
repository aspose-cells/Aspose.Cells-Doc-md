---
title: Trabajar con eventos de GridWeb
type: docs
weight: 70
url: /es/net/working-with-gridweb-events/
---
{{% alert color="primary" %}} 

Todos los programadores deben estar familiarizados con los eventos y su propósito. Los eventos se utilizan para enviar notificaciones de cambios que pueden ocurrir en un control o clase. Aspose.Cells.GridWeb tiene varios eventos que pueden usarse para realizar tareas específicas cuando ocurren ciertos cambios en el control.

Este tema proporciona una introducción a todos los eventos admitidos por el control Aspose.Cells.GridWeb junto con algunos detalles sobre cómo manejar estos eventos.

{{% /alert %}} 
## **Trabajar con eventos de cuadrícula**
### **Introducción a los eventos de cuadrícula**
Aspose.Cells. El control GridWeb admite varios eventos que brindan más control para realizar operaciones cuando se activan eventos específicos en el control. Una lista completa de eventos compatibles con Aspose.Cells. El control GridWeb se puede encontrar a continuación.

{{% alert color="primary" %}} 

Esta lista no incluye eventos heredados por Aspose.Cells.GridWeb de la clase Control.

{{% /alert %}} 

|**Eventos** |**Descripción** |
|:- |:- |
| Comando celular| Ocurre cuando se hace clic en el hipervínculo de comando de una celda. Cuando se activa este evento, su parámetro e.Argument proporciona el nombre del comando.|
| CellDoubleClick| Ocurre cuando se hace doble clic en la celda.|
| error de celda| Ocurre cuando el valor de entrada de una celda tiene algún error.|
| Columna Eliminada|Ocurre cuando un usuario elimina una columna de una hoja de trabajo usando el menú del lado del cliente.|
| Columna Eliminación| Ocurre cuando un usuario intenta eliminar una columna de una hoja de trabajo usando el menú del lado del cliente.|
| ColumnDoubleClick| Ocurre cuando se hace doble clic en el encabezado de la columna.|
| Columna Insertada| Ocurre cuando un usuario inserta una columna en la hoja de trabajo usando el menú del lado del cliente.|
| Comando personalizado| Ocurre cuando un usuario hace clic en un botón de comando personalizado.|
| Cargar datos personalizados| Ocurre cuando la propiedad EnableSession del control se establece en false y necesita cargar datos de la hoja de cálculo. Puede manejar este evento en modo sin sesión para cargar datos de hojas de cálculo desde un archivo o una base de datos.|
| PageIndexChanged| Se produce cuando se cambia el índice de página de la hoja del control.|
| FilaEliminada| Ocurre cuando un usuario elimina una fila de una hoja de trabajo usando el menú del lado del cliente.|
| FilaEliminación| Ocurre cuando un usuario intenta eliminar una fila de una hoja de trabajo usando el menú del lado del cliente.|
| FilaDobleClic|Ocurre cuando se hace doble clic en el encabezado de la fila.|
| FilaInsertado| Ocurre cuando un usuario inserta una fila en la hoja de trabajo usando el menú del lado del cliente.|
| GuardarComando| Ocurre cuando el**Ahorrar** se hace clic en el botón.|
| SheetDataUpdated| Ocurre cuando el control cargó los datos publicados y actualizó los datos de la hoja de trabajo.|
| FichaHojaClic| Ocurre cuando se hace clic en la pestaña de una hoja.|
| EnviarComando| Ocurre cuando el**Enviar** se hace clic en el botón.|
| DeshacerComando| Ocurre cuando el**Deshacer** se hace clic en el botón.|
| AjaxCallFinalizado| Se dispara cuando finaliza la actualización AJAX del control. (el EnableAJAX se establecerá en verdadero).|
| CellModifiedOnAjax| Se dispara cuando la celda se modifica en la llamada AJAX.|
| OnAfterColumnFilter| Se activa después de que el filtro se haya aplicado en una columna.|
| OnBeforeColumnFilter| Se activa antes de que se aplique el filtro en una columna.|
## **Manejo de eventos de cuadrícula**
Para realizar una operación específica al desencadenar un evento específico, debemos crear un controlador de eventos. Un controlador de eventos realiza la tarea deseada cuando se activa un determinado evento. Los pasos ilustrados a continuación muestran cómo manejar un evento de cuadrícula simple usando Visual Studio.
### **Paso 1: Selección de un evento de Aspose.Cells. GridWeb Control**
1. Seleccione el control Aspose.Cells.GridWeb y abra su cuadro de diálogo Propiedades en el lado derecho.
1.  Haga clic en el**Pestaña Eventos** botón.
1. Seleccione un evento.
 Para este ejemplo, se selecciona el evento SaveCommand.
### **Paso 2: crear un controlador de eventos**
1.  Haga doble clic en un evento en el cuadro de diálogo Propiedades.

   **Hacer doble clic en un evento seleccionado** 

![todo:imagen_alternativa_texto](working-with-gridweb-events_1.png)




 Cuando se hace doble clic en el evento, Visual Studio crea automáticamente un controlador de eventos.

**Un controlador de eventos creado por Visual Studio** 

![todo:imagen_alternativa_texto](working-with-gridweb-events_2.png)




1. Agregue código para realizar alguna acción dentro del controlador de eventos.

 Aquí, una sola línea de código que guarda el contenido de la cuadrícula en un archivo de Excel cuando el**Ahorrar** se ha hecho clic en el botón se ha añadido.

Para obtener más información, mueva el cursor arriba para ver algo de código y luego descubrirá que Visual Studio es lo suficientemente inteligente como para agregar un controlador de eventos al evento SaveCommand de GridWeb.
### **Paso 3: ejecutar su aplicación**
1. Generar y ejecutar la aplicación.
1.  Hacer clic**Ahorrar**.

 El contenido de la cuadrícula se guarda en un archivo de Excel.

**Aplicación en modo de ejecución** 

![todo:imagen_alternativa_texto](working-with-gridweb-events_3.png)
