---  
title: Изображение с помощью Node.js через C++  
linktitle: Изображение  
type: docs  
weight: 300  
url: /ru/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells позволяет экспортировать лист из книги Excel и преобразовать его в различные форматы. В этой статье объясняется, как преобразовать лист в различные форматы.  
{{% /alert %}}  

## Преобразование книги в TIFF  

Файл Excel может содержать несколько листов с несколькими страницами. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) позволяет преобразовать Excel в TIFF с несколькими страницами. Также есть возможность регулировать множество параметров TIFF, например [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Разрешение ([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

В следующем фрагменте кода показано, как конвертировать Excel в TIFF с несколькими страницами. [Исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и [созданное изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) приложены для вашего справки.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Преобразование Рабочего листа в изображение**  

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и вычисления.  

Как разработчик вам может понадобиться представить рабочие листы в виде изображений. Например, вам может потребоваться использовать изображение рабочего листа в приложении или на веб-странице. Вам может понадобиться вставить изображение в документ Microsoft Word, файл PDF, презентацию PowerPoint или в другой тип документа. Просто говоря, вам нужно, чтобы рабочий лист был отображен в виде изображения, чтобы вы могли его использовать в другом месте.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

Класс [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) представляет рабочий лист для рендера в виде изображений. Он имеет перегруженный метод, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-), который может преобразовать рабочий лист в файл(ы) изображений с разными атрибутами или опциями. Он возвращает объект Buffer, вы можете сохранить изображение на диск или в поток. Поддерживаются несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Ниже приведен фрагмент кода, демонстрирующий, как преобразовать рабочий лист в Excel-файле в файл изображения.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
В настоящее время API для преобразования листов в изображения не поддерживает 3D-графики в виде пузырьков.  
{{% /alert %}}  

## **Преобразование Рабочего листа в SVG**  

SVG означает масштабируемую векторную графику. SVG является спецификацией на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, над разработкой которого работает Консорциум Всемирной паутины (W3C) с 1999 года.  

Aspose.Cells for Node.js via C++ с версии 7.1.0 умеет преобразовывать рабочие листы в SVG-изображения. Следующий пример показывает, как преобразовать рабочий лист Excel файла в SVG изображение.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Продвинутые темы**  
- [Конвертировать диаграмму Excel в изображение](/cells/ru/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
