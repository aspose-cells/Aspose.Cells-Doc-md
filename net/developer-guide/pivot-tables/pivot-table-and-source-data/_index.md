---
title: Pivot Table and Source Data
type: docs
weight: 30
url: /net/pivot-table-and-source-data/
---

## **Create Pivot Table**

It is possible to use Aspose.Cells to add pivot tables to spreadsheets programmatically.

### **Create Pivot Table Using Microsoft Excel**

Aspose.Cells provides a special set of classes in the [**Aspose.Cells.Pivot**](https://apireference.aspose.com/cells/net/aspose.cells.pivot) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects, the building blocks of a pivot table. The objects are:

- [**PivotField**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) represents a field in a [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) objects in the [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects on a worksheet.

### **Create Pivot Table Using Aspose.Cells**

1. Add data to a worksheet using the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) object's [**PutValue**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) method.
   This data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the [**PivotTables**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection's [**add**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) method, which is encapsulated in the Worksheet object.
1. Access the new [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) object from the [**PivotTables**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) collection by passing the PivotTable index.
1. Use any of the [**PivotTable**](https://apireference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objects (explained above) to manage the pivot table.

After executing the example code, a pivot table is added to the worksheet.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.

{{% /alert %}}

## **Pivot Table's Source Data**

There are times when you want to create Microsoft Excel reports with pivot tables that take data from different data sources (such as a database) that are not known at design time. This article provides an approach to dynamically change a pivot table's data source.

### **Changing a Pivot Table's Source Data**

1. Creating a new designer template.
   1. Create a new designer template file as in the screenshot below.
   1. Then define a named range, **DataSource**, which refers to this range of cells.
1. Creating a Pivot Table Based on this named range.
   1. In Microsoft Excel, choose **Data**, then **PivotTable** and **PivotChart Report**.
   1. Create a pivot table based on the named range created in the first step.
   1. Drag the corresponding field to pivot table row and column, then create the resulting pivot table as in the screenshot below.
1. Right-click the pivot table and select **Table Options**.
   1. Check **Refresh on open** in **Data options** settings.

Now, you can save this file as your designer template file.

1. Populating new data and changing source data of a pivot table.
   1. Once the designer template is created, use the following code to change the source data of the pivot table.

Executing the example code below changes the source data of the pivot table.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}
