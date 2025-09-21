---
title: Copy Sparkline by Specifying Data Range and Location of Sparkline Group with Golang via C++
linktitle: Copy Sparkline by Specifying Data Range and Location
type: docs
weight: 300
url: /go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Learn how to copy sparklines by specifying data range and location using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel allows you to copy a sparkline by specifying the data range and location of a sparkline group. Aspose.Cells supports this feature.

{{% /alert %}}

To copy a sparkline to other cells in Microsoft Excel:

1. Select the cell containing the sparkline.
1. Select **Edit Data** from the **Sparkline** section of the **Design** tab.
1. Select **Edit Group Location & Data**.
1. Specify the data range and location.
1. Click **OK**.

Aspose.Cells provides the `SparklineCollection.Add(dataRange, row, column)` method to specify a sparkline group's data range and location. The following sample code loads the source Excel file as shown in the screenshot above, then accesses the first sparkline group and adds data ranges and locations in the sparkline group. Finally, it writes the output Excel file on disk which is also shown in the screenshot above.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}