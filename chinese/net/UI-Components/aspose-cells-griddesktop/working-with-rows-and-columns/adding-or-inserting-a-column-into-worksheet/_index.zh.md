---
title: 在工作表中添加或插入列
type: docs
weight: 10
url: /zh/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

在本主题中，我们将介绍使用 Aspose.Cells.GridDesktop 的 API 在运行时向工作表添加和插入列的基本功能。添加和插入之间的基本区别在于，另外，在工作表的列集合的末尾添加列，而在插入中，可以将列添加到工作表中的任何指定位置。

{{% /alert %}} 
## **向工作表添加列**
要向工作表添加新列，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**柱子**到**工作表**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **在工作表中插入一列**
要在工作表的指定位置插入新列，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 插入**柱子**进入**工作表** （通过指定插入列的索引在特定位置）

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
