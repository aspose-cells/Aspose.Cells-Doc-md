---
title: 冻结Excel工作表的顶行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/net/how-to-freeze-rows-of-excel-worksheet
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式冻结Excel工作表的顶行。
keywords: 冻结顶部行，冻结顶部行。
---

{{% alert color="primary" %}}

在本文中，我们将学习如何冻结顶部行。
当您有大量数据在一个共同的标题下时，当向下滚动工作表时无法看到标题。您可以冻结顶行，这样即使其余数据被滚动，您也可以看到已冻结的部分。您可以轻松查看顶部行中的标题。

{{% /alert %}}

## **在Excel中冻结行**

**![Excel中冻结顶部行](Freeze-Rows.png)**


1.如果要冻结顶部行，则首先选择需要被冻结的行下面的行
2. 单击“查看” > “冻结窗格”
3.在下拉菜单中，点击"冻结顶部行"。
4.如果向下滚动，则第一行始终在顶部视图中。

**![Fonzen row](Frozen-Row.png)**

通过看您可以看到，第一行是冻结的，第一行在向下滚动时始终保持在视图顶部。

冻结行让您在查看大量数据时无需跟踪行标签。




## **使用Aspose.Cells for .Net冻结行**
用Aspose.Cells for .Net很容易冻结行。 
请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)方法来冻结行。
1. 构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一行。
3. 保存文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

附上[示例源Excel文件](../Freeze.xlsx)。
