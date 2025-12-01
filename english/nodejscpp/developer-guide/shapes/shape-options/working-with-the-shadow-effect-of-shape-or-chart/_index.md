---  
title: Working with the Shadow Effect of Shape or Chart with Node.js via C++  
linktitle: Working with the Shadow Effect of Shape or Chart  
type: docs  
weight: 220  
url: /nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Learn how to work with the shadow effect of shapes or charts using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
Aspose.Cells for Node.js via C++ provides the [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) property along with the [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) class to work with the shadow effect of shape or chart. The [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) class contains the following properties which can be set to achieve different results as per application requirements.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Working with the Shadow Effect of Shape or Chart**  
The following sample code loads the [source excel file](5115425.xlsx) and accesses the first shape in the first worksheet and sets the sub-properties of the [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) property and then saves the workbook in the [output excel file](5115411.xlsx).  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
