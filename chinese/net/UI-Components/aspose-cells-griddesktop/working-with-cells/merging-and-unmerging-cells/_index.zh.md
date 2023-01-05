---
title: 在 GridDesktop 中合并和取消合并 Cells
linktitle: 合并和取消合并 Cells
type: docs
weight: 90
url: /zh/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

在本主题中，我们将讨论合并和取消合并工作表单元格的实用功能。当我们需要跨越某些行或列以增强数据的可读性时，此功能非常有用。

{{% /alert %}} 
## **合并 Cells**
要将单元格合并为一个大单元格，请按照以下步骤操作：

- 访问任何想要的**工作表**
- 创建一个**范围Cells**合并
- **合并**单元格的范围变成一个大单元格

您可以使用**合并**的方法**工作表**合并单元格。但是，可以使用定义一系列单元格**单元格范围**目的。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **取消合并 Cells**
要将一个大单元格拆分为多个单元格，请按照以下步骤操作：

- 访问任何想要的**工作表**
- 访问需要取消合并的合并单元格
- **取消合并**使用合并单元格的位置将大单元格分成许多单元格

您可以使用**取消合并**的方法**工作表**使用其位置取消合并单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

当您将单元格合并为单个单元格时，左上角单元格（在单元格范围内）的格式设置将应用于合并的单元格，但当单元格未合并时，所有未合并的单元格将保持其格式设置。

{{% /alert %}}
