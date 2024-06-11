---
title: 将图表转换为中国区域的图像
description: 学习如何使用 Aspose.Cells for .NET 设置图表的中文配置。我们的指南将演示如何配置图表以支持中文字符和格式，包括字体、大小、文本方向等。
keywords: Aspose.Cells for .NET, 图表, 中文配置, 字体, 字体大小, 文本方向, 支持。
linktitle: 设置中国区域
type: docs
weight: 9
url: /zh/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置中国区域。

{{% /alert %}}

## **定义继承类**

第一步，您需要定义一个从 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) 继承的类 "ChartChineseSetttings"。 
然后，通过重写相关函数，您可以将图表元素的文本设置为您自己的语言。
代码示例:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **为图表配置中文设置**

在这一步，您将使用在前一步中定义的类 "ChartChineseSetttings"。
代码示例:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

## **结论**

在这个示例中，如果不为图表设置中国区域，则以下图表元素可能以默认语言（例如英语）渲染。
在上述操作之后，我们可以获得一个带有中国区域的输出图表图片。

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|
| :- | :- | :- |
|轴标题名称|坐标轴标题|Axis Title|
|轴单位名称|百,千...|Hundreds, Thousands...|
|图表标题|图表标题|
|增加|增加|
|减少|减少|
|汇总|汇总|
|其他|其他|
|系列|系列|
