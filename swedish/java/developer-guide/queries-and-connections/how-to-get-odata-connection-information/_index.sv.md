---
title: Hur man får information om OData-anslutning
type: docs
weight: 60
url: /sv/java/how-to-get-odata-connection-information/
---
## **Få information om OData-anslutning**

Det kan finnas fall där utvecklare behöver extrahera OData-information från excel-filen. Aspose.Cells tillhandahåller[**Arbetsbok.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)egenskap som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av DataMashup-klassen. Klassen DataMashup tillhandahåller egenskapen PowerQueryFormulas som returnerar samlingen PowerQueryFormulaCollction. Från PowerQueryFormulaCollction kan du få tillgång till PowerQueryFormula och PowerQueryFormulaItem.

Följande kodavsnitt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i följande kodavsnitt bifogas som referens.

[Källfilen](ODataSample.xlsx)

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Konsolutgång**

Anslutningsnamn: Beställningar

Namn: Källa

Värde: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Namn: Order_table

Värde: Källa{[Name="Orders",Signature="table"]}[Data]