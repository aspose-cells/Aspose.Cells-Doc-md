---
title: 访问和修改单元格的值
type: docs
weight: 20
url: /zh/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: 本文介绍如何在GridDesktop中获取和修改单元格的值。
---

{{% alert color="primary" %}} 

在上一个主题中，我们讨论了如何访问工作表的单元格。在本主题中，我们将简单扩展该主题，以向开发人员展示如何使用Aspose.Cells.GridDesktop的API来访问和修改单元格的值。

{{% /alert %}} 
## **使用Aspose.Cells.GridDesktop访问和修改单元格的值**
在访问和修改单元格的值之前，我们应该知道如何访问单元格。有三种访问工作表单元格的方法。有关这三种方法的详细信息，请参阅[在工作表中访问单元格](/cells/zh/net/accessing-cells-in-a-worksheet/)。

每个单元格都有一个名为Value的属性。因此，一旦访问了单元格，开发人员就可以访问和修改Value属性的内容，从而访问和更改单元格的值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**重要提示：** 使用单元格的Value属性修改其值是设置单个或少量单元格的值的良好方法。如果需要设置许多单元格的值，则此方法的性能将不佳。因此，为了设置许多单元格的值，应使用单元格的**SetCellValue**方法来提高应用程序的性能。下面显示了使用**SetCellValue**方法的上述代码片段的修改版本。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
