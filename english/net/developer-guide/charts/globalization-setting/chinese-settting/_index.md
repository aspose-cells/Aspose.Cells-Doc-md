---
title: Convert Chart to Image for Chinese Region
description: Learn how to use Aspose.Cells for .NET sets Chinese configuration for charts. Our guide will demonstrate how to configure charts to support Chinese characters and formats, including fonts, sizes, text directions, and more.
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: Set Chinese Region
type: docs
weight: 9
url: /net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In this topic, we will show you how to set Chinese Region for a chart.

{{% /alert %}}

## **Defines an inheritance class**

First step, you need to define a class "ChartChineseSetttings" that inherit from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Then, by rewriting the related functions, you can set the text of the chart elements in your own language.
Code example:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Config Chinese Setting For Chart**

In this step, you will use the class "ChartChineseSetttings" you defined in the previous step.
Code example:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.

## **Conclusion**

In this example, if you do not set Chinese Region for a chart, the following chart elements may be rendered in the default language, such as English.
After the above operation, we can get an output chart picture with Chinese Region.

|**Supported elements**|**Value in this example**|**default value in the English environment**|
| :- | :- | :- |
|Axis Title Name|坐标轴标题|Axis Title|
|Axis Unit Name|百,千...|Hundreds, Thousands...|
|Chart Title Name|图表标题|Chart Title|
|Legend Increase Name|增加|Increase|
|Legend Decrease Name|减少|Decrease|
|Legend Total Name|汇总|Total|
|Other Name|其他|Other|
|Series Name|系列|Series|
