---
title: Set the Values Format Code of Chart Series
description: Learn how to set the values format code of chart series in Aspose.Cells for Java. Our guide will help you understand how to format your chart series data using the appropriate format code, allowing you to present your data accurately and professionally.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Number Format
type: docs
weight: 100
url: /java/set-the-values-format-code-of-chart-series/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
You can set the values format code of chart series using the [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) method. This method is not only useful for series that are based on a range inside the worksheet but also works well for series created with an array of values.

## **Set the Values Format Code of Chart Series**
The following sample code adds a series to an empty chart that previously had no series. It adds the series using an array of values. After adding the series, it formats it with the code `$#,##0` using the [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) method, and the number `10000` becomes `$10,000`. The screenshot shows the effect of the code on the [sample Excel file](51740712.xlsx) and the [output Excel file](51740713.xlsx) after execution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
{{< app/cells/assistant language="java" >}}
