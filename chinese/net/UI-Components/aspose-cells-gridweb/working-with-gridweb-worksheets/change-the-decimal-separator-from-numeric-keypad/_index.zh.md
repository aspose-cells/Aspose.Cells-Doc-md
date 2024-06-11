---
title: 从数字键盘更改小数分隔符
type: docs
weight: 150
url: /zh/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb、小数、小数分隔符
description: 本文介绍了如何在 GridWeb 中更改小数分隔符。
---

## **可能的使用场景**
默认情况下，根据计算机上的区域设置，Aspose.Cells.GridWeb 会相应地显示数字数据。您可以使用 Aspose.Cells.GridWeb API 从数字键盘通过编程方式更改小数分隔符。因此，当将文件导入 GridWeb 矩阵或在新的工作表单元格中输入一些数字数据（从数字键盘），它应该在视觉上显示您所需的小数分隔符。 
## **从数字键盘更改小数分隔符**
使用 **GridWorksheetCollection.NumberDecimalSeparator** 属性，您可以通过编程方式从数字键盘更改小数分隔符。请查看显示其工作方式的截图

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

请注意，小数分隔符更改仅用于用户在 GridWeb 中的视觉体验。当您编辑和保存工作簿时，它仍会根据您的区域设置小数分隔符将数字值（在电子表格中）存储。

{{% /alert %}}
