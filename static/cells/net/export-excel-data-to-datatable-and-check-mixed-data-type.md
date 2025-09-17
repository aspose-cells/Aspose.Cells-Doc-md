##Export Excel Data to DataTable and Check Mixed Data Type
Learn how to Export Excel Data to DataTable and Check Mixed Data Type through the Aspose.Cells for .NET API.
## **Possible Usage Scenarios**
If a column contains data of various types, the program will throw a type exception when exporting data to a DataTable. For exporting data table, by default, Aspose.Cells evaluates the data type for the values based on the very first (cell) value in the column. So, if the value is number, it means that the data type of the column would be numeric, which is reasonable. If the very first value is number but there are alphanumeric data or values in the column, a string data type should be assigned. To cope with it, please use [ExportDataTable overload](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1) which involves [ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/) and try to set [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) Boolean attribute to "true" if a column has both numeric and string values to escape from error.
## **Export Excel Data to DataTable and Check Mixed Data Type**
The following sample explains the use of [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/) property to export excel data to data table. Please see the [sample Excel file](sample.xlsx), its screenshot and the console output for a reference.
### **Sample Code**
### **Screenshot**
### **Console Output**
Below is the console debug output of the above sample code
Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String
