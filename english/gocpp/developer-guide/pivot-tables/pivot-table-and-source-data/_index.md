---
title: Pivot Table and Source Data with Golang via C++
linktitle: Pivot Table and Source Data
type: docs
weight: 30
url: /go-cpp/pivot-table-and-source-data/
description: Learn how to dynamically change a pivot table's source data using Aspose.Cells with Golang via C++.
---

## **Pivot Table's Source Data**

There are times when you want to create Microsoft Excel reports with pivot tables that take data from different data sources (such as a database) that are not known at design time. This article provides an approach to dynamically change a pivot table's data source.

### **Changing a Pivot Table's Source Data**

1. Creating a new designer template.
   1. Create a new designer template file as in the screenshot below.
   1. Define a named range, **DataSource**, which refers to this range of cells.

      **Creating a designer template & defining a named range, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)
   
2. Creating a Pivot Table Based on this named range.
   1. In Microsoft Excel, choose **Data**, then **PivotTable** and **PivotChart Report**.
   1. Create a pivot table based on the named range created in the first step.

      **Creating a pivot table based on the named range, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

   1. Drag the corresponding fields to the pivot table rows and columns, then create the resulting pivot table as shown in the screenshot below.

      **Creating a pivot table based on a corresponding field** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

3. Right‑click the pivot table and select **Table Options**.
   1. Check **Refresh on open** in **Data options** settings.

      **Setting the pivot table options** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Now, you can save this file as your designer template file.

4. Populating new data and changing the source data of a pivot table.
   1. Once the designer template is created, use the following code to change the source data of the pivot table.

Executing the example code below changes the source data of the pivot table.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotTableAndSourceData.go" >}}