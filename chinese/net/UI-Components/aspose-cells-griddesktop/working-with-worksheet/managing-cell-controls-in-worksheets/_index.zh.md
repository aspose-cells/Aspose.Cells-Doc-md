---
title: 管理工作表中的 Cell 控件
type: docs
weight: 130
url: /zh/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

本主题讨论有关使用 Aspose.Cells.GridDesktop 的 API 管理单元格控件的一些重要概念。我们将解释开发人员如何从他们的工作表中访问、修改和删除单元格控件。让我们来看看它。

{{% /alert %}} 
## **访问 Cell 控件**
要访问和修改工作表中现有的单元格控件，开发人员可以从**控件**的集合**工作表**通过指定显示单元格控件的单元格（使用单元格名称或其在行号和列号方面的位置）。访问单元格控件后，开发人员可以在运行时修改其属性。例如，在下面给出的示例中，我们访问了一个现有的**复选框**细胞控制从**工作表**并修改了它的 Checked 属性。

**重要的：** **控件**集合包含所有类型的单元格控件，形式为**细胞控制**对象。所以，如果你需要访问特定类型的单元格控件，比如说**复选框**那么你将不得不强制转换**细胞控制**反对**复选框**班级。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **删除 Cell 控件**
要删除现有的单元格控件，开发人员可以简单地访问所需的工作表，然后**去掉**从细胞控制**控件**的集合**工作表**通过指定包含单元格控件的单元格（使用其名称或行号和列号）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
