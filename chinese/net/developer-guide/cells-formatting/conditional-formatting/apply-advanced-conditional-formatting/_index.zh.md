---
title: 应用高级条件格式
description: 如何在C#中使用Aspose.Cells库应用高级条件格式。通过调整这些条件，您可以更好地控制单元格的外观。
keywords: Aspose.Cells, 高级条件格式, C#, 条件, 格式
type: docs
weight: 70
url: /zh/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

Microsoft Excel 2007及更高版本（2010/2013/2016）为条件格式提供了一些高级功能。例如，它允许您应用单元格底纹、边框、彩色图标、箭头、标志和字体格式等，这些已经变得相当复杂。

{{% /alert %}} 
## **向Microsoft Excel文件应用高级条件格式**
条件格式可以:

- 通过在单元格中嵌入简单条形图来以图形方式增强底层数字，添加有阴影的数据条。
- 根据范围中其他单元格的值之间的关系自动使用颜色标度着色单元格。默认设置将最低值着为红色，并向上移动至用绿色着色的最高值。
- 与颜色标度类似，使用图标集，但与着色单元格不同，它向单元格添加小图标，例如箭头和交通灯。

Aspose.Cells完全支持Microsoft Excel 2007及更高版本在运行时对XLSX格式的单元格提供的条件格式。此示例展示了高级条件格式类型的练习，包括图标集、数据条、颜色标度、时间段、最高/最低等规则，并具有不同组属性。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
### **计算 Microsoft Excel 选择的ColorScale条件格式的颜色**
Aspose.Cells允许您计算模板文件中使用ColorScale条件格式时Microsoft Excel选择的颜色。查看下面的示例代码，了解如何计算Microsoft Excel选择的颜色。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
