---
title: 在工作表中添加单元格控件
type: docs
weight: 120
url: /zh/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop，添加，控件，按钮，复选框，组合框
description: 本文介绍了如何在GridDesktop中的工作表添加控件。
---

{{% alert color="primary" %}} 

单元格控件实际上是可以添加到工作表中的控件。我们称之为**单元格控件**，因为这些控件显示在单元格中。在本主题中，我们将讨论添加和处理这些单元格控件的事件。

{{% /alert %}} 
## **介绍**
目前，Aspose.Cells.GridDesktop支持添加三种类型的单元格控件，包括以下内容：

- **按钮**
- **复选框**
- **组合框**

所有这些控件都是从一个抽象类**CellControl**派生出来的。每个工作表包含一个**Controls**集合。使用这个**Controls**集合可以轻松地添加新的单元格控件和访问现有的单元格控件。

**重要：** 如果要将单元格控件添加到整个列的所有单元格而不是逐个添加，可以参考[在工作表中管理单元格控件。](/cells/zh/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **添加按钮**
使用Aspose.Cells.GridDesktop将按钮添加到工作表，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**Form**中
- 访问任意所需的**Worksheet**
- 将**按钮**添加到**Worksheet**的**Controls**集合中



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


在添加**按钮**时，我们可以指定单元格的位置（显示在何处）、宽度和高度以及按钮的标题。
#### **按钮事件处理**
我们已经讨论了如何向**Worksheet**添加**按钮**控件，但是如果我们无法使用它，那么在工作表中只有一个按钮有什么好处呢。这就需要对按钮的事件处理。

要处理**按钮**控件的**单击**事件，Aspose.Cells.GridDesktop提供了应根据需要由开发人员实现的**CellButtonClick**事件。例如，我们只是在下面的代码中单击按钮时显示了一条消息：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **为按钮控件指定背景图像**
我们可以设置背景图像/图片作为按钮控件的标签/文本，如下面的代码所示：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**重要：** 所有单元格控件的事件都包含一个**CellControlEventArgs**参数，提供包含了该单元格控件（其事件被触发）的行号和列号。
### **添加复选框**
使用Aspose.Cells.GridDesktop将复选框添加到工作表，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**Form**中
- 访问任意所需的**Worksheet**
- 将**复选框**添加到**Worksheet**的**Controls**集合中



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


在添加**复选框**时，我们可以指定单元格的位置（显示在何处）和复选框的状态。
#### **复选框事件处理**
Aspose.Cells.GridDesktop提供了一个在复选框的**Checked**状态改变时触发的**CellCheckedChanged**事件。开发人员可以根据自己的需求处理此事件。例如，我们只是在下面的代码中显示了一个消息，以展示复选框的**Checked**状态：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **添加下拉框**
使用Aspose.Cells.GridDesktop向工作表添加下拉框，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**Form**中
- 访问任意所需的**Worksheet**
- 创建一个数组，其中包含将添加到**ComboBox**中的项目（或值）
- 通过指定单元格的位置（单击下拉框时将显示在哪里）和将在单击下拉框时显示的项目/值，将**ComboBox**添加到**Worksheet**的**Controls**集合



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **下拉框事件处理**
Aspose.Cells.GridDesktop提供了一个在下拉框的**Selected Index**更改时触发的**CellSelectedIndexChanged**事件。开发人员可以根据自己的需求处理此事件。例如，我们只是在下面的代码中显示了一个消息，以展示下拉框的**Selected Item**：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
