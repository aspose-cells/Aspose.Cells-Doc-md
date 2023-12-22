---
title: 应用高级条件格式
description: 如何使用 C# 中的 Aspose.Cells 库来应用高级条件格式。通过调整这些标准，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells, Advanced Conditional Formatting, C#, Conditional, Formatting
type: docs
weight: 70
url: /zh/net/apply-advanced-conditional-formatting/
---
{{% alert color="primary" %}} 

Microsoft Excel 2007 及更高版本 (2010/2013/2016) 提供了一些条件格式的高级功能。例如，它允许您应用单元格底纹、边框、彩色图标、箭头、标志和字体格式等，这些都变得相当复杂。

{{% /alert %}} 
##  **将高级条件格式应用于 Microsoft Excel 文件**
条件格式可以：

- 通过在单元格中嵌入简单的条形图，添加阴影数据条以图形方式增强基础数字。
- 根据单元格与范围内其他单元格中的值的关系，使用色标自动对单元格进行着色。默认设置将最低值显示为红色，将最高值显示为绿色。
- 使用图标集的方式与色标类似，但不是给单元格添加阴影，而是向单元格添加小图标，例如箭头和交通灯。

Aspose.Cells 完全支持 Microsoft Excel 2007 及更高版本在运行时以 XLSX 格式对单元格提供的条件格式。此示例演示了高级条件格式类型的练习，包括 IconSets、DataBars、Color Scales、TimePeriods、Top/Bottom 以及具有不同属性集的其他规则。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
###  **计算 Microsoft Excel 选择的颜色以进行 ColorScale 条件格式设置**
Aspose.Cells 允许您在模板文件中使用 ColorScale 条件格式时计算 Microsoft Excel 选择的颜色。请参阅下面的示例代码，了解如何计算 Microsoft Excel 选择的颜色。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
