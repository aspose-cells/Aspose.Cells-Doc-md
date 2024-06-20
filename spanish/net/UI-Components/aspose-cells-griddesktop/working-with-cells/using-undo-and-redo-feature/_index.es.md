---
title: Usar la función de Deshacer y Rehacer
type: docs
weight: 120
url: /es/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop, deshacer, rehacer
description: Este artículo presenta la función de deshacer y rehacer en GridDesktop.
---

{{% alert color="primary" %}} 

La función de **Deshacer/Rehacer** de GridDesktop es muy útil. El nombre explica su funcionalidad en sí, permite deshacer/rehacer la(s) acción(es) reciente(s) en una hoja de cálculo. Por ejemplo, si se borra accidentalmente una fórmula o se edita datos en una celda que en realidad no se desea, estas acciones pueden corregirse utilizando las operaciones de Deshacer y Rehacer proporcionadas por el control.

{{% /alert %}} 
## **Realizar la operación de Deshacer y Rehacer**
Los siguientes APIs están disponibles para la tarea. La descripción se da con cada API, por favor, revíselos.

- **GridDesktop.EnableUndo** - atributo: Indica si la función de deshacer está habilitada, el valor predeterminado es "false".
- **UndoManager** - clase: Se usa para gestionar la operación de deshacer/rehacer.
- **GridDesktop.UndoManager** - atributo: Obtiene la instancia del objeto **UndoManager**.
- **UndoManager.Undo** - método: Realiza una operación de deshacer.
- **UndoManager.Redo** - método: Realiza la operación de rehacer.
- **UndoManager.ClearStack** - método: Limpia la pila de deshacer/rehacer.
- **UndoManager.UndoStepsCount** - atributo: Obtiene el número de pasos de deshacer disponibles actualmente.
- **UndoManager.RedoStepsCount** - atributo: Obtiene el número de pasos de rehacer disponibles actualmente.
- **UndoManager.UndoStackSize** - atributo: Obtiene/establece el tamaño de la pila de deshacer.
### **Deshacer**
El siguiente código de muestra muestra cómo implementar la operación de Deshacer utilizando la API de GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Rehacer**
El siguiente código de muestra muestra cómo implementar la operación de Rehacer utilizando la API de GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Actualmente, la operación de deshacer/rehacer se refiere al cambio en el valor de una celda.

{{% /alert %}}
