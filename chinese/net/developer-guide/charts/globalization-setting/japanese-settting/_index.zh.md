---
title: 将图表转换为针对日本地区的图像
description: 学习如何使用 Aspose.Cells for .NET 设置图表的日文配置。我们的指南将演示如何配置图表以支持日文字符和格式，包括字体、大小、文本方向等。
keywords: Aspose.Cells for .NET, 图表, 日文配置, 字体, 字体大小, 文本方向, 支持。
linktitle: 设置日本地区
type: docs
weight: 10
url: /zh/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置日本地区。

{{% /alert %}}

## **定义继承类**

首先，您需要定义一个从[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)继承的类"ChartJapaneseSetttings"。 
然后，通过重写相关函数，您可以将图表元素的文本设置为您自己的语言。
代码示例:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **为图表配置日本设置**

在这一步中，您将使用在上一步中定义的"ChartJapaneseSetttings"类。
代码示例:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

## **结论**

在此示例中，如果不为图表设置日本地区，则以下图表元素可能以默认语言（如英文）呈现。
在上述操作后，我们可以获得一个具有日本区域的输出图表图片。

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|
| :- | :- | :- |
|轴标题名称|軸タイトル|Axis Title|
|轴单位名称|百,千...|Hundreds, Thousands...|
|图表标题名称|グラフ タイトル|Chart Title|
|图例增加名称|ぞうか|Increase|
|图例减少名称|削減|Decrease|
|图例总数名称|すべての|Total|
|其它名称|その他|Other|
|系列名称|シリーズ|Series|
