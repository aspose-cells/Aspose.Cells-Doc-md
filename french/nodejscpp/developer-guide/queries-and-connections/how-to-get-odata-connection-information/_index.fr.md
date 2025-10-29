---
title: Comment obtenir les informations de connexion OData avec Node.js via C++
linktitle: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/nodejs-cpp/how-to-get-odata-connection-information/
description: Apprenez comment extraire les informations de connexion OData à partir d un fichier Excel en utilisant Aspose.Cells for Node.js via C++.
---

## **Obtenir les informations de connexion OData**

Il peut arriver que les développeurs aient besoin d'extraire des informations OData à partir du fichier Excel. Aspose.Cells for Node.js via C++ fournit la propriété [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--) qui renvoie le DataMashup présent dans le fichier Excel. Cette information est représentée par la classe [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) fournit la propriété [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) qui retourne la collection [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection). À partir de [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection), vous pouvez accéder à [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) et [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem).

Le code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier source](96928098.xlsx)

### **Code d'exemple**

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

### **Sortie console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
