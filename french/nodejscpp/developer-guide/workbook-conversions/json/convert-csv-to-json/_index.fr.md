---
title: Convertir CSV en JSON avec Node.js via C++
linktitle: Convertir un fichier CSV en JSON
type: docs
weight: 220
url: /fr/nodejs-cpp/convert-csv-to-json/
description: Convertissez un fichier CSV en JSON en utilisant l API facile à utiliser Aspose.Cells for Node.js via C++.
keywords: Convertir, Convertir CSV en JSON, CSV vers JSON, CSV, JSON, Convertir CSV en JSON Node.js via C++, code C++ pour convertir CSV en JSON
---

## **Convertir CSV en JSON**

Aspose.Cells prend en charge la conversion de CSV en JSON. Pour cela, l'API fournit les classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) fournit les options pour exporter la plage vers JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) a les propriétés suivantes.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): Cela exporte la valeur de chaîne des cellules au format JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): Indique si la plage contient une ligne d'en-tête.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Indique l'indentation.

La classe [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) exporte le JSON en utilisant les options d'export définies avec la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/).

Le code d'exemple suivant démontre l'utilisation des classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) pour charger le [fichier CSV source](104398879.csv) et afficher la sortie JSON dans la console.

### **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Load CSV file
const filePath = path.join(sourceDir, "SampleCsv.csv");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);
const lastCell = workbook.getWorksheets().get(0).getCells().getLastCell();

// Set JsonSaveOptions
const jsonSaveOptions = new AsposeCells.JsonSaveOptions();
const range = workbook.getWorksheets().get(0).getCells().createRange(0, 0, lastCell.getRow() + 1, lastCell.getColumn() + 1);
const data = AsposeCells.JsonUtility.exportRangeToJson(range, jsonSaveOptions);

// Print JSON
console.log(data);
```

### **Sortie console**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
