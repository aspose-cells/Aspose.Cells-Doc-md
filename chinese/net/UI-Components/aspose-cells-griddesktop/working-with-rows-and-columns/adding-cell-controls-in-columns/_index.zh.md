---
title: 在列中添加单元格控件
type: docs
weight: 90
url: /zh/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop，添加，控件，控件
description: 本文介绍如何在GridDesktop中的列中添加控件。
---

{{% alert color="primary" %}} 

在后续讨论中，我们已经讨论了如何添加和管理工作表中的单元格控件。但是，使用这些方法，我们只能逐个将单元格控件添加到单个单元格。如果有人想要将单元格控件添加到一个或多个列的所有单元格中，怎么办？在这种情况下，为了减少开发人员的工作量，Aspose.Cells.GridDesktop提供了按列添加单元格控件的功能。这意味着开发人员可以只选择所需的列并指定任何单元格控件。指定的单元格控件将添加到指定列的所有单元格。让我们看看如何使用这一功能。

{{% /alert %}} 
## **介绍**
目前，Aspose.Cells.GridDesktop支持添加三种类型的单元格控件，包括以下内容：

- **按钮**
- **复选框**
- **组合框**

所有这些控件都是从一个抽象类 **CellControl** 派生而来。

**重要:** 如果您想将单元控件添加到单个单元格而不是整个列中，您可以参考[在工作表中添加单元格控件。](/cells/zh/net/adding-cell-controls-in-worksheets/)
### **添加按钮**
要使用Aspose.Cells.GridDesktop在列中添加按钮，请按照以下步骤进行：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 将 **Button** 添加到 **Worksheet** 的任意指定 **Column** 中

**注意:** 在添加 **Button** 时，我们可以指定按钮的宽度、高度和标题。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


以上代码片段会向指定列的所有单元格添加按钮。每当选择该特定列的任何单元格时，按钮会变为可见。有关按钮事件处理的更多信息，请参考[按钮控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **添加复选框**
要使用Aspose.Cells.GridDesktop在列中添加复选框，请按照以下步骤进行：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 将 **CheckBox** 添加到 **Worksheet** 的任意指定 **Column** 中

**注意:** 在添加 **CheckBox** 时，我们还可以指定复选框的状态。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


以上代码片段会向指定列的所有单元格添加复选框。有关复选框事件处理的更多信息，请参阅[复选框控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **添加下拉框**
要使用Aspose.Cells.GridDesktop在列中添加下拉框，请按照以下步骤进行：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 创建一个将添加到 **ComboBox** 中的项目（或值）数组
- 将包含项目或值的 **ComboBox** 添加到 **Worksheet** 的任意指定 **Column** 中



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


以上代码片段会向指定列的所有单元格添加下拉框。每当选择该特定列的任何单元格时，下拉框会变为可见。有关下拉框事件处理的更多信息，请参阅[下拉框控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
