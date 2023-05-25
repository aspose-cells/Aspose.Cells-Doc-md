---
title: 解冻行或列
linktitle: 解冻窗格
type: docs
weight: 190
url: /zh/net/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用 C# 库和 .NET API 以编程方式解冻 Excel 工作表的行、列或窗格。
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

在本文中，我们将学习如何解冻行、列和窗格。
如果 Excel 文件中的工作表被冻结，有时我们想解冻它或调整冻结的行、列或窗格。

{{% /alert %}}

##  **在 Excel 中**

1. 单击视图选项卡 > 冻结窗格 > 解冻窗格。

**![在 Excel 中解冻窗格](Unfreeze-Panes.png)**




##  **使用 Aspose.Cells for .Net 解冻行、列或窗格**
使用 Aspose.Cells for .Net 解冻窗格很简单。请使用[**工作表.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)unfeeze 窗格的方法。

1. 构造工作簿以打开冻结的文件。
2. 使用 Worksheet.UnFreezePanes() 方法解冻窗格。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

随附的[示例源 Excel 文件](Frozen.xlsx).
