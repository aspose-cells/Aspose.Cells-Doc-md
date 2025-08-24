---
title: How to Create Dynamic Scrolling Chart with Golang via C++
linktitle: Create Dynamic Scrolling Chart
description: Learn how to create a dynamic scrolling chart using Aspose.Cells for C++. Our step-by-step guide will demonstrate how to implement smooth data transitions and automatic scrolling in your chart for a continuous and updated display.
keywords: Aspose.Cells for C++, Dynamic Scrolling Chart, Data Transitions, Smooth Scrolling, Continuous Display, Updating Visualization.
type: docs
weight: 75
url: /go-cpp/create-dynamic-scrolling-chart/
---

## **Possible Usage Scenarios**
Dynamic scrolling chart is a type of graphical representation used to display data that changes over time. It is designed to provide a real-time view of data, allowing users to track continuous updates and trends. The chart continuously updates itself as new data is added, and it automatically scrolls to show the most recent information.

Dynamic scrolling charts are commonly used in various industries, such as finance, stock market analysis, weather tracking, and social media analytics. They enable users to visualize and analyze data patterns and make informed decisions based on real-time information.

These charts are typically interactive, allowing the user to zoom in or out, scroll through historical data, and adjust time intervals. They often support multiple data series, providing a comprehensive view of different metrics and their correlations.

Overall, dynamic scrolling charts are valuable tools for monitoring and analyzing time-series data, facilitating real-time decision-making and enhancing data visualization capabilities.

## **Use Aspose Cells to Create Dynamic Scrolling Chart**
In the next paragraphs, we will show you how to create a Dynamic Scrolling Chart using Aspose.Cells. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Scrolling Chart File](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-Scrolling.go" >}}
## **Notes**
In the generated file, you can operate on the scroll bar, while the chart dynamically counts the latest 10 sets of data. This is done using the "OFFSET" formula in the sample code:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-Scrolling-1.go" >}}
You can try changing the number "10" to "15" in cell "Sheet1!$H$20", and the dynamic chart will count the latest 15 sets of data. Now we have created a dynamic scrolling chart using Aspose.Cells successfully.