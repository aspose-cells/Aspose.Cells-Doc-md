---
title: Convert Chart to Localized Image with C++
description: Learn how to set globalization configurations for charts using Aspose.Cells for C++. Our guide demonstrates how to configure the chart to support multiple languages and regional formats to correctly display text, dates, and numbers in different languages.
keywords: Aspose.Cells for C++, Charts, Globalization Settings, Multiple Languages, Regional Formats, Display, Text, Dates, Numbers.
linktitle: Set Localized Region
type: docs
weight: 50
url: /cpp/convert-chart-to-localized-image/
alias: [/cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

In this topic, we will show you how to convert chart to localized image, you will know how to set localized region for a chart.

{{% /alert %}}

## **Scenario**

In what scenario would we need to set localized region for a chart?

When you open an xlsx file with a chart in Excel, in this case, suppose you open it with a Spanish Regional Setting in Excel, you can see the elements in the chart area, such as Chart Title and Legend, translated into Spanish. But when you save this chart as a picture with Aspose.Cells, you may encounter the following issue: 

**![Global Issue](GlobalIssue.png)**

In this scenario, the Chart Legend in the output picture is not the same as in Excel; it remains displayed in English by default. Now you can solve this issue by setting localized region for the chart. With the correct settings, the following elements will be rendered according to your localization settings.

## **Supported elements**

The following elements in the chart can be rendered according to your localization settings.

|**Supported elements**|**default value in the English environment**|
| :- | :- |
|Axis Title Name|Axis Title|
|Axis Unit Name|Hundreds, Thousands...|
|Chart Title Name|Chart Title|
|Legend Increase Name|Increase|
|Legend Decrease Name|Decrease|
|Legend Total Name|Total|
|Other Name|Other|
|Series Name|Series|

## **Operation Steps**

The following example will show you in detail how to set localized region to achieve the effect you want.

- [How to Set Chinese Region for Chart](/cells/cpp/convert-chart-to-image-for-chinese-region/)
- [How to Set Japanese Region for Chart](/cells/cpp/convert-chart-to-image-for-japanese-region/)

