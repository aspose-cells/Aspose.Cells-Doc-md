---
title: Insert Pivot Table
description: Create and format Pivot Table with Aspose.Cells for Python via .NET.
linktitle: Pivot Tables
url: /python-net/pivot-tables/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Create Pivot Table**
It is possible to use Aspose.Cells for Python via .NET to add pivot tables to spreadsheets programmatically.

### **Pivot Table Object Model**
Aspose.Cells for Python via .NET provides a special set of classes in the [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) objects, the building blocks of a pivot table. The objects are:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) objects in the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) object's [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) method. This data will be used as the pivot table's data source.  
2. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) collection's [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) method, which is encapsulated in the Worksheet object.  
3. Access the new [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) object from the [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) collection by its index.  
4. Use any of the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objects (explained above) to manage the pivot table.
After executing the example code, a pivot table is added to the worksheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## **Advanced topics**

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET](/cells/python-net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET](/cells/python-net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/python-net/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/python-net/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via .NET](/cells/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}