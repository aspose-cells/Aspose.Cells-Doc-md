---
title: Group Pivot Fields in the Pivot Table
type: docs
weight: 80
url: /nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: How to group Pivot Fields in the Pivot Table with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, How to Group Pivot Fields in the Pivot Table Using Aspose.Cells for Node.js via C++ Excel Library.
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to group pivot fields of the pivot table. When there is a large amount of data related to a pivot field, it is often useful to group them into sections. Aspose.Cells for Node.js via C++ also provides this feature using the [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-) method.

## **How to Group Pivot Fields in the Pivot Table**

The following sample code loads the [sample Excel file](64716818.xlsx) and performs grouping on the first pivot field using the [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-) method. It then refreshes and calculates data of the pivot table and saves the workbook as [output Excel file](64716817.xlsx). The screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the first pivot field is now grouped by months and quarters.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}