---
title: 向工作表添加或插入一行
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: 本文介绍了如何在 GridDesktop 中添加或插入行。
---

{{% alert color="primary" %}} 

类似于我们以前的某篇文章，本篇文章描述了在运行时使用 Aspose.Cells.GridDesktop 的 API 向工作表添加和插入行的功能。添加和插入的基本区别在于，添加是将行添加到工作表的行集合的末尾，而插入则可以将行插入到工作表的任何指定位置。

{{% /alert %}} 
## **向工作表添加一行**
要向工作表添加新行，请按照以下步骤执行:

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 将 **行** 添加到 **工作表**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **在工作表中插入行**
要在指定位置向工作表插入新行，请按照以下步骤执行:

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 向 **工作表** 中插入 **行**（通过指定要插入的行的索引位置）

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
