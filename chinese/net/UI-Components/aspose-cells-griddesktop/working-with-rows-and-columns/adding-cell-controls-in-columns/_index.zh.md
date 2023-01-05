---
title: 在列中添加 Cell 控件
type: docs
weight: 90
url: /zh/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

在我们后面的讨论中，我们讨论了如何在工作表中添加和管理单元格控件。但是，使用这些方法，我们可以将单元格控件一个接一个地添加到单个单元格中。如果有人想将单元格控件添加到一列或多列的所有单元格怎么办？在这种情况下，为了减少开发人员的工作量，Aspose.Cells.GridDesktop 提供了按列添加单元格控件的功能。这意味着开发人员只能选择所需的列并指定任何单元格控件。指定的单元格控件将添加到指定列的所有单元格。让我们看看如何使用此功能。

{{% /alert %}} 
## **介绍**
目前Aspose.Cells.GridDesktop支持添加三种类型的单元格控件，包括以下几种：

- **按钮**
- **复选框**
- **组合框**

所有这些控件都派生自一个抽象类，**细胞控制**.

**重要的：**如果您想将单元格控件添加到单个单元格而不是整列，那么您可以参考[在工作表中添加 Cell 控件。](/cells/zh/net/adding-cell-controls-in-worksheets/)
### **添加按钮**
要使用 Aspose.Cells.GridDesktop 将按钮添加到列中，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**按钮**任何指定**柱子**的**工作表**

**笔记：**添加时**按钮**我们可以指定按钮的宽度、高度和标题。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


上面的代码片段将按钮添加到指定列的所有单元格。 Whenever any cell of that specific column is selected, a button becomes visible.有关按钮事件处理的更多信息，请参阅[按钮控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **添加复选框**
要使用 Aspose.Cells.GridDesktop 将复选框添加到列中，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**复选框**任何指定**柱子**的**工作表**

**笔记：**添加时**复选框**，我们还可以指定复选框的状态。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


上面的代码片段将复选框添加到指定列的所有单元格。有关复选框事件处理的更多信息，请参阅[CheckBox 控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **添加组合框**
要使用 Aspose.Cells.GridDesktop 将组合框添加到列中，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 创建将添加到的项目（或值）数组**组合框**
- 添加**组合框**（包含项目或值）到任何指定**柱子**的**工作表**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


上面的代码片段将组合框添加到指定列的所有单元格。 Whenever any cell of that specific column is selected, a combobox becomes visible.有关组合框事件处理的更多信息，请参阅[ComboBox 控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
