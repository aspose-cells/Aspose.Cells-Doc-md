---  
title: Рендеринг последовательности страниц с помощью свойств PageIndex и PageCount в ImageOrPrintOptions через Node.js и C++  
linktitle: Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions  
type: docs  
weight: 110  
url: /ru/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Узнайте, как рендерить определенные страницы Excel файла в изображения с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Вы можете рендерить последовательность страниц вашего Excel файла в изображения с помощью Aspose.Cells, используя свойства [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) и [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Эти свойства полезны, когда в вашем листе много страниц, например, тысячи страниц, но вам нужно рендерить только некоторые из них. Это не только экономит время обработки, но и сокращает потребление памяти процессом рендеринга.  

## **Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions**  

Следующий пример кода загружает [пример файла Excel](55541781.xlsx) и рендерит только страницы 4, 5, 6 и 7, используя свойства [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) и [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Вот сгенерированные страницы в результате кода.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleImageOrPrintOptions_PageIndexPageCount.xlsx"));
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Specify image or print options
// We want to print pages 4, 5, 6, 7
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setPageIndex(3);
opts.setPageCount(4);
opts.setImageType(AsposeCells.ImageType.Png);
// Create sheet render object
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);
// Print all the pages as images
for (let i = opts.getPageIndex(); i < sheetRender.getPageCount(); i++) {
sheetRender.toImage(i, path.join(outputDir, `outputImage-${i + 1}.png`));
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
