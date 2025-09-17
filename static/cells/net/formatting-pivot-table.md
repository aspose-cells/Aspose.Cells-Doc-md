##Formatting Pivot Table
## **Pivot Table Appearance**
How to Create a Pivot Table explains how to create a simple pivot table. This article describes how to customize a pivot table's appearance by setting various properties:
- Pivot table format options
- Pivot fields format options
- Data field format options
### **Setting Pivot Table Format Options**
The [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) class controls the overall pivot table and can be formatted in a number of ways.
#### **Setting the AutoFormat Type**
Microsoft Excel offers a number of different pre-set report formats. Aspose.Cells support these formatting options too. To access them:
1. Set [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) to **true**.
1. Assign a formatting option from the [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype) enumeration.
#### **Setting Format Options**
The code sample below shows how to format the pivot table to show grand totals for rows and columns, and how to set the report's field order. It also shows how to set a customer string for null values.
#### **Formatting Look and Feel Manually**
To formatting how the pivot table report looks manually, instead of using pre-set report formats, use the [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) and [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall) methods. Create a style object for your desired formatting, for example:
### **Setting Pivot Field Format Options**
The [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) class represents a field in a pivot table and can be formatted in a number of ways. The code sample below shows how to:
- Access row fields.
- Setting subtotals.
- Setting autosort.
- Setting autoshow.
#### **Setting Row/Column/Page Fields Format**
### **Setting Data fields format**
The code sample below shows how to set display formats and number format for data fields.
### **Clearing Pivot Fields**
The [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) has a method named [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) that allows you to clear pivot fields. Use it when you want to clear all the pivot fields in the areas, for example, page, column, row or data.
The code sample below shows how to clear all the pivot fields in a data area.
