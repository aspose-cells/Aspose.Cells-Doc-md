---
title: 冻结Excel工作表的最顶部行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/python-net/how-to-freeze-rows-of-excel-worksheet
description: 在本文中，您将学习如何使用Aspose.Cells for Python via .NET API对Excel工作表的顶部行进行冻结。
keywords: Python Excel库, Python冻结顶部行
---

## **介绍**

在本文章中，我们将学习如何冻结顶部行。当您在一行下有大量共同标题的数据时，向下滚动工作表时，您无法看到标题。您可以冻结顶部行，以便在其余数据被滚动时仍然可以看到该冻结部分。您可以轻松看到顶部行的标题。

## **如何在Excel中冻结行**

**![在Excel中冻结顶部行](Freeze-Rows.png)**


1. 如果您想要冻结顶部行，则首先选择需要冻结的行下方的行
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单中，单击“冻结顶部行”。
4. 如果向下滚动，第一行始终处于顶部视图中。

**![冻结行](Frozen-Row.png)**

正如您所看到的，第一行已被冻结，当您向下滚动时，第一行始终保持在视图顶部。

冻结行使您能够查看大量数据，无需跟踪行标签。




## **使用Aspose.Cells for Python Excel库冻结行的方法**
使用Aspose.Cells for Python via .NET，很容易冻结行。请使用[**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)方法在所选行上冻结行。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一行。
3.保存文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Row.py" >}}

附有[示例源Excel文件](../Freeze.xlsx)。
