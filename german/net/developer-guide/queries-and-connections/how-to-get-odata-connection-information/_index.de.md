---
title: Wie man OData Verbindungsinformationen abruft
type: docs
weight: 60
url: /de/net/how-to-get-odata-connection-information/
---

## **OData-Verbindungsinformationen abrufen**

Es kann vorkommen, dass Entwickler OData-Informationen aus der Excel-Datei extrahieren müssen. Aspose.Cells bietet die [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup)-Eigenschaft, die Informationen zu DataMashup liefert, die in der Excel-Datei vorhanden sind. Diese Informationen werden durch die [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)-Klasse dargestellt. Die [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)-Klasse bietet die [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas)-Eigenschaft, die die [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)-Sammlung zurückgibt. Über die [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) können Sie auf [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) und [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem) zugreifen.

Der folgende Code-Ausschnitt zeigt die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Code-Ausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](96928098.xlsx)

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
