---
title: Convert Chart to Image for Japanese Region
description: Learn how to use Aspose.Cells for .NET sets the Japanese configuration for the chart. Our guide will demonstrate how to configure charts to support Japanese characters and formatting, including fonts, size, text direction, and more.
keywords: Aspose.Cells for .NET, Charts, Japanese configuration, font, font size, text direction, support.
linktitle: Set Japanese Region
type: docs
weight: 10
url: /net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In this topic, we will show you how to set Japanese Region for a chart.

{{% /alert %}}

## **Defines an inheritance class**

First step, you need to define a class "ChartJapaneseSetttings" that inherit from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Then, by rewriting the related functions, you can set the text of the chart elements in your own language.
Code example:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Config Japanese Setting For Chart**

In this step, you will use the class "ChartJapaneseSetttings" you defined in the previous step.
Code example:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.

## **Conclusion**

In this example, if you do not set Japanese Region for a chart, the following chart elements may be rendered in the default language, such as English.
After the above operation, we can get an output chart picture with Japanese Region.

|**Supported elements**|**Value in this example**|**default value in the English environment**|
| :- | :- | :- |
|Axis Title Name|軸タイトル|Axis Title|
|Axis Unit Name|百,千...|Hundreds, Thousands...|
|Chart Title Name|グラフ タイトル|Chart Title|
|Legend Increase Name|ぞうか|Increase|
|Legend Decrease Name|削減|Decrease|
|Legend Total Name|すべての|Total|
|Other Name|その他|Other|
|Series Name|シリーズ|Series|
{{< app/cells/assistant language="csharp" >}}
