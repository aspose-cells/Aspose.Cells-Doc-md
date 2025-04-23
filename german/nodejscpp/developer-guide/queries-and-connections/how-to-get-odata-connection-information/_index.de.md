---
title: Wie man OData Verbindungsinformationen mit Node.js über C++ erhält
linktitle: Wie man OData Verbindungsinformationen abruft
type: docs
weight: 60
url: /de/nodejs-cpp/how-to-get-odata-connection-information/
description: Erfahren Sie, wie Sie OData Verbindungsinformationen aus einer Excel Datei mit Aspose.Cells for Node.js via C++ extrahieren.
---

## **OData-Verbindungsinformationen abrufen**

Es kann Fälle geben, in denen Entwickler OData-Informationen aus der Excel-Datei extrahieren müssen. Aspose.Cells for Node.js via C++ bietet die Eigenschaft [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--), die die DataMashup-Informationen in der Excel-Datei zurückgibt. Diese Informationen werden durch die Klasse [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) dargestellt. Die Klasse [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) stellt die Eigenschaft [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) bereit, die die [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)-Sammlung zurückgibt. Vom [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection) aus können Sie Zugriff auf [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) und [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) erhalten.

Der folgende Code-Ausschnitt zeigt die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Code-Ausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](96928098.xlsx)

### **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ODataSample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const PQFcoll = workbook.getDataMashup().getPowerQueryFormulas();

for (let i = 0; i < PQFcoll.getCount(); i++) {
const PQF = PQFcoll.get(i);
console.log("Connection Name: " + PQF.getName());
const PQFIcoll = PQF.getPowerQueryFormulaItems();

for (let j = 0; j < PQFIcoll.getCount(); j++) {
const PQFI = PQFIcoll.get(j);
console.log("Name: " + PQFI.getName());
console.log("Value: " + PQFI.getValue());
}
}
```

### **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
