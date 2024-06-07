---
title: 重命名工作表
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/rename-worksheet/
keywords: GridWeb，rename，重命名工作表，重命名GridWorksheet
description: 本文介绍了如何在GridWeb中重命名工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

在使用Aspose.Cells.GridWeb处理许多工作表并决定更改它们的名称以使其更有意义时，重命名工作表可能非常有用。例如，包含发票的工作表可以被重命名为Invoice，而不是Sheet1。本主题描述了这个简单但有用的功能。

{{% /alert %}} 
## **重命名工作表**
所有工作表都包含一个允许开发人员访问或修改工作表名称的Name属性。

1. 从GridWorksheetCollection访问工作表。
1. 重命名所选工作表。



{{% alert color="primary" %}} 

有关如何访问Aspose.Cells.GridWeb中的工作表的更多详细信息，请参阅【访问工作表】(/cells/zh/net/aspose-cells-gridweb/access-worksheets/)。

{{% /alert %}} 

在执行代码之前，工作表具有默认名称，如Sheet1。

**输入文件：工作表具有默认名称Sheet1** 

![todo:image_alt_text](rename-worksheets_1.png)

运行代码后，工作表将被命名为Students。

**输出：工作表被命名为Students** 

![todo:image_alt_text](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
