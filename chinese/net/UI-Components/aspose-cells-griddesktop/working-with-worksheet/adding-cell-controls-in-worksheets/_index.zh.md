---
title: 在工作表中添加 Cell 控件
type: docs
weight: 120
url: /zh/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

Cell 控件实际上就是那些可以添加到工作表中的控件。我们称他们为**Cell 控件**因为这些控件显示在单元格中。在本主题中，我们将讨论如何添加和处理这些单元格控件的事件。

{{% /alert %}} 
## **介绍**
目前Aspose.Cells.GridDesktop支持添加三种类型的单元格控件，包括以下几种：

- **按钮**
- **复选框**
- **组合框**

所有这些控件都派生自一个抽象类，**细胞控制**.每个工作表包含一个集合**控件**.可以添加新的单元格控件，并且可以使用此访问现有的单元格控件**控件**轻松收藏。

**重要的：**如果你想将单元格控件添加到一列的所有单元格而不是一个一个地添加那么你可以参考[管理列中的 Cell 控件。](/cells/zh/net/adding-cell-controls-in-worksheets/)
### **添加按钮**
要使用 Aspose.Cells.GridDesktop 将按钮添加到工作表中，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**按钮**到**控件**的集合**工作表**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


添加时**按钮**，我们可以指定单元格的位置（显示位置）、宽度和高度以及按钮的标题。
#### **按钮的事件处理**
我们已经讨论过添加**按钮**控制到**工作表**但是如果我们不能使用它，那么在工作表中只拥有一个按钮有什么好处呢？那么，就需要对按钮进行事件处理了。

处理**点击**事件的**按钮**控件，Aspose.Cells.GridDesktop提供**单元格按钮点击**开发人员应根据需要实施的事件。例如，我们刚刚在单击按钮时显示了一条消息，如下所示：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **为按钮控件指定背景图像**
我们可以为按钮控件设置背景图像/图片及其标签/文本，如下面的代码所示：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**重要的：**单元格控件的所有事件都包含一个**CellControlEventArgs**提供包含单元格控件（其事件被触发）的单元格的行号和列号的参数。
### **添加复选框**
要使用 Aspose.Cells.GridDesktop 将复选框添加到工作表中，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**复选框**到**控件**的集合**工作表**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


添加时**复选框**，我们可以指定单元格的位置（显示它的位置）和复选框的状态。
#### **CheckBox 的事件处理**
Aspose.Cells.GridDesktop提供**CellCheckedChanged**当**勾选**复选框的状态已更改。开发者可以根据自己的需求来处理这个事件。例如，我们刚刚显示了一条消息以显示**勾选**以下代码中复选框的状态：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **添加组合框**
要使用 Aspose.Cells.GridDesktop 将组合框添加到工作表中，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 创建将添加到的项目（或值）数组**组合框**
- 添加**组合框**到**控件**的集合**工作表**通过指定单元格的位置（将显示组合框的位置）以及单击组合框时将显示的项目/值



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **ComboBox的事件处理**
Aspose.Cells.GridDesktop提供**CellSelectedIndexChanged**当**精选指数**组合框的更改。开发者可以根据自己的意愿来处理这个事件。例如，我们刚刚显示了一条消息以显示**所选项目**组合框的：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
