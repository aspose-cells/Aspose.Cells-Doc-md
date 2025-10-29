---  
title: Экспорт диапазона ячеек в листе в изображение с помощью Node.js через C++  
linktitle: Экспорт диапазона ячеек листа в изображение  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Возможные сценарии использования**  

Вы можете создать изображение листа с помощью Aspose.Cells for Node.js via C++. Однако иногда необходимо экспортировать только диапазон ячеек в листе в изображение. В этой статье объясняется, как это реализовать.  

## **Экспорт диапазона ячеек листа в изображение**  

Чтобы сделать изображение диапазона, установите область печати на нужный диапазон, затем установите все поля равными 0. Также установите [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) в **true**. Следующий код создает изображение диапазона D8:G16. Ниже приведен скриншот [примера файла Excel](47153160.xlsx), использованного в коде. Вы можете попробовать код с любым файлом Excel.  

## **Скриншот образца файла Excel и его экспортированного изображения**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Выполнение кода создает изображение только для диапазона D8:G16.  

**![todo:image_alt_text](Output-Image.png)**  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
