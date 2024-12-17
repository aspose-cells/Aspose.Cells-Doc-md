---
title: Copy Sparkline by Specifying Data Range and Location of Sparkline Group
type: docs
weight: 300
url: /python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel allows you to copy a sparkline by specifying the data range and location of a sparkline group. Aspose.Cells for Python via .NET supports this feature.

{{% /alert %}}

To copy a sparkline to other cells in Microsoft Excel:

1. Select the cell containing the sparkline.
1. Select **Edit Data** from the **Sparkline** section of the **Design** tab.
1. Select **Edit Group Location & Data**.
1. Specify the data range and location.
1. Click **OK**.

Aspose.Cells for Python via .NET provides the SparklineCollection.Add(dataRange, row, column) method to specify a sparkline group's data range and location. The following sample code loads the source Excel file as shown in the screenshot above, then accesses the first sparkline group and adds data ranges and locations in the sparkline group. Finally, it writes the output Excel file on disk which is also shown in the screenshot above.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

