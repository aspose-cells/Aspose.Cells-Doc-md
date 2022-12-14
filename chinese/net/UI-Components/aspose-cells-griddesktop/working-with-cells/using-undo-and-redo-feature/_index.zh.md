---
title: 使用撤消和重做功能
type: docs
weight: 120
url: /zh/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

GridDesktop 的撤消/重做功能非常有用。该名称本身就说明了它的功能，它允许您撤消/重做工作表中最近的操作。例如，如果一个公式被意外删除或您编辑了一个您实际上并不想要的单元格中的数据，这些操作可以通过使用控件提供的撤消和重做操作来纠正。

{{% /alert %}} 
## **执行撤消和重做操作**
以下 API 可用于该任务。每个API都给出了描述，请检查它们。

- **GridDesktop.EnableUndo** - 属性：表示是否启用Undo功能，默认值为“false”。
- **撤销管理器**– class：用于管理undo/redo操作。
- **GridDesktop.UndoManager** – 属性：它获取的实例**撤销管理器**目的。
- **UndoManager.Undo** – 方法：它执行撤销操作。
- **UndoManager.Redo -**方法：它执行重做操作。
- **UndoManager.ClearStack** – 方法：清除撤消/重做堆栈。
- **UndoManager.UndoStepsCount** – 属性：它获取当前可用的撤消步骤的计数。
- **UndoManager.RedoStepsCount** – 属性：它获取当前可用重做步骤的计数。
- **UndoManager.UndoStackSize** – 属性：它获取/设置撤消堆栈大小。
### **撤消**
下面的示例代码展示了如何使用 GridDesktop API 实现撤消操作。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **重做**
下面的示例代码展示了如何使用 GridDesktop API 实现 Redo 操作。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

目前，撤消/重做操作是指单元格值的更改。

{{% /alert %}}
