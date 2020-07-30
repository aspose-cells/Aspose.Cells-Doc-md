---
title : "Using Undo and Redo Feature" 
description : "" 
weight : 16648 
toc : false
type: docs
url: /net/developerguide/griddesktop/cells/using+undo+and+redo+feature/
---

# Aspose.Cells for .NET : Using Undo and Redo Feature


The GridDesktop's Undo/Redo feature is very useful. The name explains its functionality itselft, it allows you to undo/redo the recent action(s) in a worksheet. For example, if a formula is accidentally deleted or you edit data in a cell which you don't actually want, these actions can be corrected by using the Undo and Redo operations provided by the control.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Performing Undo and Redo Operation](#performing-undo-and-redo-operation)
    *   1.1 [Undo](#undo)
{{< /panel >}}

 

 

## Performing Undo and Redo Operation

The following APIs are available for the task. The description is given with each API, please check them.

*   **GridDesktop.EnableUndo** - attribute: It indicates whether the Undo function is enabled, the default value is "false".
*   **UndoManager** – class: It is used to manage the undo/redo operation.
*   **GridDesktop.UndoManager** – attribute: It gets the instance of the **UndoManager** object.
*   **UndoManager.Undo** – method: It performs an undo operation.
*   **UndoManager.Redo -** method: It performs the redo operation.
*   **UndoManager.ClearStack** – method: It clears the undo/redo stack.
*   **UndoManager.UndoStepsCount** – attribute: It gets the count of current available undo steps.
*   **UndoManager.RedoStepsCount** – attribute: It gets the count of current available redo steps.
*   **UndoManager.UndoStackSize** – attribute: It gets/sets the undo stack size.

### Undo

The following sample code shows how to implement the Undo operation using the GridDesktop API.

###   
Redo

The following sample code shows how to implement the Redo operation using the GridDesktop API.

Currently, undo/redo operation refers to the change in a cell value.

