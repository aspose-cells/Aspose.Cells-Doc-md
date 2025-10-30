---
title: Hur man hämtar OData anslutningsinformation med Node.js via C++
linktitle: Hur man får OData anslutningsinformation
type: docs
weight: 60
url: /sv/nodejs-cpp/how-to-get-odata-connection-information/
description: Lär dig hur du extraherar OData anslutningsinformation från en Excel fil med hjälp av Aspose.Cells for Node.js via C++.
---

## **Få OData-anslutningsinformation**

Det kan finnas tillfällen då utvecklare behöver extrahera OData-information från Excel-filen. Aspose.Cells for Node.js via C++ tillhandahåller `[**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--)`-egenskapen som returnerar DataMashup-informationen som är närvarande i Excel-filen. Denna information representeras av klassen `[**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup)`. Klassen `[**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup)` tillhandahåller egenskapen `[**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--)`, som returnerar `[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)`-samlingen. Från `[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)` kan du få tillgång till `[**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula)` och `[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem)`.

Följande kodsnutt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928098.xlsx)

### **Exempelkod**

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

### **Konsoloutput**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
