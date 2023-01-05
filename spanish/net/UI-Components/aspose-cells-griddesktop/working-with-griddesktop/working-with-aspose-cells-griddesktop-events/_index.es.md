---
title: Trabajando con Aspose.Cells.GridDesktop Events
type: docs
weight: 30
url: /es/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

Los eventos se utilizan para enviar notificaciones cuando se produce un cambio en un control o clase. Aspose.Cells.GridDesktop tiene varios eventos que se utilizan para realizar tareas específicas cuando se producen ciertos cambios en el control. Este tema proporciona una introducción a todos los eventos compatibles con el control Aspose.Cells.GridDesktop y explica cómo manejar esos eventos.

{{% /alert %}} 
## **Introducción**
El control Aspose.Cells.GridDesktop admite varios eventos que brindan más control para realizar operaciones cuando se activan eventos específicos. A continuación se muestra una lista completa de eventos compatibles con el control Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

Esta lista no incluye los eventos heredados por Aspose.Cells.GridDesktop de la clase Control.

{{% /alert %}} 

|**Eventos**|**Descripción**|
|:- |:- |
|AntesCalcular|Ocurre antes de calcular la fórmula en el libro de trabajo.|
|Antes de Cargar Archivo|Ocurre antes de que el libro de trabajo se cargue desde el archivo.|
|ColumnHeaderClick|Ocurre cuando se hace clic en el encabezado de la columna.|
|ColumnHeaderDoubleClick|Ocurre cuando se hace doble clic en el encabezado de la columna.|
|CellDataChanged|Se produce cuando se modifican los datos o el valor dentro de una celda de cuadrícula. Este evento también se puede desencadenar si el valor de una celda se cambia mediante programación mediante la propiedad Value o el método SetCellValue de GridCell.|
|Clic en el botón de la celda|Ocurre cuando se hace clic en el botón de la celda.|
|CellCheckedChanged|Se produce cuando se cambia la casilla de verificación de la propiedad Marcada de la celda.|
|CellSelectedIndexChanged|Ocurre cuando se cambia la propiedad SelectedIndex del cuadro combinado de celda.|
|CellClick|Ocurre cuando se hace clic en una celda de cuadrícula.|
|CellDoubleClick|Ocurre cuando se hace doble clic en una celda de cuadrícula.|
|CellKeyPressed|Ocurre cuando se presiona una tecla mientras una celda tiene el foco. Si desea crear un controlador de eventos para el evento CellKeyPressed, establezca la propiedad Handled del argumento CellKeyEventArgs en verdadero para evitar que el control GridDesktop controle el evento clave.|
|AfterInsertColumnsAfterInsertColumns|Se produce cuando se inserta una columna. Puede obtener el índice de la columna utilizando la propiedad Index del argumento Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|AfterInsertRows|Ocurre cuando se inserta una fila. Puede obtener el índice de la fila mediante la propiedad Index del argumento Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|Error de carga de archivo|Se produce cuando no se puede cargar el libro de trabajo.|
|FinalizarCalcular|Ocurre después de calcular la fórmula en el libro de trabajo.|
|FinalizarCargarArchivo|Se produce cuando se carga el libro de trabajo.|
|FocusedCellChanged|Ocurre cada vez que se cambia el foco de una celda.|
|FilaEncabezadoClic|Ocurre cuando se hace clic en el encabezado de la fila.|
|RowHeaderDoubleClick|Ocurre cuando se hace doble clic en el encabezado de la fila.|
|FilaColumnaOcultoCambiado|Ocurre cuando se cambia el estado oculto de fila o columna.|
|SelectedSheetIndexChanged|Ocurre cuando un usuario selecciona una nueva hoja de cálculo, es decir, cuando la hoja seleccionada cambia de una hoja de cálculo a otra. Este evento también se puede desencadenar mediante programación si cambia la propiedad ActiveSheetIndex del control GridDesktop.|
## **Manejo de eventos de cuadrícula**
Para realizar una operación específica cuando se desencadena un evento específico, cree un controlador de eventos. Un controlador de eventos realiza una tarea particular cuando se desencadena un determinado evento. A continuación, se configura un controlador de eventos para manejar un evento Grid simple usando Visual Studio.NET.

**Paso 1: seleccionar un evento de Aspose.Cells. GridDesktop Control**

1. En Visual Studio, seleccione el control Aspose.Cells.GridDesktop y abra su**Propiedades** diálogo.
1.  Haga clic en el**Eventos** pestaña.
1.  Seleccione un evento. (para este ejemplo, el**CellClick** se selecciona el evento).

**Paso 2: crear un controlador de eventos**

1.  Haga doble clic en un evento seleccionado en el**Propiedades** diálogo.
1. Cuando se hace doble clic en el evento, Visual Studio.NET crea un controlador de eventos. A continuación se muestra el código generado por el diseñador que muestra que se crea un evento para el control GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 Ahora agregue código para realizar la operación deseada dentro del controlador de eventos. Para este ejemplo, hemos agregado una línea de código que muestra un cuadro de mensaje para notificaciones.
Eche un vistazo al controlador de eventos que Visual Studio ha agregado al evento CellClick del control GridDesktop. Se verá algo como el código de abajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Paso 3: ejecutar la aplicación**

1. Generar y ejecutar la aplicación.
1. Cada vez que se hace clic en una celda de la cuadrícula, aparece un cuadro de mensaje con el mensaje "Cell se hizo clic".
