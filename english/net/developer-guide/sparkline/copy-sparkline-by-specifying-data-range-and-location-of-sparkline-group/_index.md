---
title: Copy Sparkline by Specifying Data Range and Location of Sparkline Group
type: docs
weight: 300
url: /net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel allows you to copy a sparkline by specifying the data range and location of a sparkline group. Aspose.Cells supports this feature.

{{% /alert %}}

To copy a sparkline to other cells in Microsoft Excel:

1. Select the cell containing the sparkline.  
2. Select **Edit Data** from the **Sparkline** section of the **Design** tab.  
3. Select **Edit Group Location & Data**.  
4. Specify the data range and location.  
5. Click **OK**.

Aspose.Cells provides the `SparklineCollection.Add(dataRange, row, column)` method to specify a sparkline group's data range and location. The following sample code loads the source Excel file as shown in the screenshot above, then accesses the first sparkline group and adds data ranges and locations to the sparkline group. Finally, it writes the output Excel file on disk, which is also shown in the screenshot above.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
