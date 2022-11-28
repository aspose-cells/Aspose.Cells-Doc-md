---
title: Date Axis
type: docs
weight: 200
url: /net/date-axis/
---

## **Possible Usage Scenarios**
When you create a chart from worksheet data that uses dates, and the dates are plotted along the horizontal (category) axis in the chart, Aspose.cells automatically changes the category axis to a date (time-scale) axis.
A date axis displays dates in chronological order at specific intervals or base units, such as the number of days, months, or years, even if the dates on the worksheet are not in sequential order or in the same base units.
By default, Aspose.cells determines the base units for the date axis based on the smallest difference between any two dates in the worksheet data.  For example, if you have data for stock prices where the smallest difference between dates is seven days, Excel sets the base unit to days, but you can change the base unit to months or years if you want to see the performance of the stock over a longer period of time.
## **Handle Primary and Second Axis like Microsoft Excel**
Please see the following sample code that create a new Excel file and put values of the chart in the first worksheet. 
Then we add a chart and set the type of the [**Axis**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
to [**TimeScale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) and then set the base units to Days.

![todo:image_alt_text](excel.png)
## **Sample Code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
