---
title: Insert Pivot Table
linktitle: Pivot Tables
type: docs
weight: 160
url: /nodejs-cpp/create-pivot-table/
description: Create and format pivot tables of Excel spreadsheet files.
---

## **Create Pivot Table**

It is possible to use Aspose.Cells for Node.js via C++ to add pivot tables to spreadsheets programmatically.

### **Pivot Table Object Model**

Aspose.Cells for Node.js via C++ provides a special set of classes that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) objects, the building blocks of a pivot table. The objects are:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) objects in the [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**

1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) object's [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) method.
   This data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) collection's [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) method, which is encapsulated in the Worksheet object.
1. Access the new [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) object from the [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) collection by passing the PivotTable index.
1. Use any of the [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) objects (explained above) to manage the pivot table.

After executing the example code, a pivot table is added to the worksheet.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}