---  
title: Создайте прозрачное изображение листа Excel с Node.js через C++  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /ru/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Узнайте, как генерировать прозрачное изображение листа Excel с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Иногда вам может потребоваться создать изображение вашего листа как прозрачное изображение. Вы хотите применить прозрачность ко всем ячейкам без цвета заливки. Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--) для применения прозрачности к изображению листа. Когда это свойство имеет значение **false**, то ячейки без цвета заливки рисуются белым цветом, а когда оно имеет значение **true**, то ячейки без цвета заливки рисуются прозрачными.  

{{% /alert %}}  

На следующем изображении листа прозрачность не была применена. Ячейки без цвета заливки рисуются белым цветом.  

|**Вывод без прозрачности: фон ячейки белый**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Тогда как на следующем изображении листа прозрачность была применена. Ячейки без цвета заливки рисуются прозрачными.  

|**Вывод со включенной прозрачностью**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

Следующий образец кода генерирует прозрачное изображение из листа Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateTransparentImage.xlsx"));

// Apply different image or print options
const imgOption = new AsposeCells.ImageOrPrintOptions();
imgOption.setImageType(AsposeCells.ImageType.Png);
imgOption.setHorizontalResolution(200);
imgOption.setVerticalResolution(200);
imgOption.setOnePagePerSheet(true);

// Apply transparency to the output image
imgOption.setTransparent(true);

// Create image after applying image or print options
const sr = new AsposeCells.SheetRender(wb.getWorksheets().get(0), imgOption);
sr.toImage(0, path.join(outputDir, "outputCreateTransparentImage.png"));
```  

