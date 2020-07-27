+++
title = "Pivot Table and Source Data" 
description = "" 
weight = 12250 
+++

Aspose.Cells for Java : Pivot Table and Source Data  

# Aspose.Cells for Java : Pivot Table and Source Data



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Pivot Table's Source Data](#PivotTableandSourceData-PivotTable'sSourceData)
    *   1.1 [Changing a Pivot Table's Source Data](#PivotTableandSourceData-ChangingaPivotTable'sSourceData)
{{< /panel >}}
 

 

## Pivot Table's Source Data

There are times when you want to create Microsoft Excel reports with pivot tables that takes data from different data sources (such as a database) that are not known at design time. This article provides an approach to dynamically change a pivot table's data source.

### Changing a Pivot Table's Source Data

1.  Creating a new designer template.
    1.  Create a new designer template file as in the screenshot below.
    2.  Then define a named range, **DataSource**, which refers to this range of cells.  
          
        **Creating a designer template & defining a named range, DataSource**  
        ![](https://docs2.aspose.com/cells/java/attachments/5275913/5472404.png)
2.  Creating a Pivot Table Based on this named range.
    1.  In Microsoft Excel, choose **Data**, then **PivotTable** and **PivotChart Report**.
    2.  Create a pivot table based on the named range created in the first step.  
          
        **Creating a pivot table based on the named range, DataSource**  
        ![](https://docs2.aspose.com/cells/java/attachments/5275913/5472416.png)
    3.  Drag the corresponding field to pivot table row and column, then create the resulting pivot table as in the screenshot below.  
          
        **Creating a pivot table based on a corresponding field**  
        ![](https://docs2.aspose.com/cells/java/attachments/5275913/5472415.png)
3.  Right-click the pivot table and select **Table Options**.
    1.  Check **Refresh on open** in **Data options** settings.  
          
        **Setting the pivot table options**  
        ![](https://docs2.aspose.com/cells/java/attachments/5275913/5472414.png)  
          
        Now, you can save this file as your designer template file.
4.  Populating new data and changing source data of a pivot table.
    1.  Once the designer template is created, use the following code to change the source data of the pivot table.

Executing the example code below changes the source data of the pivot table and the pivot table will look like the one below.

**Dynamically changed pivot table**  
![](https://docs2.aspose.com/cells/java/attachments/5275913/5472413.png)

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Pivot Table-001.png](https://docs2.aspose.com/cells/java/attachments/5275913/5472404.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Pivot Table-002.png](https://docs2.aspose.com/cells/java/attachments/5275913/5472416.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Pivot Table-003.png](https://docs2.aspose.com/cells/java/attachments/5275913/5472415.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Pivot Table-004.png](https://docs2.aspose.com/cells/java/attachments/5275913/5472414.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Pivot Table-005.png](https://docs2.aspose.com/cells/java/attachments/5275913/5472413.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [How to Create a PivotTable-001.png](https://docs2.aspose.com/cells/java/attachments/5275913/5472412.png) (image/png)  

