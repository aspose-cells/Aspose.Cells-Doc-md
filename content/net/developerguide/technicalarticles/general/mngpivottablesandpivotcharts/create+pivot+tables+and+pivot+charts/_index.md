---
title : "Create Pivot Tables and Pivot Charts" 
description : "" 
weight : 20414 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngpivottablesandpivotcharts/create+pivot+tables+and+pivot+charts/
---

# Aspose.Cells for .NET : Create Pivot Tables and Pivot Charts


A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product or date. With Microsoft Excel it is possible to quickly re-arrange the information in the pivot table by dragging buttons to a new position.

A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells supports [pivot tables](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/general/mngpivottablesandpivotcharts/create+pivot+tables+and+pivot+charts) and [pivot charts](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/general/mngpivottablesandpivotcharts/create+pivot+tables+and+pivot+charts).

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Pivot Tables and Charts](#adding-pivot-tables-and-charts)
    *   1.1 [Preparing to use Aspose.Cells](#preparing-to-use-aspose.cells)
    *   1.2 [Adding a Pivot Table](#adding-a-pivot-table)
    *   1.3 [Adding a Pivot Chart](#adding-a-pivot-chart)
{{< /panel >}}
 

 

## Adding Pivot Tables and Charts

Aspose.Cells provides a special set of classes used to create pivot tables. These classes are used to create and set `PivotTable` objects, which act as a `PivotTable` object's basic building blocks:

*   `PivotField`, a field in a pivot table report.
*   `PivotFields`, a collection of all the `PivotField` objects in a pivot table.
*   `PivotTable`, a `PivotTable` report on a worksheet.
*   `PivotTables`, a collection of all the `PivotTable` objects on the worksheet.

### Preparing to use Aspose.Cells

1.  Download and install Aspose.Cells:
    1.  [Download Aspose.Cells](http://www.aspose.com/community/files/51/.net-components/aspose.cells-for-.net/default.aspx).
    2.  Install it on your development computer.  
        All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents. To work with the component in its full capacity you do need to have a valid license.
2.  Create a project:
    1.  Start Visual Studio.Net.
    2.  Create a new console application.
3.  Add references:  
    Add reference to the Aspose.Cells component into your project, for example ...\\Program Files\\Aspose\\Aspose.Cells\\Bin\\Net1.0\\Aspose.Cells.dll

### Adding a Pivot Table

To create a pivot table using Aspose.Cells:

1.  Add some data to a worksheet cells using a `Cell` object's `PutValue`/`setValue` method. You also use a template file already filled with data. The data will be used as the pivot table's data source.
2.  Add a pivot table to the worksheet by calling the `PivotTables` collection's `add` method (encapsulated in the `Worksheet` object).
3.  Access the new `PivotTable` object from the `PivotTables` collection by passing its index. # Use any of the pivot table objects encapsulated in the `PivotTable` object to manage the table.

Code examples are given below.

### Adding a Pivot Chart

To create a PivotChart using Aspose.Cells:

1.  Add a chart.
2.  Set the `PivotSource` of the chart to refer to an existing pivot table in the spreadsheet.
3.  Set other attributes.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Create Pivot Tables and Pivot Charts-001.png](https://docs2.aspose.com/cells/net/attachments/5017727/5112635.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Create Pivot Tables and Pivot Charts-002.png](https://docs2.aspose.com/cells/net/attachments/5017727/5112636.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Create Pivot Tables and Pivot Charts-003.png](https://docs2.aspose.com/cells/net/attachments/5017727/5112637.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Create Pivot Tables and Pivot Charts-004.png](https://docs2.aspose.com/cells/net/attachments/5017727/5112638.png) (image/png)  

