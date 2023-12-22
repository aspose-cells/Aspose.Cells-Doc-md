---
title: Excel – R1C1 参考样式与 A1
type: docs
weight: 30
url: /zh/net/r1c1-reference-style-vs-a1/
description: R1C1参考风格VS。 A1 样式使用 Aspose.Cells for Python via .NET API。
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

在 Excel 中，R1C1 和 A1 是两种不同的引用样式，用于标识工作表中的单元格。请注意，A1 和 R1C1 之间的选择很大程度上取决于个人喜好。大多数用户更熟悉 A1 样式，但 R1C1 在某些情况下可能很有用，特别是在处理公式和计算时。

{{% /alert %}}

##  **A1参考样式**

这是 Excel 中的默认引用样式。在 A1 样式中，列由字母（A、B、C、...、Z、AA、AB、...、ZZ、AAA、AAB、...）标识，行由数字标识（1、 2、3、...）。
例如，第一列第二行的单元格称为A2。

##  **R1C1参考风格**

在R1C1风格中，行和列都由数字标识。字母“R”代表行号，字母“C”代表列号。例如，R2C1 指的是第二行第一列的单元格。

方括号中的任何数字均指距当前单元格的相对距离。与 A1 指的是列后跟行号不同，R1C1 则相反：行后跟列（这确实需要一些时间来适应）。正数将指下面和/或右侧的单元格。负数将指上方和/或左侧的单元格。

例如，R[2]C[3] 是向下 2 行、向右 3 列的单元格。 R[-1]C[-4] 是向上 1 行、向左 4 列的单元格。如果括号中没有显示数字，则您引用的是同一行或同一列，即 R[3]C 将是同一列中当前单元格下方 3 行的单元格。
<br>
<image src="2.png" width="70%" />

##  **R1C1参考样式和A1参考样式的比较**
这是一个快速比较：
|**A1风格**|**R1C1风格**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **如何在 R1C1 参考风格和 A1 参考风格之间切换**
您可以在 Excel 设置中在这些参考样式之间切换。要更改参考样式：

1. 转到“文件”选项卡。
1. 选择底部的“选项”。
1. 在“Excel 选项”对话框中，转到“公式”类别。
1. 在“使用公式”部分下，选中或取消选中“R1C1 参考样式”选项。
1. 单击“确定”应用更改。
<br>
<image src="1.png" width="70%" />

##  **如何在Excel中使用R1C1参考样式和A1参考样式**
以下示例演示如何以两种样式计算两个单元格值的总和。
<br>
A1参考样式：
<br>
<image src="4.png" width="70%" />

R1C1参考样式：
<br>
<image src="3.png" width="70%" />
