---
title: Set the Values Format Code of Chart Series
type: docs
weight: 100
url: /net/set-the-values-format-code-of-chart-series/
---

## **Possible Usage Scenarios**
You can set the values format code of chart series using the [Series.ValuesFormatCode](https://apireference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) property. This property is not only useful for the series which is based on the range inside the worksheet but also works well for the series created with an array of values.
## **Set the Values Format Code of Chart Series**
The following sample code adds a series in the empty chart which has no series before. It adds the series using the array of values. Once, it adds the series, it formats it with the code $#,##0 using the [Series.ValuesFormatCode](https://apireference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) property and the number 10000 becomes $10,000. The screenshot shows the effect of code on the [sample Excel file](51740712.xlsx) and [output Excel file](51740713.xlsx) after execution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
