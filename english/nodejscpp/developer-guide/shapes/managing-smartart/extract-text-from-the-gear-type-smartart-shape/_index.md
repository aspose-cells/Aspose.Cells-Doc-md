---
title: Extract Text from the Gear Type SmartArt Shape with Node.js via C++
linktitle: Extract Text from the Gear Type SmartArt Shape
type: docs
weight: 500
url: /nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Learn how to extract text from the Gear Type SmartArt Shape using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells can extract text from the Gear Type Smart Art Shape. In order to do so, you should first convert Smart Art Shape to Group Shape using the [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--) method. Then you should get the array of all the Individual Shapes forming the Group Shape using the [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--) method. Finally, you can iterate all of the Individual Shapes one by one in a loop and extract their text using the [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) property.

## **Extract Text from the Gear Type SmartArt Shape**

The following sample code loads the [sample Excel file](67338483.xlsx) that contains Gear Type Smart Art Shape. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for a reference.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **Console Output**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
