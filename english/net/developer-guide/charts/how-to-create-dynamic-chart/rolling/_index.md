---
title: How to create Dynamic Rolling Chart
description: Learn how to create a dynamic rolling chart using Aspose.Cells for .NET. Our guide will demonstrate how to implement smooth data transitions and rolling averages in your chart for a continuous and updated display.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /net/create-dynamic-rolling-chart/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A dynamic rolling chart refers to a graphical representation that displays data points constantly shifting and updating over time. It is a type of chart that continually updates itself, showcasing a rolling window of the most recent data points while discarding older data points as new ones come in.

Dynamic rolling charts are commonly used to visualize trends and patterns in real-time or streaming data. They are particularly useful in scenarios where temporal aspects and changes over time are critical, such as stock market analysis, weather monitoring, or live performance tracking.

These charts typically employ animation or auto-scrolling mechanisms to ensure the most up-to-date information is always presented. The length of the rolling window can be customized to show a specific time period, such as the last hour, day, or week.

In summary, a dynamic rolling chart is a continuously updated graphical representation that displays the latest data points while discarding older ones, allowing users to observe real-time trends and patterns.

## **Use Aspose Cells to create Dynamic Rolling Chart**
In the next paragraphs, we will show you how to create Dynamic Rolling Chart using Aspose.Cells. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

## **Notes**
In the generated file, you can continue to add data in columns A and B, while the chart dynamically counts the latest 5 sets of data. This is done using the "OFFSET" formula in the sample code:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

You can try changing the number "-5" to "-10" in the formula, and the dynamic chart will count the latest 10 sets of data. Now we have created a dynamic rolling chart using Aspose.Cells successfully.
{{< app/cells/assistant language="csharp" >}}
