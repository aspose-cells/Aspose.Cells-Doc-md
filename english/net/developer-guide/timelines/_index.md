---
title: Insert Timeline
linktitle: Timelines
type: docs
weight: 170
url: /net/create-timeline/
description: Learn how to create a timeline with Aspose.Cells.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Instead of adjusting filters to show dates, you can use a PivotTable Timeline——a dynamic filter option that lets you easily filter by date/time, and zoom in on the period you want with a slider control. Microsoft Excel allows you to create timeline by selecting a pivot table and then clicking the *Insert > Timeline*. Aspose.Cells also allows you to create timeline using the [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index) method.

## **Create Timeline to a Pivot Table**

Please see the following sample code. It loads the [sample Excel file](input.xlsx) that contains the pivot table. It then creates the timeline based on the first base pivot field. Finally, it saves the workbook in [output XLSX](output.xlsx) format. The following screenshot shows the timeline created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

{{< app/cells/assistant language="csharp" >}}
