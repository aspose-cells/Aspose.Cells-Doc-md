---
title: Lägg till villkorsbaserade ikoner med celltext med Node.js via C++
linktitle: Lägg till villkorliga ikoner med celltexten
type: docs
weight: 160
url: /sv/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/
description: Lär dig hur du lägger till villkorsbaserade ikoner bredvid celltexten med Aspose.Cells for Node.js via C++. Förbättra datans betydelse genom ikoner.
---

{{% alert color="primary" %}} 

Ibland vill du lägga till villkorsbaserade ikoner bredvid texten i en cell för att göra data mer meningsfull för läsarna. Du vill använda några av de villkorsstyrda formateringsikontyperna men utan att tillämpa villkorsstyrd formatering på cellerna. Aspose.Cells for Node.js via C++ stöder denna funktion.

{{% /alert %}} 

Följande kodexempel visar hur du lägger till villkorliga ikoner inställda med celltexten.



```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet (default worksheet) in the workbook
const worksheet = workbook.getWorksheets().get(0);
// Get the cells
const cells = worksheet.getCells();
// Set the columns widths (A, B and C)
worksheet.getCells().setColumnWidth(0, 24);
worksheet.getCells().setColumnWidth(1, 24);
worksheet.getCells().setColumnWidth(2, 24);

// Input date into the cells
cells.get("A1").putValue("KPIs");
cells.get("A2").putValue(19551794);
cells.get("A3").putValue(11.8070745566204);
cells.get("A4").putValue(11.858589818569);
cells.get("B1").putValue("UA Contract Size Group 4");
cells.get("B2").putValue(19551794);
cells.get("B3").putValue(11.8070745566204);
cells.get("B4").putValue(11.858589818569);
cells.get("C1").putValue("UA Contract Size Group 3");
cells.get("C2").putValue(8150131.66666667);
cells.get("C3").putValue(10.3168384396244);
cells.get("C4").putValue(11.3326931937091);

// Get the conditional icon's image data and add pictures
const iconTypes = [
{ type: AsposeCells.IconSetType.TrafficLights31, row: 1, column: 1 },
{ type: AsposeCells.IconSetType.Arrows3, row: 1, column: 2 },
{ type: AsposeCells.IconSetType.Symbols3, row: 2, column: 1 },
{ type: AsposeCells.IconSetType.Stars3, row: 2, column: 2 },
{ type: AsposeCells.IconSetType.Boxes5, row: 3, column: 1 },
{ type: AsposeCells.IconSetType.Flags3, row: 3, column: 2 }
];

iconTypes.forEach(icon => {
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(icon.type, icon.type === AsposeCells.IconSetType.Flags3 ? 1 : 0);
const stream = new Uint8Array(imagedata);
worksheet.getPictures().add(icon.row, icon.column, stream);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
