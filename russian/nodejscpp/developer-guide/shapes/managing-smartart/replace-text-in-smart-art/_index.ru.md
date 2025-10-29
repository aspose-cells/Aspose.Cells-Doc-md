---  
title: Заменить текст в smart art с помощью Node.js через C++  
linktitle: Замена текста в умном изображении  
type: docs  
weight: 1200  
url: /ru/nodejs-cpp/replace-text-in-smart-art/  
description: Узнайте, как заменить текст в smart art с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Smart art — это один из основных объектов в рабочей книге. Часто требуется обновлять текст в smart art. Aspose.Cells for Node.js via C++ предоставляет эту возможность, устанавливая свойство [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).  

Образец исходного файла можно загрузить по следующей ссылке:  

[SmartArt.xlsx](77496338.xlsx)  

## **Образец кода**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
