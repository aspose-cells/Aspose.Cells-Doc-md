---
title: Convert Chart to Localized Image with Python via .NET
linktitle: Set Localized Region
type: docs
weight: 50
url: /python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Learn how to set globalization configurations for charts using Aspose.Cells for Python via .NET. Configure charts to support multiple languages and regional formats for correct display of text, dates, and numbers.
keywords: Aspose.Cells for Python via .NET, Charts, Globalization Settings, Multiple Languages, Regional Formats, Display, Text, Dates, Numbers.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In this topic, we will show you how to convert a chart to a localized image and how to set the localized region for a chart.

{{% /alert %}}

## **Scenario**

When might you need to set the localized region for a chart?

If you open an XLSX file containing a chart in Excel with Spanish regional settings, elements like the chart title and legend appear in Spanish. However, saving this chart as an image using Aspose.Cells might result in these elements remaining in English by default:

**![Global Issue](GlobalIssue.png)**

This occurs because the chart legend in the output image doesn't match Excel's localization. You can resolve this by configuring the chart's localized region settings.

## **Supported Elements**

The following chart elements will render according to your localization settings:

| **Supported Elements**      | **Default Value (English)**       |
|-----------------------------|-----------------------------------|
| Axis Title Name             | Axis Title                        |
| Axis Unit Name              | Hundreds, Thousands...           |
| Chart Title Name            | Chart Title                       |
| Legend Increase Name        | Increase                          |
| Legend Decrease Name        | Decrease                          |
| Legend Total Name           | Total                             |
| Other Name                  | Other                             |
| Series Name                 | Series                            |

{{< app/cells/assistant language="python-net" >}}
