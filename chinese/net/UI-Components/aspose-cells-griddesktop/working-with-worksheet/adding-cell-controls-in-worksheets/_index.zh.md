---
title: 在工作表中添加单元格控件
type: docs
weight: 120
url: /zh/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: 本文介绍如何在GridDesktop的工作表中添加控件。
---

{{% alert color="primary" %}} 

实际上，单元格控件是可以添加到工作表中的控件。我们将它们称为**单元格控件**，因为这些控件显示在单元格中。在这个主题中，我们将讨论如何添加并处理这些单元格控件的事件。

{{% /alert %}} 
## **介绍**
目前，Aspose.Cells.GridDesktop支持添加三种类型的单元格控件，包括如下：

- **按钮**
- **复选框**
- **组合框**

所有这些控件都衍生自一个抽象类**CellControl**。每个工作表都包含一个**Controls**集合。可以轻松地通过这个**Controls**集合添加新的单元格控件并访问现有的控件。

**重要：** 如果你想在一列的所有单元格中添加单元格控件，而不是一个一个添加，那么你可以参考[在列中管理单元格控件。](/cells/zh/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **添加按钮**
使用Aspose.Cells.GridDesktop在工作表中添加按钮，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 将**按钮**添加到**工作表**的**控件**集合中



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


在添加**按钮**时，我们可以指定单元格的位置（显示位置）、宽度和高度以及按钮的标题。
#### **按钮的事件处理**
我们已经讨论了在**工作表**中添加**按钮**控件，但是如果我们不能使用它，那么在工作表中只有一个按钮有什么优势呢？这就需要处理按钮的事件。

为了处理**按钮**控件的**单击**事件，Aspose.Cells.GridDesktop提供了**CellButtonClick**事件，开发人员应根据需要实现它。例如，当按钮被点击时，我们只显示一个消息，如下所示：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **为按钮控件指定背景图片**
我们可以为按钮控件设置背景图片/图片，并附上标签/文本，如下所示的代码：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**重要：** 所有单元格控件的事件都包含一个**CellControlEventArgs**参数，该参数提供包含触发事件的单元格控件的行号和列号。
### **添加复选框**
使用Aspose.Cells.GridDesktop在工作表中添加复选框，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 将**复选框**添加到**工作表**的**控件**集合中



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


在添加**复选框**时，我们可以指定单元格的位置（显示位置）和复选框的状态。
#### **复选框的事件处理**
Aspose.Cells.GridDesktop提供了**CellCheckedChanged**事件，当复选框的**Checked**状态改变时触发。开发人员可以根据自己的需求处理此事件。例如，我们在下面的代码中只是显示了一个消息来显示复选框的**Checked**状态:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **添加下拉列表框**
要使用Aspose.Cells.GridDesktop在工作表中添加下拉列表框，请按照以下步骤进行:

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 创建一个数组（或值）的集合，将被添加到**下拉列表框**
- 通过指定单元格的位置（下拉列表框将显示的位置）和下拉列表框被点击时将显示的项目/值，将**下拉列表框**添加到**工作表**的**控件**集合中



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **下拉列表框的事件处理**
Aspose.Cells.GridDesktop提供了**CellSelectedIndexChanged**事件，当下拉列表框的**Selected Index**改变时触发。开发人员可以根据自己的需要处理此事件。例如，我们只是显示一个消息来显示下拉列表框的**Selected Item**:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
