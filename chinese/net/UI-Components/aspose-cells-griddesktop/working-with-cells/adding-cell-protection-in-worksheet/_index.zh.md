---
title: 在工作表中添加保护
type: docs
weight: 130
url: /zh/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop, 保护
description: 本文介绍如何在GridDesktop的工作表中保护单元格。
---

{{% alert color="primary" %}} 

Aspose.Cells for GridDesktop允许您在工作表中保护单元格。首先需要保护工作表，然后可以保护工作表中所需的单元格。为了保护工作表，请将Worksheet.Protected属性设置为true，然后使用Worksheet.SetProtected()方法保护单元格范围。

{{% /alert %}} 
## **使用Aspose.Cells.GridDesktop保护单元格**
以下示例代码保护了GridDesktop活动工作表中范围A1:B1中的所有单元格。当您双击此范围内的任何单元格时，您将无法编辑它们。这将使这些单元格为只读。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
