---
title: Trabajar con eventos de Aspose.Cells.GridDesktop
type: docs
weight: 30
url: /es/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, evento, eventos
description: Este artículo presenta cómo usar eventos en GridDesktop.
---

{{% alert color="primary" %}} 

Los eventos se utilizan para enviar notificaciones cuando ocurre un cambio en un control o clase. Aspose.Cells.GridDesktop tiene varios eventos que se utilizan para realizar tareas específicas cuando ocurren ciertos cambios en el control. Este tema proporciona una introducción a todos los eventos admitidos por el control Aspose.Cells.GridDesktop y explica cómo manejar esos eventos.

{{% /alert %}} 
## **Introducción**
El control Aspose.Cells.GridDesktop admite varios eventos que brindan más control para realizar operaciones cuando se activan eventos específicos. A continuación se muestra una lista completa de eventos admitidos por el control Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

Esta lista no incluye aquellos eventos heredados por Aspose.Cells.GridDesktop de la clase Control.

{{% /alert %}} 

| **Eventos** | **Descripción** |
| :- | :- |
| BeforeCalculate | Ocurre antes de calcular la fórmula en el libro de trabajo. |
| BeforeLoadFile | Ocurre antes de que se cargue el libro de trabajo desde el archivo. |
| ColumnHeaderClick | Ocurre cuando se hace clic en el encabezado de la columna. |
| ColumnHeaderDoubleClick | Ocurre cuando se hace doble clic en el encabezado de la columna. |
| CellDataChanged | Ocurre cuando los datos o el valor dentro de una celda de la cuadrícula cambian. Este evento también puede activarse si se cambia el valor de una celda programáticamente utilizando la propiedad Value o el método SetCellValue de una GridCell. |
| CellButtonClick | Ocurre cuando se hace clic en el botón de la celda. |
| CellCheckedChanged | Ocurre cuando se cambia la propiedad Checked de la casilla de verificación de la celda. |
| CellSelectedIndexChanged | Ocurre cuando se cambia la propiedad SelectedIndex de la celda de lista desplegable. |
| CellClick | Ocurre cuando se hace clic en una celda de la cuadrícula. |
| |CellDoubleClick| Ocurre cuando se hace doble clic en una celda de la cuadrícula. |
| CellKeyPressed | Ocurre cuando se presiona una tecla mientras una celda tiene el foco. Si desea crear un controlador de eventos para el evento CellKeyPressed, establezca la propiedad Handled del argumento CellKeyEventArgs en true para evitar que el control GridDesktop maneje el evento de tecla. |
| AfterInsertColumns | Ocurre cuando se inserta una columna. Puede obtener el índice de la columna utilizando la propiedad Index del argumento Aspose.Cells.GridDesktop.WorksheetEventArgs. |
| AfterInsertRows | Ocurre cuando se inserta una fila. Puede obtener el índice de la fila utilizando la propiedad Index del argumento Aspose.Cells.GridDesktop.WorksheetEventArgs. |
| FailLoadFile | Ocurre cuando falla al cargar el libro de trabajo. |
| FinishCalculate | Ocurre después de calcular la fórmula en el libro de trabajo. |
| FinishLoadFile | Ocurre cuando el libro de trabajo se carga. |
|FocusedCellChanged|Se produce cada vez que se cambia el foco de una celda.|
|RowHeaderClick|Se produce cuando se hace clic en el encabezado de fila.|
|RowHeaderDoubleClick|Se produce cuando se hace doble clic en el encabezado de fila.|
|RowColumnHiddenChanged|Se produce cuando se cambia el estado oculto de la fila o columna.|
|SelectedSheetIndexChanged|Se produce cuando un usuario selecciona una nueva hoja de cálculo, es decir, cuando la hoja seleccionada cambia de una hoja de cálculo a otra. Este evento también puede ser activado programáticamente si cambia la propiedad ActiveSheetIndex del control GridDesktop.|
## **Manejo de Eventos de la Cuadrícula**
Para realizar una operación específica cuando se desencadena un evento específico, cree un controlador de eventos. Un controlador de eventos realiza una tarea particular cuando se desencadena cierto evento. A continuación, se configura un controlador de eventos para manejar un simple evento de la cuadrícula utilizando Visual Studio.NET.

**Paso 1: Selección de un Evento de Control Aspose.Cells.GridDesktop**

1. En Visual Studio, seleccione el control Aspose.Cells.GridDesktop y abra su cuadro de diálogo **Propiedades**.
1. Haga clic en la pestaña **Eventos**.
1. Seleccione un evento. (por ejemplo, se selecciona el evento **CellClick** para este ejemplo).

**Paso 2: Creación de un Controlador de Eventos**

1. Haga doble clic en un evento seleccionado en el cuadro de diálogo **Propiedades**.
1. Cuando se hace doble clic en el evento, Visual Studio.NET crea un controlador de eventos. A continuación, se muestra el código generado por el diseñador que muestra que se crea un evento para el Control GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Ahora agregue código para realizar la operación deseada dentro del controlador de eventos. Para este ejemplo, hemos agregado una línea de código que muestra un cuadro de diálogo para las notificaciones. 
Eche un vistazo al controlador de eventos que Visual Studio ha agregado al evento CellClick del control GridDesktop. Se verá algo como el código a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Paso 3: Ejecución de la Aplicación**

1. Compile y ejecute la aplicación.
1. Cada vez que se hace clic en una celda de la cuadrícula, aparece un cuadro de diálogo con el mensaje "Se hizo clic en la celda".
