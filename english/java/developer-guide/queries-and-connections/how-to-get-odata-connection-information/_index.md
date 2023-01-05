---
title: How to get OData Connection Information
type: docs
weight: 60
url: /java/how-to-get-odata-connection-information/
---

## **Get OData Connection Information**

There might be cases where developers need to extract OData information from the excel file. Aspose.Cells provides the [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) property which returns the DataMashup information present in the Excel file. This information is represented by the DataMashup class. The DataMashup class provides the PowerQueryFormulas property that returns the PowerQueryFormulaCollction collection. From the PowerQueryFormulaCollction, you can get access to PowerQueryFormula and PowerQueryFormulaItem.

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The Source file used in the following code snippet is attached for your reference.

[Source File](ODataSample.xlsx)

### **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Console Output**

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]
