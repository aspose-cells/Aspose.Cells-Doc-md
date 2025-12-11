---
title: Convert Chart to Localized Image
description: Learn how to set globalization configurations for charts using Aspose.Cells for .NET. Our guide demonstrates how to configure the chart to support multiple languages and regional formats to correctly display text, dates, and numbers in different languages.
keywords: Aspose.Cells for .NET, Charts, Globalization Settings, Multiple Languages, Regional Formats, Display, Text, Dates, Numbers.
linktitle: Set Localized Region
type: docs
weight: 50
url: /net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In this topic, we will show you how to convert a chart to a localized image; you will learn how to set a localized region for a chart.

{{% /alert %}}

## **Scenario**

In what scenario would we need to set a localized region for a chart?

When you open an XLSX file with a chart in Excel, suppose you open it with a Spanish regional setting, you can see the elements in the chart area, such as Chart Title and Legend, translated into Spanish. But when you save this chart as a picture with Aspose.Cells, you may encounter the following issue:

**![Global Issue](GlobalIssue.png)**

In this scenario, the Chart Legend in the output picture is not the same as in Excel; it remains displayed in English by default. You can solve this issue by setting a localized region for the chart. With the correct settings, the following elements will be rendered according to your localization settings.

## **Supported elements**

The following elements in a chart can be rendered according to your localization settings.

| **Supported elements** | **Default value in the English environment** |
| :- | :- |
| Axis Title Name | Axis Title |
| Axis Unit Name | Hundreds, Thousands… |
| Chart Title Name | Chart Title |
| Legend Increase Name | Increase |
| Legend Decrease Name | Decrease |
| Legend Total Name | Total |
| Other Name | Other |
| Series Name | Series |

## **Operation Steps**

The following example will show you in detail how to set a localized region to achieve the desired effect.

- [How to Set Chinese Region for Chart](/cells/net/convert-chart-to-image-for-chinese-region/)
- [How to Set Japanese Region for Chart](/cells/net/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="csharp" >}}
