---
title: 在工作表中添加或插入行
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop，插入，添加，行，插入行，添加行
description: 本文介绍了如何在 GridDesktop 中添加或插入行。
---

{{% alert color="primary" %}} 

类似于我们先前的一个主题，本主题描述了在运行时使用 Aspose.Cells.GridDesktop API 向工作表添加和插入行的功能。添加和插入之间的基本区别在于，添加是将行添加到工作表的行集合的末尾，而插入可以在工作表中的任何指定位置添加行。

{{% /alert %}} 
## **向工作表添加一行**
要向工作表添加新行，请按以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 在**工作表**中添加**行**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **将行插入工作表**
要在指定位置将新行插入工作表，请按以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 将**行**插入**工作表** (通过指定要插入到的行的索引位置)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
