---  
title: Рендеринг сегментатора с помощью Node.js через C++  
linktitle: Рендеринг срезки  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/rendering-slicer/  
---  

## **Возможные сценарии использования**  
Aspose.Cells for Node.js via C++ поддерживает отображение форм сегментаторов. Если вы преобразуете лист в изображение или сохраняете книгу в PDF или HTML, вы увидите, что сегментаторы отображаются правильно.  

## **Рендеринг срезки**  
 Следующий пример кода загружает [пример файла Excel](67338479.xlsx), содержащий существующий сегментатор. Он преобразует лист в изображение, задав область печати, охватывающую только сегментатор. Полученное изображение — это [выходное изображение](67338480.png), показывающее прорисованный сегментатор. Как видно, сегментатор отображается корректно и выглядит так же, как в исходном файле Excel.  

![todo:image_alt_text](rendering-slicer_1)  
## **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
