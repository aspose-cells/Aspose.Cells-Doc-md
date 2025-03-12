---
title: Convert the Smart Art to Group Shape with Node.js via C++
linktitle: Convert the Smart Art to Group Shape
type: docs
weight: 200
url: /nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Possible Usage Scenarios**

You can convert Smart Art Shape into Group Shape using the [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--) method. It will enable you to handle smart art shape like a group shape. Consequently, you will have access to the individual parts or shapes of the group shape.

## **Convert the Smart Art to Group Shape**

The following sample code loads the [sample Excel file](55541793.xlsx) containing a smart art shape as shown in this screenshot. It then converts the smart art shape into group shape and prints the Shape.isGroup property. Please see the console output of the sample code given below.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Sample Code**

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

## **Console Output**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
