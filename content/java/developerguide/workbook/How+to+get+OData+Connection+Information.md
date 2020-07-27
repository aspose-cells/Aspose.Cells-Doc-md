+++
title = "How to get OData Connection Information" 
description = "" 
weight = 12105 
+++

Aspose.Cells for Java : How to get OData Connection Information  

# Aspose.Cells for Java : How to get OData Connection Information


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Get OData Connection Information](#HowtogetODataConnectionInformation-GetODataConnectionInformation)
    *   1.1 [Sample Code](#HowtogetODataConnectionInformation-SampleCode)
    *   1.2 [Console Output](#HowtogetODataConnectionInformation-ConsoleOutput)
{{< /panel >}}
 

# Get OData Connection Information

There might be cases where developers need to extract OData information from the excel file. Aspose.Cells provides the [Workbook.DataMashup](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#DataMashup) property which returns the DataMashup information present in the Excel file. This information is represented by the DataMashup class. The DataMashup class provides the PowerQueryFormulas property that returns the PowerQueryFormulaCollction collection. From the PowerQueryFormulaCollction, you can get access to PowerQueryFormula and PowerQueryFormulaItem.

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The Source file used in the following code snippet is attached for your reference.

[Source File](https://docs.aspose.com/download/attachments/96764782/ODataSample.xlsx?version=1&modificationDate=1575566431680&api=v2)

### Sample Code

### Console Output

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, \[Implementation="2.0"\])

Name: Orders\_table

Value: Source{\[Name="Orders",Signature="table"\]}\[Data\]

