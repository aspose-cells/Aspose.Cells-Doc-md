---
title: 管理列中的单元格控件
type: docs
weight: 100
url: /zh/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, 控件, 控制
description: 本文介绍了如何在列中设置GridDesktop控件。
---

{{% alert color="primary" %}} 

本主题讨论了使用Aspose.Cells.GridDesktop API管理列中单元格控件的一些重要概念。我们将解释开发人员如何访问、修改和删除他们工作表中列的单元格控件。让我们来看一下。

{{% /alert %}} 
## **访问单元格控件**
要访问并修改列中的现有单元格控件，开发人员可以使用**Aspose.Cells.GridDesktop.Data.GridColumn**的CellControl属性。一旦访问了单元格控件，开发人员就可以在运行时修改它的属性。例如，在下面的示例中，我们已经访问了特定**Aspose.Cells.GridDesktop.Data.GridColumn**中现有的**复选框**单元格控件，并修改了其Checked属性。

**重要:** CellControl 属性以**CellControl**对象的形式提供单元格控件。因此，如果您需要访问特定类型的单元格控件，比如**复选框**，那么您需要将**CellControl**对象转换为**CheckBox**类。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **删除单元格控件**
要移除现有的单元格控件，开发人员可以简单地访问所需的工作表，然后使用**Aspose.Cells.GridDesktop.Data.GridColumn**的**RemoveCellControl**方法从特定列中**移除**单元格控件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

**工作表**中的每一列都由**Aspose.Cells.GridDesktop.Data.GridColumn**类的实例表示。

{{% /alert %}}
