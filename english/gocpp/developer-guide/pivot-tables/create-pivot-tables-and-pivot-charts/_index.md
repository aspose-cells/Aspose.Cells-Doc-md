---
title: Create Pivot Tables and Pivot Charts with Golang via C++
linktitle: Create Pivot Tables and Pivot Charts
type: docs
weight: 20
url: /go-cpp/create-pivot-tables-and-pivot-charts/
description: Learn how to create pivot tables and pivot charts in Excel files using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product, or date. With Microsoft Excel, it is possible to quickly rearrange the information in the pivot table by dragging buttons to a new position.

A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells supports [pivot tables](/cells/cpp/create-pivot-tables-and-pivot-charts/) and [pivot charts](/cells/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Adding Pivot Tables and Charts**

Aspose.Cells provides a special set of classes used to create pivot tables. These classes are used to create and configure PivotTable objects, which act as the basic building blocks of a PivotTable.

- **PivotField**, a field in a pivot table report.
- **PivotFields**, a collection of all the PivotField objects in a pivot table.
- **PivotTable**, a PivotTable report on a worksheet.
- **PivotTables**, a collection of all the PivotTable objects on the worksheet.

### **Preparing to use Aspose.Cells**

1. Download and install Aspose.Cells:
   1. [Download Aspose.Cells](https://downloads.aspose.com/cells/go-cpp/).
   2. Install it on your development computer.  
      All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only adds watermarks to produced documents. To work with the component at full capacity, you need a valid license.
2. Create a project:
   1. Start your C++ IDE (e.g., Visual Studio).
   2. Create a new console application.
3. Add references:  
   Add a reference to the Aspose.Cells component in your project, for example, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Adding a Pivot Table**

To create a pivot table using Aspose.Cells:

1. Add some data to a worksheet’s cells using a `Cell` object's `PutValue` method. You can also use a template file already filled with data. The data will be used as the pivot table’s data source.
2. Add a pivot table to the worksheet by calling the `PivotTables` collection’s `Add` method (encapsulated in the `Worksheet` object).
3. Access the new `PivotTable` object from the `PivotTables` collection by its index. Use any of the objects within the `PivotTable` to manage the table.

Code examples are given below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}

### **Adding a Pivot Chart**

To create a PivotChart using Aspose.Cells:

1. Add a chart.
2. Set the `PivotSource` of the chart to refer to an existing pivot table in the spreadsheet.
3. Set other attributes.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}