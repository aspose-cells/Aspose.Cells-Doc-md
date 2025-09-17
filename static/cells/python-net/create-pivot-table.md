##Insert Pivot Table
Create and format Pivot Table with Aspose.Cells for Python via .NET.
## **Create Pivot Table**
It is possible to use Aspose.Cells for Python via .NET to add pivot tables to spreadsheets programmatically.
### **Pivot Table Object Model**
Aspose.Cells for Python via .NET provides a special set of classes in the [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) namespace that are used to create and control pivot tables. These classes are used to create and set [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) objects, the building blocks of a pivot table. The objects are:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) represents a field in a [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) represents a collection of all the [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) objects in the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) represents a PivotTable on a worksheet.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) represents a collection of all the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objects on a worksheet.
### **Creating a Simple Pivot Table Using Aspose.Cells**
1. Add data to a worksheet using the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) object's [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) method.
This data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) collection's [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) method, which is encapsulated in the Worksheet object.
1. Access the new [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) object from the [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) collection by passing the PivotTable index.
1. Use any of the [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objects (explained above) to manage the pivot table.
After executing the example code, a pivot table is added to the worksheet.
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
## **Advance topics**
- [Consolidation Function](https://docs.aspose.com/cells/python-net/consolidation-function/)
- [Custom sorting in Pivot Table](https://docs.aspose.com/cells/python-net/custom-sorting-in-pivot-table/)
- [Customize Globalization Settings for Pivot Table](https://docs.aspose.com/cells/python-net/customize-globalization-settings-for-pivot-table/)
- [Disable Pivot Table Ribbons](https://docs.aspose.com/cells/python-net/disable-pivot-table-ribbons/)
- [Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table](https://docs.aspose.com/cells/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formatting Pivot Table](https://docs.aspose.com/cells/python-net/formatting-pivot-table/)
- [Get External Connection Data Source of Pivot Table](https://docs.aspose.com/cells/python-net/get-external-connection-data-source-of-pivot-table/)
- [Get Pivot Table refresh date and refresh by who information](https://docs.aspose.com/cells/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Group Pivot Fields in the Pivot Table](https://docs.aspose.com/cells/python-net/group-pivot-fields-in-the-pivot-table/)
- [Parsing Pivot Cached Records while loading Excel file](https://docs.aspose.com/cells/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Pivot Table and Source Data](https://docs.aspose.com/cells/python-net/pivot-table-and-source-data/)
- [Pivot Table Hide and Sort data](https://docs.aspose.com/cells/python-net/pivot-table-hide-and-sort-data/)
- [Refresh and Calculate Pivot Table having Calculated Items](https://docs.aspose.com/cells/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Save Pivot Table in ODS file](https://docs.aspose.com/cells/python-net/save-pivot-table-in-ods-file/)
- [Show report filter pages option](https://docs.aspose.com/cells/python-net/show-report-filter-pages-option/)
- [Working with data display formats of DataField in Pivot Table](https://docs.aspose.com/cells/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
