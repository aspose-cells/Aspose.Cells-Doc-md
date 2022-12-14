---
title: 从数字键盘更改小数点分隔符
type: docs
weight: 150
url: /zh/net/change-the-decimal-separator-from-numeric-keypad/
---
## **可能的使用场景**
默认情况下，Aspose.Cells.GridWeb 根据计算机上的区域设置相应地显示数字数据。您可以使用 Aspose.Cells.GridWeb API 以编程方式更改数字小键盘的小数分隔符。因此，当将文件导入 GridWeb 矩阵或将一些数字数据（从数字小键盘）输入新的工作表单元格时，它应该有您想要的小数点可视化设置分隔符。
## **从数字键盘更改小数点分隔符**
使用**GridWorksheetCollection.NumberDecimalSeparator**属性，您可以通过编程方式从数字键盘更改小数点分隔符。请查看显示其工作原理的屏幕截图

![待办事项：图片_替代_文本](change-the-decimal-separator-from-numeric-keypad_1.png)

![待办事项：图片_替代_文本](change-the-decimal-separator-from-numeric-keypad_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

请注意，小数分隔符更改仅用于用户在 GridWeb 中的视觉体验。当您编辑和保存工作簿时，它仍会按照您的语言环境/区域小数点分隔符存储数值（在电子表格中）。

{{% /alert %}}
