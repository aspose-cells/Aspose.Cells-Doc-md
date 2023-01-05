---
title: Uso de la función Deshacer y Rehacer
type: docs
weight: 120
url: /es/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

La función Deshacer/Rehacer de GridDesktop es muy útil. El nombre explica su funcionalidad en sí mismo, le permite deshacer/rehacer las acciones recientes en una hoja de trabajo. Por ejemplo, si una fórmula se elimina accidentalmente o si edita datos en una celda que en realidad no desea, estas acciones se pueden corregir mediante las operaciones Deshacer y Rehacer proporcionadas por el control.

{{% /alert %}} 
## **Ejecución de operaciones de deshacer y rehacer**
Las siguientes API están disponibles para la tarea. La descripción se proporciona con cada API, verifíquelos.

- **GridDesktop.EnableUndo** - atributo: Indica si la función Deshacer está habilitada, el valor por defecto es "falso".
- **UndoManager** – class: Se utiliza para gestionar la operación de deshacer/rehacer.
- **GridDesktop.UndoManager** – atributo: Obtiene la instancia del**UndoManager** objeto.
- **UndoManager.Deshacer** – método: Realiza una operación de deshacer.
- **UndoManager.Rehacer -** método: Realiza la operación redo.
- **UndoManager.ClearStack** – método: Borra la pila de deshacer/rehacer.
- **UndoManager.UndoStepsCount** – atributo: Obtiene el conteo de pasos de deshacer disponibles actualmente.
- **UndoManager.RedoStepsCount** – atributo: Obtiene el conteo de pasos de rehacer disponibles actualmente.
- **UndoManager.UndoStackSize** – atributo: Obtiene/establece el tamaño de la pila de deshacer.
### **Deshacer**
El siguiente código de ejemplo muestra cómo implementar la operación Deshacer mediante GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Rehacer**
El siguiente código de ejemplo muestra cómo implementar la operación Redo mediante GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Actualmente, la operación de deshacer/rehacer se refiere al cambio en el valor de una celda.

{{% /alert %}}
