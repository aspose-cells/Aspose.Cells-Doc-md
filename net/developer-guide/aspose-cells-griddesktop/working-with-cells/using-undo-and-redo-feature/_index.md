---
title: Using Undo and Redo Feature
type: docs
weight: 120
url: /net/using-undo-and-redo-feature/
---

{{% alert color="primary" %}} 

The GridDesktop's Undo/Redo feature is very useful. The name explains its functionality itself, it allows you to undo/redo the recent action(s) in a worksheet. For example, if a formula is accidentally deleted or you edit data in a cell which you don't actually want, these actions can be corrected by using the Undo and Redo operations provided by the control.

{{% /alert %}} 
## **Performing Undo and Redo Operation**
The following APIs are available for the task. The description is given with each API, please check them.

- **GridDesktop.EnableUndo** - attribute: It indicates whether the Undo function is enabled, the default value is "false".
- **UndoManager** – class: It is used to manage the undo/redo operation.
- **GridDesktop.UndoManager** – attribute: It gets the instance of the **UndoManager** object.
- **UndoManager.Undo** – method: It performs an undo operation.
- **UndoManager.Redo -** method: It performs the redo operation.
- **UndoManager.ClearStack** – method: It clears the undo/redo stack.
- **UndoManager.UndoStepsCount** – attribute: It gets the count of current available undo steps.
- **UndoManager.RedoStepsCount** – attribute: It gets the count of current available redo steps.
- **UndoManager.UndoStackSize** – attribute: It gets/sets the undo stack size.
### **Undo**
The following sample code shows how to implement the Undo operation using the GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Redo**
The following sample code shows how to implement the Redo operation using the GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Currently, undo/redo operation refers to the change in a cell value.

{{% /alert %}}
