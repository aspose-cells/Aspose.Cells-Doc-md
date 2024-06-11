---
title: 在列中添加单元格控件
type: docs
weight: 90
url: /zh/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: 本文介绍如何在GridDesktop中的列中添加控件。
---

{{% alert color="primary" %}} 

在我们以后的讨论中，我们已经讨论了在工作表中添加和管理单元格控件。但是，使用这些方法，我们可以逐个将单元格控制添加到单个单元格中。如果有人想要将单元格控件添加到一个或多个列的所有单元格中怎么办？在这种情况下，为了减少开发人员的工作量，Aspose.Cells.GridDesktop提供了根据列添加单元格控件的功能。这意味着开发人员只需选择一个所需的列并指定任何单元格控件。指定的单元格控件将添加到所指定列的所有单元格中。让我们看看如何使用此功能。

{{% /alert %}} 
## **介绍**
目前，Aspose.Cells.GridDesktop支持添加三种类型的单元格控件，包括如下：

- **按钮**
- **复选框**
- **组合框**

所有这些控件都是继承自抽象类**CellControl**。

**重要:** 如果要将单元格控件添加到单个单元格而不是整个列，则可以参考[在工作表中添加单元格控件。](/cells/zh/net/adding-cell-controls-in-worksheets/)
### **添加按钮**
要在Aspose.Cells.GridDesktop中的列中添加按钮，请按照以下步骤操作:

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 将**按钮**添加到**工作表**的任何指定**列**中

**注意:** 在添加**按钮**时，我们可以指定按钮的宽度、高度和标题。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


上述代码片段将按钮添加到所指定列的所有单元格中。每当选择特定列的任何单元格时，按钮会变为可见。有关按钮事件处理的更多信息，请参阅[按钮控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **添加复选框**
要在Aspose.Cells.GridDesktop中的列中添加复选框，请按照以下步骤操作:

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 在**工作表**的任何指定**列**中添加**复选框**

**注意：** 在添加**复选框**时，我们还可以指定复选框的状态。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


上面的代码片段将复选框添加到指定列的所有单元格。有关复选框的事件处理的更多信息，请参阅[复选框控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **添加下拉列表框**
要使用Aspose.Cells.GridDesktop在列中添加组合框，请按照以下步骤进行：

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 创建一个将添加到**组合框**的项目（或值）数组
- 在**工作表**的任何指定**列**中添加包含项目或值的**组合框**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


上面的代码片段将组合框添加到指定列的所有单元格。每当选择特定列的任何单元格时，组合框都会变为可见。有关组合框的事件处理的更多信息，请参阅[组合框控件的事件处理。](/cells/zh/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
