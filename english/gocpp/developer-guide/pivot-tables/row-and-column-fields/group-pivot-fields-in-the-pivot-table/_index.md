---
title: Group Pivot Fields in the Pivot Table with Golang via C++
linktitle: Group Pivot Fields in the Pivot Table
type: docs
weight: 80
url: /go-cpp/group-pivot-fields-in-the-pivot-table/
description: Learn how to group pivot fields in a pivot table using Aspose.Cells for Go via C++.
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to group pivot fields **in** the pivot table. When there is a large amount of data related to a pivot field, it is often useful to group them into sections. Aspose.Cells also provides this feature using the [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) method.

## **Group Pivot Fields in the Pivot Table**

The following sample code loads the [sample Excel file](64716818.xlsx) and performs grouping on the first pivot field using the [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) method. It then refreshes the pivot table, calculates its data, and saves the workbook as [output Excel file](64716817.xlsx). The screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the first pivot field is now grouped by months and quarters.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}
