---
title: How to do Japanese Setting for Chart
linktitle: Japanese Setting
type: docs
weight: 50
url: /net/do-japanese-setting-for-chart/
---

{{% alert color="primary" %}}

In this topic, we will show you how to do japanese setting for a chart.

{{% /alert %}}

## **Defines an inheritance class**

First step, you need to define a class "ChartJapaneseSetttings" that inherit from Aspose.Cells.ChartsChartGlobalizationSettings. Code example:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Config Japanese Setting For Chart**

Code example:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.


