---
title: Hur man får OData anslutningsinformation
type: docs
weight: 60
url: /sv/net/how-to-get-odata-connection-information/
---

## **Få OData-anslutningsinformation**

Det kan finnas fall där utvecklare behöver extrahera OData-information från Excel-filen. Aspose.Cells tillhandahåller egenskapen [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av klassen [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup). Klassen [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) tillhandahåller egenskapen [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) som returnerar samlingen [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction). Från [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) kan du få tillgång till [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) och [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Följande kodsnutt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928098.xlsx)

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Konsoloutput**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
