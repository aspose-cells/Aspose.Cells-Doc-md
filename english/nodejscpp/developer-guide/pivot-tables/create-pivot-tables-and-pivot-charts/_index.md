---
title: Create Pivot Tables and Pivot Charts
type: docs
weight: 20
url: /nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: How to add Pivot Tables and Pivot Charts with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, Add Pivot Tables and Pivot Charts Using Aspose.Cells for Node.js via C++ Excel Library.
---

{{% alert color="primary" %}}

A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product or date. With Microsoft Excel it is possible to quickly re-arrange the information in the pivot table by dragging buttons to a new position.

A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells for Node.js via C++ supports [pivot tables](/cells/nodejs-cpp/create-pivot-tables-and-pivot-charts/) and [pivot charts](/cells/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Add Pivot Tables and Charts Using Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ provides a special set of classes used to create pivot tables. These classes are used to create and set PivotTable objects, which act as a PivotTable object's basic building blocks:

- PivotField, a field in a pivot table report.
- PivotFields, a collection of all the PivotField objects in a pivot table.
- PivotTable, a PivotTable report on a worksheet.
- PivotTables, a collection of all the PivotTable objects on the worksheet.

### **Prepare to use Aspose.Cells for Node.js via C++**
1. Install Aspose.Cells for Node.js via C++ from NPM, use command as:  $ npm install aspose.cells.node.
1. You can also follow the step-by-step instructions on how to install “Aspose.Cells for Node.js via C++” to your developer environment.


### **How to Add a Pivot Table Using Aspose.Cells for Node.js via C++**

To create a pivot table using Aspose.Cells for Node.js via C++:

1. Add some data to a worksheet cells using a Cell object's put_value method. You also use a template file already filled with data. The data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the PivotTables collection's add method (encapsulated in the Worksheet object).
1. Access the new PivotTable object from the PivotTables collection by passing its index. # Use any of the pivot table objects encapsulated in the PivotTable object to manage the table.

Code examples are given below.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **How to Add a Pivot Chart Using Aspose.Cells for Node.js via C++ Library**

To create a PivotChart using Aspose.Cells for Node.js via C++:

1. Add a chart.
1. Set the PivotSource of the chart to refer to an existing pivot table in the spreadsheet.
1. Set other attributes.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}