---
title: Wie man OData Verbindungsinformationen abruft
type: docs
weight: 60
url: /de/python-net/how-to-get-odata-connection-information/
---

## **OData-Verbindungsinformationen abrufen**

Es kann Fälle geben, in denen Entwickler OData-Informationen aus der Excel-Datei extrahieren müssen. Aspose.Cells für Python via .NET bietet die Eigenschaft [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup), die die DataMashup-Informationen in der Excel-Datei zurückgibt. Diese Informationen werden durch die [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup)-Klasse dargestellt. Die [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup)-Klasse bietet die Eigenschaft [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas), die die Sammlung [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) zurückgibt. Über [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) können Sie auf [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) und [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem) zugreifen.

Der folgende Code-Ausschnitt zeigt die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Code-Ausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](96928098.xlsx)

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

