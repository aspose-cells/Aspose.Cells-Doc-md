---
title: 在工作表中添加或插入行
type: docs
weight: 30
url: /zh/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

与我们之前的主题之一类似，本主题描述了使用 Aspose.Cells.GridDesktop 的 API 在运行时向工作表添加和插入行的功能。添加和插入之间的基本区别在于，另外，在工作表的行集合的末尾添加一行，而在插入中，可以将行添加到工作表中的任何指定位置。

{{% /alert %}} 
## **向工作表添加行**
要向工作表添加新行，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**排**到**工作表**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **在工作表中插入一行**
要在工作表的指定位置插入新行，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 插入**排**进入**工作表**（通过指定插入行的索引在特定位置）

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
