---
title: GridDesktop中合并和取消合并单元格
linktitle: 合并和分割单元格
type: docs
weight: 90
url: /zh/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop，合并，取消合并
description: 本文介绍了GridDesktop中的合并和取消合并。
---

{{% alert color="primary" %}} 

在本主题中，我们将讨论工作表的合并和取消合并单元格的实用功能。在需要跨越一些行或列以提高数据可读性的情况下，此功能非常有用。

{{% /alert %}} 
## **合并单元格**
要将单元格合并为一个大单元格，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 创建要合并的**单元范围**
- 将单元范围**合并**成大单元格

您可以使用**工作表**的**合并**方法来合并单元格。然而，可以使用**CellRange**对象来定义单元范围。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **取消合并单元格**
要将大单元格取消合并为多个单元格，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 访问需要取消合并的合并单元格
- 使用合并单元格的位置**取消合并**大单元格为多个单元格

您可以使用**工作表**的**取消合并**方法来使用其位置取消合并单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

当您将单元格合并为一个单元格时，合并单元格的左上角单元格（在单元范围内）的格式设置将应用于合并单元格，但当取消合并单元格时，所有取消合并的单元格将保留其格式设置。

{{% /alert %}}
