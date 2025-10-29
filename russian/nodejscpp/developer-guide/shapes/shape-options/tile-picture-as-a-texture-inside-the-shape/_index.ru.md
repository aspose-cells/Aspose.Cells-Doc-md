---  
title: Запечатлите изображение в виде текстуры внутри формы с помощью Node.js через C++  
linktitle: Размещение изображения в качестве текстуры внутри формы  
type: docs  
weight: 1700  
url: /ru/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Узнайте, как вставить небольшое изображение в виде текстуры внутри формы с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Когда изображение маленькое и не покрывает всю поверхность формы без потери качества, то у вас есть возможность повторить его. Повторение заполняет поверхность формы маленьким изображением, повторяя их, как плитку.  

## **Текстурное изображение внутри формы**  

Вы можете заполнить поверхность формы изображением и повторять его, используя свойство [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) и установив его значение **true**. Посмотрите следующий пример кода, его образец Excel-файла и скриншот для справки.  

## **Снимок экрана**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
