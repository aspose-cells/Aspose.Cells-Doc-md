---
title: Pivot Table and Source Data
type: docs
weight: 110
url: /java/pivot-table-and-source-data/
---

## **Pivot Table's Source Data**
There are times when you want to create Microsoft Excel reports with pivot tables that takes data from different data sources (such as a database) that are not known at design time. This article provides an approach to dynamically change a pivot table's data source.
## **Changing a Pivot Table's Source Data**
1. Creating a new designer template.
   1. Create a new designer template file as in the screenshot below.
   1. Then define a named range, **DataSource**, which refers to this range of cells. 

      **Creating a designer template & defining a named range, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Creating a Pivot Table Based on this named range.
   1. In Microsoft Excel, choose **Data**, then **PivotTable** and **PivotChart Report**.
   1. Create a pivot table based on the named range created in the first step. 

      **Creating a pivot table based on the named range, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

1. Drag the corresponding field to pivot table row and column, then create the resulting pivot table as in the screenshot below. 

   **Creating a pivot table based on a corresponding field** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

1. Right-click the pivot table and select **Table Options**.
   1. Check **Refresh on open** in **Data options** settings. 

      **Setting the pivot table options** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)



Now, you can save this file as your designer template file.

1. Populating new data and changing source data of a pivot table.
   1. Once the designer template is created, use the following code to change the source data of the pivot table.

Executing the example code below changes the source data of the pivot table and the pivot table will look like the one below.

**Dynamically changed pivot table** 

![todo:image_alt_text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
{{< app/cells/assistant language="java" >}}