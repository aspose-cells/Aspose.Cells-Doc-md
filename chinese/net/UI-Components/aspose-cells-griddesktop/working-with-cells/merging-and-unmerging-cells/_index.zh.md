---
title: GridDesktop 中合并和拆分单元格
linktitle: 合并和拆分单元格
type: docs
weight: 90
url: /zh/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop、合并、拆分
description: 介绍了 GridDesktop 中的合并和拆分。
---

{{% alert color="primary" %}} 

本主题将讨论工作表单元格合并和拆分的实用功能。在需要跨越一些行或列以增强数据可读性时，此功能非常有用。

{{% /alert %}} 
## **合并单元格**
要将单元格合并成一个较大的单元格，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 创建要合并的 **单元格范围**
- **合并** 单元格范围成一个大单元格

您可以使用 **Worksheet** 的 **Merge** 方法合并单元格。但是，可以使用 **CellRange** 对象定义单元格范围。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **拆分单元格**
要将一个大单元格拆分为多个单元格，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 访问需要取消合并的合并单元格
- 使用合并单元格的位置将大单元格取消合并为多个单元格

您可以使用**Worksheet**的**Unmerge**方法根据其位置取消合并单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

当您将单元格合并为一个单元格时，将对合并单元格应用左上角单元格的格式设置（在单元格范围内），但当取消合并单元格时，所有未合并的单元格将保留其格式设置。

{{% /alert %}}
