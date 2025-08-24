---
title: How to create Dynamic Rolling Chart with Golang via C++
linktitle: How to create Dynamic Rolling Chart
description: Learn how to create a dynamic rolling chart using Aspose.Cells for C++. Our guide will demonstrate how to implement smooth data transitions and rolling averages in your chart for a continuous and updated display.
keywords: Aspose.Cells for C++, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /go-cpp/create-dynamic-rolling-chart/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-Rolling.go" >}}
## **Notes**
In the generated file, you can continue to add data in columns A and B, while the chart dynamically counts the latest 5 sets of data. This is done using the "OFFSET" formula in the sample code:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-Rolling-1.go" >}}
You can try changing the number "-5" to "-10" in the formula, and the dynamic chart will count the latest 10 sets of data. Now we have created a dynamic rolling chart using Aspose.Cells successfully.