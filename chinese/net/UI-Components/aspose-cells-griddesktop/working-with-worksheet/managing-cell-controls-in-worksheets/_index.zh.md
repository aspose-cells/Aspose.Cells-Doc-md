---
title: 在工作表中管理单元格控件
type: docs
weight: 130
url: /zh/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop，单元格控件，控件，控件
description: 这篇文章介绍了如何在GridDesktop中处理单元格控件。
---

{{% alert color="primary" %}} 

本主题讨论了使用Aspose.Cells.GridDesktop API管理单元格控件的一些重要概念。我们将解释开发人员如何访问，修改和移除工作表中的单元格控件。让我们来看一看。

{{% /alert %}} 
## **访问单元格控件**
要访问并修改工作表中现有的单元格控件，开发人员可以通过指定单元格控件所在的单元格（使用单元格名称或其行列号）从**Worksheet**的**Controls**集合中访问特定的单元格控件。一旦访问到单元格控件，开发人员可以在运行时修改其属性。例如，在下面的示例中，我们从**工作表**中访问了一个现有的**CheckBox**单元格控件，并修改了其Checked属性。

**重要提示：** **Controls**集合包含以**CellControl**对象形式存在的所有类型的单元格控件。因此，如果您需要访问特定类型的单元格控件，比如**CheckBox**，您将需要将**CellControl**对象转换为**CheckBox**类。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **移除单元格控件**
要移除现有的单元格控件，开发人员可以简单地访问所需的工作表，然后通过指定包含单元格控件的单元格（使用其名称或行列号）从**工作表**的**Controls**集合中**移除**单元格控件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
