---
title: 将中国地区的图表转换为图像
description: 了解如何使用 Aspose.Cells for .NET 设置图表的中文配置。我们的指南将演示如何配置图表以支持中文字符和格式，包括字体、大小、文本方向等。
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: 设置中国地区
type: docs
weight: 9
url: /zh/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置中国区域。

{{% /alert %}}

##  **定义一个继承类**

第一步，需要定义一个类“ChartChineseSetttings”，继承自[**图表全球化设置**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
然后，通过重写相关函数，您可以用自己的语言设置图表元素的文本。
代码示例：
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **配置图表中文设置**

在此步骤中，您将使用在上一步中定义的类“ChartChineseSetttings”。
代码示例：

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

然后您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

##  **结论**

在本例中，如果您没有为图表设置中文区域，则以下图表元素可能会以默认语言呈现，例如英语。
经过上面的操作，我们就可以得到一个带有中文区域的输出图表图片了。

|**支持的元素**|**本例中的值**|**英文环境下的默认值**|
| :- | :- | :- |
|轴标题名称|坐标轴标题|轴标题|
|轴单位名称|百,千...|数百、数千……|
|图表标题名称|图表标题|图表标题|
|图例增加名称|增加|增加|
|图例 减少名称|减少|减少|
|图例 总名称|汇总|全部的|
|其他名字|其他|其他|
|系列名称|系列|系列|
