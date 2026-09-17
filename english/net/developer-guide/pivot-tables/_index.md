---
title: Insert Pivot Table
description: Create and format pivot tables of Excel spreadsheet files.
linktitle: Pivot Tables
url: /net/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Create Pivot Table**
It is possible to use Aspose.Cells to add pivot tables to spreadsheets programmatically.

### **Pivot Table Object Model**
Aspose.Cells provides a special set of classes in the [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects, the building blocks of a pivot table. The objects are:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) objects in the [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) object's [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method. This data will be used as the pivot table's data source.  
2. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection's [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) method, which is encapsulated in the Worksheet object.  
3. Access the new [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) object from the [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection by passing the PivotTable's index.  
4. Use any of the [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects (explained above) to manage the pivot table.
After executing the example code, a pivot table is added to the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for .NET](/cells/net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/net/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/net/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for .NET](/cells/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}