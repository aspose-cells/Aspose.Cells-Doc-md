---
title: Set custom DataSource for WorkbookDesigner
type: docs
weight: 60
url: /net/set-custom-datasource-for-workbookdesigner/
---

Aspose.Cells provides the option to set custom DataSource for WorkbookDesigner. The API provides an overloaded method [WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5) which takes the name of the source as the first parameter and the instance of the class that implements [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) as the second parameter. 

The following code snippet demonstrates the use of [WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5) method to set the custom DataSource.
## **Sample Code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-1.cs" >}}

The implementation of *CustomerDataSource*, *Customer*, and *CustomerList* classes is given below

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}

The source and output excel files are attached for reference.

[Source File](95584319.xlsx)

[Output File](95584320.xlsx)
{{< app/cells/assistant language="csharp" >}}