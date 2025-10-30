---
title: Cargar elLibro con información cultural del sistema específica usando Node.js y C++
linktitle: Cargar el Libro con Información Específica de Cultura del Sistema
type: docs
weight: 190
url: /es/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Escenarios de uso posibles**
Anteriormente, tenías que cambiar la info de cultura de todo el hilo para tratar números y fechas en un formato cultural particular, pero ahora Aspose.Cells for Node.js via C++ proporciona la propiedad `LoadOptions.CultureInfo` que puedes usar para cargar tu libro con info de cultura específica sin cambiar la cultura del hilo.

## **Cargar el Libro con Información Específica de Cultura del Sistema**
El siguiente ejemplo muestra cómo cargar el libro con info de cultura del sistema específica para tratar fechas.

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

El siguiente ejemplo muestra cómo cargar el libro con info de cultura del sistema específica para tratar números.

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
