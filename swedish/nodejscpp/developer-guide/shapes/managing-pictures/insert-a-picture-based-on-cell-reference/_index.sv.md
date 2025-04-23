---
title: Infoga en bild baserad på cellreferens med Node.js via C++
linktitle: Infoga en bild baserat på cellreferens
type: docs
weight: 150
url: /sv/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Lär dig hur du infogar en bild i ett kalkylblad baserat på en cellreferens med Aspose.Cells for Node.js via C++. Visa cellens data i en bild.
---

{{% alert color="primary" %}}
Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ange en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).
{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells for Node.js via C++ stöder att visa innehållet i en kalkylcells- eller cellområde i en bild. Du kan länka bilden till cellen som innehåller den data du vill visa. Eftersom cellen eller cellområdet är länkat till grafiken, visas ändringar i data i cellen eller cellområdet automatiskt i grafiken. Lägg till en bild till kalkylbladet genom att anropa [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)-metoden i [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-objektet). Ange cellområdet med hjälp av [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)-attributet för [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)-objektet.

### Kodexempel

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
