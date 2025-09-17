##How to get OData Connection Information
## **Get OData Connection Information**
There might be cases where developers need to extract OData information from the excel file. Aspose.Cells for Python via .NET provides the [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) property which returns the DataMashup information present in the Excel file. This information is represented by the [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) class. The [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) class provides the [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) property that returns the [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) collection. From the [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/), you can get access to [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) and [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).
The following code snippet demonstrates the use of these classes to retrieve the OData information.
The Source file used in the following code snippet is attached for your reference.
[Source File](96928098.xlsx)
### **Sample Code**
### **Console Output**
Connection Name: Orders
Name: Source
Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])
Name: Orders_table
Value: Source{[Name="Orders",Signature="table"]}[Data]
