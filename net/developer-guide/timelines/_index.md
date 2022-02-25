---
title: Insert Timeline
linktitle: Timelines
type: docs
weight: 170
url: /net/create-timeline/
aliases: [/net/timelines/,/net/create-timeline-to-a-pivot-table/]
description: Manage timelines of Excel files with Aspose.Cells.
---

## **Possible Usage Scenarios**

A timeline is used to filter data quickly. It can be used to filter data in a pivot table. Microsoft Excel allows you to create timeline by selecting a pivot table and then clicking the *Insert > Timeline*. Aspose.Cells also allows you to create timeline using the [**Worksheet.Timelines.Add()**](https://apireference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index) method.

## **Create Timeline to a Pivot Table**

Please see the following sample code. It loads the [sample Excel file](input.xlsx) that contains the pivot table. It then creates the timeline based on the first base pivot field. Finally, it saves the workbook in [output XLSX](output.xlsx) format. The following screenshot shows the timeline created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "timelines-CreateTimelineToPivotTable.cs" >}}