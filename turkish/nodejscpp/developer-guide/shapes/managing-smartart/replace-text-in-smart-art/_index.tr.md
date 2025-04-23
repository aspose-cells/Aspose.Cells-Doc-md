---  
title: Node.js ile C++ kullanarak smart art taki metni değiştir  
linktitle: Akıllı sanatta metni değiştir  
type: docs  
weight: 1200  
url: /tr/nodejs-cpp/replace-text-in-smart-art/  
description: Aspose.Cells for Node.js via C++ kullanarak smart art taki metni değiştirmeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Smart art, çalışma kitabındaki ana nesnelerden biridir. Genellikle smart art'taki metni güncellemek gerekebilir. Aspose.Cells for Node.js via C++, bu özelliği [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) özelliğini ayarlayarak sağlar.  

Örnek kaynak dosyası aşağıdaki bağlantıdan indirilebilir:  

[SmartArt.xlsx](77496338.xlsx)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SmartArt.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(sourceFilePath);

const worksheets = wb.getWorksheets();
for (let i = 0; i < worksheets.getCount(); i++) 
{
const worksheet = worksheets.get(i);
const shapes = worksheet.getShapes();
for (let j = 0; j < shapes.getCount(); j++) 
{
const shape = shapes.get(j);
shape.setAlternativeText("ReplacedAlternativeText"); // This works fine just as the normal Shape objects do.
if (shape.isSmartArt()) 
{
const smartArtShapes = shape.getResultOfSmartArt().getGroupedShapes();
for (let k = 0; k < smartArtShapes.length; k++) 
{
const smartart = smartArtShapes[k];
smartart.setText("ReplacedText"); // This doesn't update the text in Workbook which I save to the another file.
}
}
}
}

const options = new AsposeCells.OoxmlSaveOptions();
options.setUpdateSmartArt(true);
const outputFilePath = path.join(dataDir, "outputSmartArt.xlsx");
wb.save(outputFilePath, options);
```  

