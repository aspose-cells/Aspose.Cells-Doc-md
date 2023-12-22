---
title: 将日本地区的图表转换为图像
description: 了解如何使用 Aspose.Cells for .NET 设置图表的日语配置。我们的指南将演示如何配置图表以支持日语字符和格式，包括字体、大小、文本方向等。
keywords: Aspose.Cells for .NET, Charts, Japanese configuration, font, font size, text direction, support.
linktitle: 设置日本地区
type: docs
weight: 10
url: /zh/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置日本区域。

{{% /alert %}}

##  **定义一个继承类**

第一步，您需要定义一个继承自的类“ChartJapanSetttings”[**图表全球化设置**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
然后，通过重写相关函数，您可以用自己的语言设置图表元素的文本。
代码示例：
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **配置图表的日语设置**

在此步骤中，您将使用在上一步中定义的类“ChartJapanSetttings”。
代码示例：

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

然后您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

##  **结论**

在此示例中，如果您未为图表设置日语区域，则以下图表元素可能会以默认语言（例如英语）呈现。
经过上述操作后，我们就可以得到一张带有日本地区的输出图表图片。

|**支持的元素**|**本例中的值**|**英文环境下的默认值**|
| :- | :- | :- |
|轴标题名称|軸タイトル|轴标题|
|轴单位名称|百,千...|数百、数千……|
|图表标题名称|グラフ タイトル|图表标题|
|图例增加名称|ぞうか|增加|
|图例 减少名称|削減|减少|
|图例 总名称|すべての|全部的|
|其他名字|その他|其他|
|系列名称|シリーズ|系列|
