---  
title: Определить, является ли фигура Shape фигурой Smart Art с помощью Node.js через C++  
linktitle: Определить, является ли форма формой Smart Art  
type: docs  
weight: 400  
url: /ru/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Узнайте, как определить, является ли фигура в Excel Smart Art, используя Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Smart Art Shapes — это специальные фигуры в Microsoft Excel, позволяющие автоматически создавать сложные диаграммы. Вы можете определить, является ли фигура smart art или обычной, используя свойство [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--).  

## **Определение, является ли форма формой Smart Art**  

Следующий пример кода загружает [пример файла Excel](55541792.xlsx), содержащий фигуру Smart Art, как показано на этом скриншоте. Затем он выводит значение свойства [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) первой фигуры. Пожалуйста, смотрите вывод в консоли ниже.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **Вывод в консоль**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
