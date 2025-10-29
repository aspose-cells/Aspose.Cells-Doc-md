---
title: Charger le classeur avec des informations de culture système spécifiques via Node.js et C++
linktitle: Charger le classeur avec des paramètres régionaux spécifiques du système
type: docs
weight: 190
url: /fr/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Scénarios d'utilisation possibles**
Auparavant, il fallait changer le paramètre de culture de tout le thread pour gérer les numéros et dates dans un format culturel particulier, mais maintenant Aspose.Cells for Node.js via C++ fournit la propriété `LoadOptions.CultureInfo` que vous pouvez utiliser pour charger votre classeur avec une culture spécifique sans modifier la culture du thread entier.

## **Charger le classeur avec des paramètres régionaux spécifiques du système**
Le code d'exemple suivant montre comment charger le classeur avec une culture système spécifique pour gérer les dates.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');

// Create a readable stream
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>");
inputStream.push(null); // Signal end of stream

const culture = new Intl.NumberFormat("en-GB", {
minimumFractionDigits: 2,
maximumFractionDigits: 2
```

Le code d'exemple suivant montre comment charger le classeur avec une culture système spécifique pour gérer les numéros.

```javascript
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');
const path = require("path");

const dataDir = path.join(__dirname, "data");
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>");
inputStream.push(null);

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Html);        
options.setRegion(AsposeCells.CountryCode.UnitedKingdom);

(async () => {
const workbook = new AsposeCells.Workbook(inputStream, options);
const cell = workbook.getWorksheets().get(0).getCells().get("A1");
console.assert(cell.getType() === AsposeCells.CellValueType.IsNumeric);
console.assert(cell.getDoubleValue() === 1234.56);
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
