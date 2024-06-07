---
title: 将图表转换为适合中国地区的图片
description: 了解如何使用 Aspose.Cells for .NET 设置图表的中国配置。我们的指南将演示如何配置图表以支持中文字符和格式，包括字体、大小、文本方向等。
keywords: Aspose.Cells for .NET，图表，中国配置，字体，字体大小，文本方向，支持。
linktitle: 设置中国区域
type: docs
weight: 9
url: /zh/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置中国地区。

{{% /alert %}}

## **定义一个继承类**

首先，您需要定义一个从 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) 继承的类 "ChartChineseSetttings"。 
然后，通过重写相关函数，您可以用您自己的语言设置图表元素的文本。
代码示例：
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **为图表配置中文设置**

在此步骤中，您将使用在上一步中定义的类 "ChartChineseSetttings"。
代码示例：

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

然后您可以在输出图像中看到效果，图表中的元素将根据您的设置渲染。

## **结论**

在这个示例中，如果您没有为图表设置中文区域，以下图表元素可能会以默认语言（如英语）呈现。
在上述操作之后，我们可以获得包含中文区域的输出图表图片。

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|
| :- | :- | :- |
|坐标轴标题名|坐标轴标题|Axis Title|
|轴单位名称|百,千...|Hundreds, Thousands...|
|图表标题名|图表标题|Chart Title|
|图例增加名|增加|Increase|
|图例减少名|减少|Decrease|
|图例总计名|汇总|Total|
|其他名|其他|Other|
|系列名|系列|Series|
