---
title: Wie man OData Verbindungsinformationen abruft
type: docs
weight: 60
url: /de/java/how-to-get-odata-connection-information/
---

## **OData-Verbindungsinformationen abrufen**

Es kann vorkommen, dass Entwickler OData-Informationen aus der Excel-Datei extrahieren müssen. Aspose.Cells bietet die Eigenschaft [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup), die die im Excel-File vorhandenen Datenmashup-Informationen zurückgibt. Diese Informationen werden durch die Klasse DataMashup dargestellt. Die Klasse DataMashup bietet die Eigenschaft PowerQueryFormulas, die die PowerQueryFormulaCollction-Sammlung zurückgibt. Aus der PowerQueryFormulaCollction können Sie auf PowerQueryFormula und PowerQueryFormulaItem zugreifen.

Der folgende Code-Ausschnitt zeigt die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Code-Ausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](ODataSample.xlsx)

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
