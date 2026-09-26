---
title: How to get OData Connection Information with Golang via C++
linktitle: How to get OData Connection Information
type: docs
weight: 60
url: /go-cpp/how-to-get-odata-connection-information/
description: Learn how to extract OData connection information from Excel files using Aspose.Cells for Go via C++.
---

## **Get OData Connection Information**

There might be cases where developers need to extract OData information from an Excel file. Aspose.Cells provides the `Workbook.GetDataMashup()` property, which returns the DataMashup information present in the Excel file. This information is represented by the **DataMashup** class. The **DataMashup** class provides the `GetPowerQueryFormulas()` property that returns a **PowerQueryFormulaCollection**. From the **PowerQueryFormulaCollection**, you can get access to **PowerQueryFormula** and **PowerQueryFormulaItem**.

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The source file used in the following code snippet is attached for your reference.

[Source File](96928098.xlsx)

### **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToGetOdataConnectionInformation.go" >}}

### **Console Output**

{{< highlight go >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="go" >}}
