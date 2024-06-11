---
title: 使用撤消和重做功能
type: docs
weight: 120
url: /zh/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop，撤消，重做
description: 本文介绍了GridDesktop中的撤消和重做功能。
---

{{% alert color="primary" %}} 

GridDesktop的撤消/重做功能非常有用。名称自己解释了它的功能，它允许您在工作表中撤消/重做最近的操作。例如，如果一个公式被意外删除或者您编辑了一个您实际上不想要的单元格中的数据，这些操作可以通过控件提供的撤消和重做操作来纠正。

{{% /alert %}} 
## **执行撤消和重做操作**
以下API用于此任务。每个API都附有描述，请查阅。

- **GridDesktop.EnableUndo** - 属性: 它指示是否启用了撤消功能，默认值为"false"。
- **UndoManager** – 类: 用于管理撤消/重做操作。
- **GridDesktop.UndoManager** – 属性: 获取**UndoManager**对象的实例。
- **UndoManager.Undo** – 方法: 执行撤消操作。
- **UndoManager.Redo -** 方法: 执行重做操作。
- **UndoManager.ClearStack** – 方法: 清除撤销/恢复栈。
- **UndoManager.UndoStepsCount** – 属性: 获取当前可用的撤销步数。
- **UndoManager.RedoStepsCount** – 属性: 获取当前可用的重做步数。
- **UndoManager.UndoStackSize** – 属性: 获取/设置撤销栈的大小。
### **撤销**
以下示例代码展示如何使用GridDesktop API实现撤销操作。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **重做**
以下示例代码展示如何使用GridDesktop API实现重做操作。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

当前, 撤销/重做操作是指单元格值的更改。

{{% /alert %}}
