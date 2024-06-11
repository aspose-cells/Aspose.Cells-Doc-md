---
title: 添加或插入工作表中的列
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,插入,添加,列,插入列,插入行
description: 本文介绍了如何在GridDesktop中插入或添加列。
---

{{% alert color="primary" %}} 

在本主题中，我们将描述使用Aspose.Cells.GridDesktop的API在运行时向工作表添加和插入列的基本功能。添加和插入之间的基本区别在于，添加时列被添加到工作表的列集合的末尾，而插入时列可以添加到工作表中的任何指定位置。

{{% /alert %}} 
## **向工作表添加列**
要向工作表添加新列，请按照以下步骤进行：

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 在 **工作表** 中添加 **列**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **在工作表中插入列**
要在指定位置向工作表插入新列，请按照以下步骤执行:

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 向 **工作表** 中插入 **列** （通过指定要插入的列的索引位置）

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
