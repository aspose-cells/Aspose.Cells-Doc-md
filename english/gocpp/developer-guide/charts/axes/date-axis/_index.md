---
title: Date Axis with Golang via C++
linktitle: Date Axis
description: Learn how to manage the date axis in Aspose.Cells for Go via C++. Our guide will help you understand how to work with various date formats, time scales, and tick label frequencies.
keywords: Aspose.Cells for Go, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /go-cpp/date-axis/
---

## **Possible Usage Scenarios**
When you create a chart from worksheet data that uses dates, and the dates are plotted along the horizontal (category) axis in the chart, Aspose.Cells automatically changes the category axis to a date (time‑scale) axis.  
A date axis displays dates in chronological order at specific intervals or base units, such as the number of days, months, or years, even if the dates on the worksheet are not in sequential order or in the same base units.  
By default, Aspose.Cells determines the base units for the date axis based on the smallest difference between any two dates in the worksheet data. For example, if you have data for stock prices where the smallest difference between dates is seven days, Aspose.Cells sets the base unit to days, but you can change the base unit to months or years if you want to see the performance of the stock over a longer period of time.

## **Handle Date Axis Like Microsoft Excel**
Please see the following sample code, which creates a new Excel file and places the chart data in the first worksheet. Then we add a chart and set the type of the [**Axis**](https://reference.aspose.com/cells/go-cpp/axis/) to [**TimeScale**](https://reference.aspose.com/cells/go-cpp/categorytype/) and then set the base units to Days.

![todo:image_alt_text](excel.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DateAxis.go" >}}
{{< app/cells/assistant language="go" >}}
