---
title: Pivot Tables
type: docs
weight: 160
url: /net/create-pivot-table/
aliases: [/net/pivot-tables/]
---

## **Create Pivot Table**

It is possible to use Aspose.Cells to add pivot tables to spreadsheets programmatically.

### **Pivot Table Object Model**

Aspose.Cells provides a special set of classes in the [**Aspose.Cells.Pivot**](https://apireference.aspose.com/cells/net/aspose.cells.pivot) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects, the building blocks of a pivot table. The objects are:

- [**PivotField**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) represents a field in a [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) objects in the [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**

1. Add data to a worksheet using the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) object's [**PutValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method.
   This data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the [**PivotTables**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection's [**add**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) method, which is encapsulated in the Worksheet object.
1. Access the new [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) object from the [**PivotTables**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection by passing the PivotTable index.
1. Use any of the [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects (explained above) to manage the pivot table.

After executing the example code, a pivot table is added to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.

{{% /alert %}}

