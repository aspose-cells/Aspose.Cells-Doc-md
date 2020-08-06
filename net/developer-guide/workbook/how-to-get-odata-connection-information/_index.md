---
title: How to get OData Connection Information
type: docs
weight: 60
url: /net/how-to-get-odata-connection-information/
---

# **Get OData Connection Information**
There might be cases where developers need to extract OData information from the excel file. Aspose.Cells provides the [Workbook.DataMashup](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/datamashup) property which returns the DataMashup information present in the Excel file. This information is represented by the [DataMashup](https://apireference.aspose.com/net/cells/aspose.cells.querytables/datamashup) class. The [DataMashup](https://apireference.aspose.com/net/cells/aspose.cells.querytables/datamashup) class provides the [PowerQueryFormulas](https://apireference.aspose.com/net/cells/aspose.cells.querytables/datamashup/properties/powerqueryformulas) property that returns the [PowerQueryFormulaCollction](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformulacollction) collection. From the [PowerQueryFormulaCollction](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformulacollction), you can get access to [PowerQueryFormula](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformula) and [PowerQueryFormulaItem](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformulaitem).

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The Source file used in the following code snippet is attached for your reference.

[Source File](attachments/96764782/96928098.xlsx)
### **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}
### **Console Output**
Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]