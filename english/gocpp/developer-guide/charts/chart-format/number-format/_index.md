---
title: Set the Values Format Code of Chart Series with Golang via C++
linktitle: Number Format
type: docs
weight: 100
url: /go-cpp/set-the-values-format-code-of-chart-series/
description: Learn how to set the values format code of chart series in Aspose.Cells for C++. Our guide will help you understand how to format your chart series data using the appropriate format code, allowing you to present your data accurately and professionally.
keywords: Aspose.Cells for C++, chart series, values format code, formatting, data presentation, accuracy, professionalism.
---

## **Possible Usage Scenarios**
You can set the values format code of chart series using the [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) property. This property is not only useful for the series which is based on the range inside the worksheet but also works well for the series created with an array of values.

## **Set the Values Format Code of Chart Series**
The following sample code adds a series in the empty chart which has no series before. It adds the series using the array of values. Once, it adds the series, it formats it with the code `$#,##0` using the [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) property and the number `10000` becomes `$10,000`. The screenshot shows the effect of code on the [sample Excel file](51740712.xlsx) and [output Excel file](51740713.xlsx) after execution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-NumberFormat.go" >}}