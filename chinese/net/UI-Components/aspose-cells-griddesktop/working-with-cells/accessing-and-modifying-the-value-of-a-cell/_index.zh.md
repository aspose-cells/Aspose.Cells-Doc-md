---
title: 访问和修改 a Cell 的值
type: docs
weight: 20
url: /zh/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

在我们之前的主题中，我们讨论了如何访问工作表的单元格。在本主题中，我们将简单地扩展该主题以向开发人员展示他们如何使用 Aspose.Cells.GridDesktop 的 API 访问和修改单元格的值。

{{% /alert %}} 
## **使用 Aspose.Cells.GridDesktop 访问和修改 Cell 值**
在访问和修改单元格的值之前，我们应该知道如何访问单元格。可以通过三种方法访问工作表的单元格。有关这三种方法的更多详细信息，请[在工作表中访问 Cells。](/cells/zh/net/accessing-cells-in-a-worksheet/)

每个单元格都有一个名为 Value 的属性。因此，一旦访问了单元格，开发人员就可以访问和修改 Value 属性的内容，以便访问和更改单元格的值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**重要的：**使用单元格的 Value 属性修改其值是设置单个或几个单元格值的好方法。如果您需要设置许多单元格的值，那么这种方法的性能不会很好。因此，要设置多个单元格的值，您应该使用**设置单元格值**用于提高应用程序性能的单元方法。上述代码片段的修改版本使用**设置单元格值**方法如下所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
