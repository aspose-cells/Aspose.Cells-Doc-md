---
title : "How to get OData Connection Information" 
description : "" 
weight : 12121 
toc : false
type: docs
url: /net/developerguide/workbook/how+to+get+odata+connection+information/
---

# Aspose.Cells for .NET : How to get OData Connection Information


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Get OData Connection Information](#get-odata-connection-information)
    *   1.1 [Sample Code](#sample-code)
    *   1.2 [Console Output](#console-output)
{{< /panel >}}
 

# Get OData Connection Information

There might be cases where developers need to extract OData information from the excel file. Aspose.Cells provides the [Workbook.DataMashup](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/datamashup) property which returns the DataMashup information present in the Excel file. This information is represented by the [DataMashup](https://apireference.aspose.com/net/cells/aspose.cells.querytables/datamashup) class. The [DataMashup](https://apireference.aspose.com/net/cells/aspose.cells.querytables/datamashup) class provides the [PowerQueryFormulas](https://apireference.aspose.com/net/cells/aspose.cells.querytables/datamashup/properties/powerqueryformulas) property that returns the [PowerQueryFormulaCollction](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformulacollction) collection. From the [PowerQueryFormulaCollction](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformulacollction), you can get access to [PowerQueryFormula](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformula) and [PowerQueryFormulaItem](https://apireference.aspose.com/net/cells/aspose.cells.querytables/powerqueryformulaitem).

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The Source file used in the following code snippet is attached for your reference.

[Source File](https://docs2.aspose.com/cells/net/attachments/96764782/96928098.xlsx)

### Sample Code

### Console Output

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, \[Implementation="2.0"\])

Name: Orders\_table

Value: Source{\[Name="Orders",Signature="table"\]}\[Data\]

