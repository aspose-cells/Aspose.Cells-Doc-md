---
title: Hur man får information om OData-anslutning
type: docs
weight: 60
url: /sv/net/how-to-get-odata-connection-information/
---
## **Få information om OData-anslutning**

 Det kan finnas fall där utvecklare behöver extrahera OData-information från excel-filen. Aspose.Cells tillhandahåller[**Arbetsbok.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup)egenskap som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) klass. De[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)klass ger[**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) egendom som returnerar[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) samling. Från[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), kan du få tillgång till[**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) och[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Följande kodavsnitt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i följande kodavsnitt bifogas som referens.

[Källfilen](96928098.xlsx)

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Konsolutgång**

Anslutningsnamn: Beställningar

Namn: Källa

Värde: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Namn: Order_table

Värde: Källa{[Name="Orders",Signature="table"]}[Data]