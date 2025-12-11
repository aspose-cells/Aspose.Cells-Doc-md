---
title: Insert Timeline with Golang via C++
linktitle: Timelines
type: docs
weight: 170
url: /go-cpp/create-timeline/
description: Learn how to create a timeline with Aspose.Cells using C++.
---

## **Possible Usage Scenarios**

Instead of adjusting filters to show dates, you can use a PivotTable Timeline—a dynamic filter option that lets you easily filter by date/time and zoom in on the period you want with a slider control. Microsoft Excel allows you to create a timeline by selecting a pivot table and then clicking the *Insert > Timeline*. Aspose.Cells also allows you to create a timeline using the [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/) method.

## **Create Timeline for a Pivot Table**

Please see the following sample code. It loads the [sample Excel file](input.xlsx) that contains the pivot table. It then creates the timeline based on the first base pivot field. Finally, it saves the workbook in [output XLSX](output.xlsx) format. The following screenshot shows the timeline created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}