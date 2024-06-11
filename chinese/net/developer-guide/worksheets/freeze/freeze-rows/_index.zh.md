---
title: 冻结Excel工作表的最顶部行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/net/how-to-freeze-rows-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式冻结Excel工作表的顶部行。
keywords: 冻结顶部行，冻结顶部行。
---

{{% alert color="primary" %}}

在本文中，我们将学习如何冻结顶部行。
当您在常见标题下有大量数据时，在工作表向下滚动时将看不到标题。您可以冻结顶部行，这样即使其余数据正在滚动，您也可以看到冻结部分。您可以轻松地在顶部行中看到标题。

{{% /alert %}}

## **在Excel中冻结行**

**![在Excel中冻结顶部行](Freeze-Rows.png)**


1. 如果您想要冻结顶部行，则首先选择需要冻结的行下方的行
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单中，单击“冻结顶部行”。
4. 如果向下滚动，第一行始终处于顶部视图中。

**![冻结行](Frozen-Row.png)**

正如您所看到的，第一行已被冻结，当您向下滚动时，第一行始终保持在视图顶部。

冻结行使您能够查看大量数据，无需跟踪行标签。




## **使用Aspose.Cells for .Net冻结行**
使用Aspose.Cells for .Net很容易冻结行。 
请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法在所选行处冻结行。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一行。
3.保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

附有[示例源Excel文件](../Freeze.xlsx)。
