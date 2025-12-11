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

Aspose.Cells can extract text from the Gear Type SmartArt shape. In order to do so, you should first convert the SmartArt shape to a GroupShape using the **Shape.getResultOfSmartArt()** method. Then you should get the array of all individual shapes forming the GroupShape using the **GroupShape.getGroupedShapes()** method. Finally, you can iterate over all individual shapes one by one in a loop and extract their text using the **Shape.getText()** method.  

## **Extract Text from the Gear Type SmartArt Shape**  

The following sample code loads the [sample Excel file](67338483.xlsx) that contains a Gear Type SmartArt shape. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for reference.  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing Gear Type SmartArt shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of the Gear Type SmartArt shape in the form of a GroupShape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes that make up the GroupShape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of Gear Type shapes and print them on the console.
for (let i = 0; i < shapes.length; i++) {
    const s = shapes[i];

    if (s.getType() === AsposeCells.AutoShapeType.Gear9 ||
        s.getType() === AsposeCells.AutoShapeType.Gear6) {
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
