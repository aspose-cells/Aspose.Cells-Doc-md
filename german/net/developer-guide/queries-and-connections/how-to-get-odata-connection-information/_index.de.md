---
title: So erhalten Sie OData-Verbindungsinformationen
type: docs
weight: 60
url: /de/net/how-to-get-odata-connection-information/
---
## **Rufen Sie OData-Verbindungsinformationen ab**

 Es kann Fälle geben, in denen Entwickler OData-Informationen aus der Excel-Datei extrahieren müssen. Aspose.Cells bietet die[**Arbeitsmappe.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) -Eigenschaft, die die in der Excel-Datei vorhandenen DataMashup-Informationen zurückgibt. Diese Informationen werden durch die dargestellt[**DatenMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) Klasse. Das[**DatenMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)Klasse bietet die[**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) Eigenschaft, die die zurückgibt[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) Sammlung. Von dem[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), auf die Sie zugreifen können[**PowerQueryFormel**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) und[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

Der folgende Codeausschnitt veranschaulicht die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Codeausschnitt verwendete Quelldatei ist als Referenz beigefügt.

[Quelldatei](96928098.xlsx)

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Konsolenausgabe**

Verbindungsname: Bestellungen

Name: Quelle

Wert: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Wert: Quelle{[Name="Orders",Signature="table"]}[Daten]