---
title: 使用撤消和重做功能
type: docs
weight: 120
url: /zh/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop，撤消，重做
description: 本文介绍了GridDesktop中的撤消和重做功能。
---

{{% alert color="primary" %}} 

GridDesktop的撤消/重做功能非常有用。名称本身就解释了它的功能，它允许您在工作表中撤消/重做最近的操作。例如，如果意外删除了一个公式，或者编辑了一个您实际上不想要的单元格中的数据，则可以使用该控件提供的撤消和重做操作来更正这些操作。

{{% /alert %}} 
## **执行撤消和重做操作**
以下API可用于此任务。请查看每个API的描述。

- **GridDesktop.EnableUndo** - 属性: 它指示撤销功能是否已启用，默认值为"false"。
- **UndoManager** – 类: 用于管理撤销/重做操作。
- **GridDesktop.UndoManager** – 属性: 获取**UndoManager**对象的实例。
- **UndoManager.Undo** – 方法: 执行撤销操作。
- **UndoManager.Redo -** 方法: 执行重做操作。
- **UndoManager.ClearStack** – 方法: 清除撤销/重做堆栈。
- **UndoManager.UndoStepsCount** – 属性: 获取当前可用的撤销步骤数。
- **UndoManager.RedoStepsCount** – 属性: 获取当前可用的重做步骤数。
- **UndoManager.UndoStackSize** – 属性: 获取/设置撤销堆栈大小。
### **撤销**
以下示例代码展示了如何使用GridDesktop API实现撤销操作。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **重做**
以下示例代码展示了如何使用GridDesktop API实现重做操作。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

目前，撤销/重做操作指的是单元格值的变化。

{{% /alert %}}
