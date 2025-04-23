---
title: Come ottenere le informazioni sulla connessione OData con Node.js tramite C++
linktitle: Come ottenere informazioni sulla connessione OData
type: docs
weight: 60
url: /it/nodejs-cpp/how-to-get-odata-connection-information/
description: Impara come estrarre le informazioni sulla connessione OData da un file Excel usando Aspose.Cells for Node.js via C++.
---

## **Ottenere informazioni sulla connessione OData**

Potrebbero esserci casi in cui gli sviluppatori devono estrarre le informazioni OData dal file Excel. Aspose.Cells for Node.js via C++ fornisce la proprietà [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--) che restituisce le informazioni DataMashup presenti nel file Excel. Queste informazioni sono rappresentate dalla classe [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) fornisce la proprietà [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) che restituisce la collezione [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection). Da [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection) puoi accedere a [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) e [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem).

Il seguente frammento di codice dimostra l'uso di queste classi per recuperare le informazioni OData.

Il file di origine utilizzato nello snippet di codice seguente è allegato per il tuo riferimento.

[File di origine](96928098.xlsx)

### **Codice di Esempio**

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

### **Output della console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
