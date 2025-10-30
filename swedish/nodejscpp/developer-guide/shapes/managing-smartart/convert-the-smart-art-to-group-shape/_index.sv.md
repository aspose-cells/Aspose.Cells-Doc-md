---
title: Konvertera Smart Art till Gruppform med Node.js via C++
linktitle: Konvertera Smart Art till gruppform
type: docs
weight: 200
url: /sv/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Möjliga användningsscenario**

Du kan konvertera Smart Art-Form till Gruppform med hjälp av [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--) metoden. Det gör att du kan hantera smart art-form som en gruppform. Därmed får du tillgång till de individuella delarna eller formerna av gruppformen.

## **Konvertera SmartArt till gruppform**

Följande exempelkod laddar den [provexemplet](55541793.xlsx) som innehåller en smart art-form som visas i denna skärmdump. Den konverterar sedan smart art-formen till en gruppform och skriver ut Shape.isGroup egenskapen. Se vänligen exempelutdata i konsolen nedan.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **Konsoloutput**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
