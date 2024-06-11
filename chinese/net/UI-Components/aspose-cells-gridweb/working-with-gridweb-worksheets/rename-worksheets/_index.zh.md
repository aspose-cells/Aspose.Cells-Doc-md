---
title: 重命名工作表
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/rename-worksheet/
keywords: GridWeb,重命名,重命名工作表,重命名 GridWorksheet
description: 本文介绍了如何在GridWeb中重命名工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

在使用Aspose.Cells.GridWeb时，重命名工作表可能会非常有用，当决定更改它们的名称以使其更加有意义时。例如，包含发票的工作表可以将其重命名为Invoice，而不是Sheet1。本主题描述了这个简单但十分有用的功能。

{{% /alert %}} 
## **重命名工作表**
所有工作表都包含一个Name属性，允许开发人员访问或修改工作表的名称。要重命名工作表：

1. 从GridWorksheetCollection中访问工作表。
1. 重命名选定的工作表。



{{% alert color="primary" %}} 

有关如何在Aspose.Cells.GridWeb中访问工作表的更多详细信息，请参阅[访问工作表](/cells/zh/net/aspose-cells-gridweb/access-worksheets/)。

{{% /alert %}} 

在执行代码之前，工作表具有默认名称，如Sheet1。

**输入文件：具有默认名称Sheet1的工作表** 

![todo:image_alt_text](rename-worksheets_1.png)

运行代码后，工作表重命名为Students。

**输出：工作表已重命名为Students** 

![todo:image_alt_text](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
