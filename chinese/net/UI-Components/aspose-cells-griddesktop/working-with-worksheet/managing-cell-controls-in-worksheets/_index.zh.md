---
title: 管理工作表中的单元格控件
type: docs
weight: 130
url: /zh/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop,cell控件, 控件，控件
description: 本文介绍了如何在GridDesktop中使用单元格控件。
---

{{% alert color="primary" %}} 

本主题讨论了使用Aspose.Cells.GridDesktop的API管理单元格控件的一些重要概念。我们将解释开发人员如何访问、修改和删除工作表中的单元格控件。让我们来看看。

{{% /alert %}} 
## **访问单元格控件**
要访问和修改工作表中现有的单元格控件，开发人员可以通过指定单元格（使用单元格名称或其在行和列编号方面的位置）从**Worksheet**的**Controls**集合中访问特定的单元格控件。一旦访问了单元格控件，开发人员可以在运行时修改它的属性。例如，在下面的示例中，我们从**Worksheet**中访问了一个现有的**CheckBox**单元格控件，并修改了它的Checked属性。

**重要:** **Controls**集合以**CellControl**对象的形式包含所有类型的单元格控件。因此，如果您需要访问特定类型的单元格控件，比如**CheckBox**，则需要将**CellControl**对象强制转换为**CheckBox**类。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **删除单元格控件**
要删除现有单元格控件，开发人员只需访问所需的工作表，然后通过指定包含单元格控件的**Controls**集合中的单元格（使用其名称或行和列编号）来**删除**单元格控件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
