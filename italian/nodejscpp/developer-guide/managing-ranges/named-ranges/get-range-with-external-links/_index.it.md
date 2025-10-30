---
title: Ottieni intervallo con link esterni usando Node.js tramite C++
linktitle: Ottieni Range con Collegamenti Esterni
type: docs
weight: 120
url: /it/nodejs-cpp/get-range-with-external-links/
description: Impara come recuperare intervalli con link esterni usando Aspose.Cells for Node.js via C++. Recupera i dati da diversi file Excel in modo efficiente.
---

## **Ottieni Intervallo con Link Esterni**

Molti file Excel accedono ai dati da altri file Excel tramite link esterni. Aspose.Cells for Node.js via C++ offre l'opzione di recuperare questi link esterni usando il metodo [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-). Il metodo [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) restituisce un array di tipo [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). La classe [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) fornisce una proprietà [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) che restituisce il nome del file esterno. La classe [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) espone i seguenti membri.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): La colonna finale dell'area
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): La riga finale dell'area
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Ottieni il nome del file esterno se questo è un riferimento esterno
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Indica se questa è un'area
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Indica se questa è una connessione esterna
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Indica in quale foglio si trova questo riferimento
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): La colonna di inizio dell'area
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): La riga di inizio dell'area

Il codice di esempio riportato di seguito mostra l'uso del metodo [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) per ottenere intervalli con collegamenti esterni.

## **Codice di Esempio**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
