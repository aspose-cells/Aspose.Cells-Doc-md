---
title: 如何获取图表中对象的位置
description: 学习如何使用Aspose.Cells for .NET获取Excel图表中的对象位置 
keywords: Aspose.Cells for .NET, Excel 图表, 获取对象位置。
type: docs
weight: 74
url: /zh/net/how-to-get-object-position-in-chart/
---

## 可能的使用场景
在某些情况下，当你使用Excel图表时，可能需要获取图表中对象的位置。你可以轻松使用Aspose.Cells实现此需求。

## 示例：获取图表中对象的位置

以下示例代码加载[示例Excel文件](TestFile.xlsx)并生成[输出Excel文件](Output.xlsx)。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

通过上述代码，你可以获得图表标题和图表 PlotArea 的位置。 
借助位置信息，可以在图表中将形状放置在对应位置。 
输出结果如下图所示，一个形状被放在PlotArea的左上角，另一个形状放在图表标题下方。
![todo:image_alt_text](OutputResult.png)

## 单位说明与转换

图表中对象位置有以下三种单位：

1. 图表区域的比例单位。

2. 图表区域的1/4000单位。这是在旧版本Excel文件中使用的单位，不建议使用。

3. 像素单位。

它们的转换代码如下： 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
