---
title: Hur man får OData anslutningsinformation
type: docs
weight: 60
url: /sv/python-net/how-to-get-odata-connection-information/
---

## **Få OData-anslutningsinformation**

Det kan finnas fall där utvecklare behöver extrahera OData-information från Excel-filen. Aspose.Cells för Python via .NET tillhandahåller egenskapen [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av klassen [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup). Klassen [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) tillhandahåller egenskapen [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) som returnerar [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/)-samlingen. Från [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) kan du få tillgång till [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) och [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).

Följande kodsnutt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928098.xlsx)

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Konsoloutput**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

