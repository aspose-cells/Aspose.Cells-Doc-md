---
title: 在列中管理单元格控件
type: docs
weight: 100
url: /zh/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop，控件，控制
description: 本文介绍了如何在列GridDesktop中设置控件。
---

{{% alert color="primary" %}} 

本主题讨论了使用Aspose.Cells.GridDesktop API在列中管理单元格控件的一些重要概念。我们将解释开发人员如何访问、修改和删除工作表列中的单元格控件。让我们来看看。

{{% /alert %}} 
## **访问单元格控件**
要访问和修改列中的现有单元格控件，开发人员可以使用 **Aspose.Cells.GridDesktop.Data.GridColumn** 的 CellControl 属性。一旦访问到单元格控件，开发人员可以在运行时修改其属性。例如，在下面给出的示例中，我们从特定的 **Aspose.Cells.GridDesktop.Data.GridColumn** 中访问了一个现有的 **CheckBox** 单元格控件，并修改了它的 Checked 属性。

**重要提示：** CellControl 属性提供了一个 **CellControl** 对象形式的单元格控件。因此，如果您需要访问特定类型的单元格控件，比如 **CheckBox**，那么您将不得不将 **CellControl** 对象转换为 **CheckBox** 类。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **移除单元格控件**
要移除现有的单元格控件，开发人员可以简单地访问所需的工作表，然后使用 **Aspose.Cells.GridDesktop.Data.GridColumn** 的 **RemoveCellControl** 方法从特定列中移除单元格控件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

工作表的 **Columns** 集合中的每个列都由 **Aspose.Cells.GridDesktop.Data.GridColumn** 类的实例表示。

{{% /alert %}}
