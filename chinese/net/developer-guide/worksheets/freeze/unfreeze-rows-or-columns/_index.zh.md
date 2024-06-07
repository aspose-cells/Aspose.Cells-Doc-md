---
title: 解冻行或列
linktitle: 取消拆分窗格
type: docs
weight: 190
url: /zh/net/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式解冻Excel工作表的行、列或窗格。
keywords: 解冻窗格、解冻行、解冻列、解冻窗口。
---

{{% alert color="primary" %}}

在本文中，我们将学习如何解冻行、列和窗格。
如果Excel文件中的工作表被冻结，有时我们想要解冻工作表或调整冻结的行、列或窗格。

{{% /alert %}}

## **在Excel中**

1. 单击“查看”选项卡 > “冻结窗格” > “取消冻结窗格”。

**![Excel中解冻窗格](Unfreeze-Panes.png)**




## **使用Aspose.Cells for .Net解冻行、列或窗格非常简单。请使用{0}方法来解冻窗格。**
1. 构建要打开的冻结文件的工作簿。

2. 使用Worksheet.UnFreezePanes()方法解冻窗格。
2. 使用Worksheet.UnFreezePanes()方法取消冻结窗格。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

附上[示例源Excel文件](Frozen.xlsx)。
