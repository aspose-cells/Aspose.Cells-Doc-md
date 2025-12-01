---  
title: Working with the Glow Effect of Shape or Chart with Node.js via C++  
linktitle: Working with the Glow Effect of Shape or Chart  
type: docs  
weight: 240  
url: /nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Learn how to work with the glow effect of shapes or charts in Node.js using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
Aspose.Cells provides the [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) property along with [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) class to work with the glow effect of shape or chart. The [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) class contains the following properties which can be set to achieve different results as per application requirements.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Working with the Glow Effect of Shape or Chart**  
The following sample code loads the [source excel file](5115407.xlsx) and accesses the first shape in the first worksheet and sets the sub-properties of [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) property and then saves the workbook in [output excel file](5115414.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
