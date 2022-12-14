---
title: 管理列中的 Cell 控件
type: docs
weight: 100
url: /zh/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

本主题讨论有关使用 Aspose.Cells.GridDesktop API 管理列中的单元格控件的一些重要概念。我们将解释开发人员如何从其工作表的列中访问、修改和删除单元格控件。让我们来看看它。

{{% /alert %}} 
## **访问 Cell 控件**
要访问和修改列中现有的单元格控件，开发人员可以使用**Aspose.Cells.GridDesktop.Data.GridColumn**.访问单元格控件后，开发人员可以在运行时修改其属性。例如，在下面给出的示例中，我们访问了一个现有的**复选框**来自特定的细胞控制**Aspose.Cells.GridDesktop.Data.GridColumn**并修改了它的 Checked 属性。

**重要的：** CellControl 属性以以下形式提供单元格控件**细胞控制**目的。所以，如果你需要访问特定类型的单元格控件，比如说**复选框**那么你将不得不强制转换**细胞控制**反对**复选框**班级。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **删除 Cell 控件**
要删除现有的单元格控件，开发人员可以简单地访问所需的工作表，然后**消除**通过使用特定列的单元格控件**删除单元格控件**的方法**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

中的每一列**列**的集合**工作表**由一个实例表示**Aspose.Cells.GridDesktop.Data.GridColumn**班级。

{{% /alert %}}
