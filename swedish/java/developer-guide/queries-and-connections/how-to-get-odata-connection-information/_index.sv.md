---
title: Hur man får OData anslutningsinformation
type: docs
weight: 60
url: /sv/java/how-to-get-odata-connection-information/
---

## **Få OData-anslutningsinformation**

Det kan finnas fall där utvecklare behöver extrahera OData information från excelfilen. Aspose.Cells tillhandahåller [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) egenskapen som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av DataMashup-klassen. DataMashup-klassen tillhandahåller egenskapen PowerQueryFormulas som returnerar PowerQueryFormulaCollction-samlingen. Från PowerQueryFormulaCollction kan du få tillgång till PowerQueryFormula och PowerQueryFormulaItem.

Följande kodsnutt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](ODataSample.xlsx)

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Konsoloutput**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
