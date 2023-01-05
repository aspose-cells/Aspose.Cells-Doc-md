---
title: So erhalten Sie OData-Verbindungsinformationen
type: docs
weight: 60
url: /de/java/how-to-get-odata-connection-information/
---
## **Rufen Sie OData-Verbindungsinformationen ab**

Es kann Fälle geben, in denen Entwickler OData-Informationen aus der Excel-Datei extrahieren müssen. Aspose.Cells bietet die[**Arbeitsmappe.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)-Eigenschaft, die die in der Excel-Datei vorhandenen DataMashup-Informationen zurückgibt. Diese Informationen werden durch die DataMashup-Klasse dargestellt. Die DataMashup-Klasse stellt die PowerQueryFormulas-Eigenschaft bereit, die die PowerQueryFormulaCollction-Auflistung zurückgibt. Über PowerQueryFormulaCollction erhalten Sie Zugriff auf PowerQueryFormula und PowerQueryFormulaItem.

Der folgende Codeausschnitt veranschaulicht die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Codeausschnitt verwendete Quelldatei ist als Referenz beigefügt.

[Quelldatei](ODataSample.xlsx)

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Konsolenausgabe**

Verbindungsname: Bestellungen

Name: Quelle

Wert: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Wert: Quelle{[Name="Orders",Signature="table"]}[Daten]