---
title: Set the Values Format Code of Chart Series
type: docs
weight: 60
url: /java/set-the-values-format-code-of-chart-series/
---

## **Possible Usage Scenarios**

You can set the values format code of chart series using the [**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode) property. This property is not only useful for the series which are based on the range inside the worksheet but also works well for the series created with an array of values.

## **Set the Values Format Code of Chart Series**

The following sample code adds a series in the empty chart which has no series before. It adds the series using the array of values. Once, it adds the series, it formats it with the code $#,##0 using the [**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode) property and the number 10000 becomes $10,000. The screenshot shows the effect of code on the [sample Excel file](51740736.xlsx) and [output Excel file](51740735.xlsx) after execution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-SetValuesFormatCodeOfChartSeries.java" >}}
