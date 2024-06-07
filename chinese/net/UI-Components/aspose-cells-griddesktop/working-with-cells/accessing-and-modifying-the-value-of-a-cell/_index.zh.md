---
title: 访问和修改单元格的值
type: docs
weight: 20
url: /zh/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,修改单元格,获取单元格,修改单元格值,获取单元格值
description: 本文介绍如何在GridDesktop中获取和修改单元格值
---

{{% alert color="primary" %}} 

在之前的话题中，我们已经讨论了如何访问工作表的单元格。在本话题中，我们将简单扩展该话题，以向开发人员展示如何使用Aspose.Cells.GridDesktop的API访问和修改单元格的值

{{% /alert %}} 
## **使用Aspose.Cells.GridDesktop访问和修改单元格的值**
在访问和修改单元格的值之前，我们应该了解如何访问单元格。访问工作表的单元格有三种方法。有关这三种方法的更多详细信息，请参阅[访问工作表中的单元格.](/cells/zh/net/accessing-cells-in-a-worksheet/)

每个单元格都有一个名为值（Value）的属性。因此，一旦访问了单元格，开发人员就可以访问和修改值属性的内容，以访问和更改单元格的值



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**重要：**使用单元格的Value属性修改其值是设置单个或少量单元格的值的良好方法。如果需要设置多个单元格的值，则此方法的性能不佳。因此，为了设置多个单元格的值，应使用单元格的**SetCellValue**方法来提高应用程序的性能。使用**SetCellValue**方法的修改版本如下所示



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
