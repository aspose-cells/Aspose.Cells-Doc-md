---
title: 将十进制分隔符从数字键盘更改
type: docs
weight: 150
url: /zh/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb,decimal,十进制分隔符
description: 本文介绍了如何在GridWeb中更改小数分隔符。
---

## **可能的使用场景**
默认情况下，Aspose.Cells.GridWeb根据计算机上的区域设置以相应的方式显示数字数据。您可以使用Aspose.Cells.GridWeb API从数字键盘编程方式更改小数分隔符。因此，当文件导入到GridWeb矩阵中或者您通过数字键盘输入一些数值数据到新的工作表单元格时，它应该以您所需的小数分隔符进行可视化设置。 
## **从数字键盘更改小数分隔符**
使用**GridWorksheetCollection.NumberDecimalSeparator**属性，您可以从数字键盘编程方式更改小数分隔符。请参阅屏幕截图，展示了它的工作原理

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

请注意，小数分隔符的更改仅适用于GridWeb中用户的视觉体验。当您编辑并保存工作簿时，它将根据您的区域设置小数分隔符仍然存储数值（在电子表格中）。

{{% /alert %}}
