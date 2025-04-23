---  
title: Преобразование листа в изображение с помощью параметров ImageOrPrint с Node.js через C++  
linktitle: Преобразование Листа в изображение с использованием параметров ImageOrPrint  
type: docs  
weight: 90  
url: /ru/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Узнайте, как преобразовать лист в файл изображения и применить различные параметры изображений и печати с помощью Aspose.Cells for Node.js via C++.   
---  

{{% alert color="primary" %}}  
Этот документ разработан для подробного понимания того, как преобразовать лист в файл изображения и применить различные параметры изображения и печати для изображения, такие как разрешение, сжатие TIFF, формат изображения и качество страницы.  
{{% /alert %}}  

## **Сохранение листов в изображения - различные подходы**  

Иногда вам может понадобиться представить ваши рабочие листы в виде изображения. Вам может потребоваться вставлять изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вам нужен рабочий лист, отображенный как изображение, чтобы вы могли использовать его в другом месте. Aspose.Cells поддерживает конвертацию рабочих листов в файлы изображений. Также Aspose.Cells поддерживает установку различных параметров, таких как формат изображения, разрешение (вертикальное и горизонтальное), качество изображения и другие параметры изображения и печати.  

Возможно, вы попробуете автоматизацию Office, но у Office Automation есть свои недостатки. Есть несколько причин и проблем: безопасность, стабильность, масштабируемость и скорость, цена и функциональность. В общем, существует множество причин, главная из которых — что Microsoft настоятельно рекомендует не использовать автоматизацию Office через сторонние программы.  

В этой статье показано, как создать консольное приложение в Visual Studio. NET, выполнить преобразование листа в изображение с использованием различных параметров изображения и печати с помощью нескольких простых строк кода с использованием API Aspose.Cells.  

Класс [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) представляет лист, для которого необходимо рендерить изображения, и имеет перегруженный метод [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-), который может напрямую преобразовать лист в файлы изображений, указав желаемые атрибуты или параметры. Этот метод возвращает объект, который можно сохранить в виде файла изображения на диск или в поток. Поддерживаются различные форматы изображений, например BMP, PNG, GIF, JPEG, TIFF, EMF и другие.  

## **Использование Aspose.Cells для преобразования листа в изображение с использованием параметров ImageOrPrint.**  

### **Создание шаблонной книги в Microsoft Excel**  

Я создал новую книгу в MS Excel и добавил некоторые данные на первый лист. Теперь я преобразую лист шаблона файла "Лист1" в файл изображения "SheetImage.tiff" и применю различные параметры изображения, такие как горизонтальное и вертикальное разрешение, сжатие Tiff и т. Д.  

### **Загрузите и установите Aspose.Cells**  

Сначала необходимо [скачать](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Установите его на ваш компьютер для разработки. Все компоненты [Aspose](http://www.aspose.com/), при установке, работают в оценочном режиме. Режим оценки не имеет ограничения по времени и только накладывает водяные знаки на создаваемые документы.  

### **Создайте проект**  

Запустите выбранную вами среду разработки (например, Visual Studio). Создайте новое консольное приложение.  

### **Добавьте ссылки**  

Этот проект будет использовать Aspose.Cells. Поэтому необходимо добавить ссылку на компонент Aspose.Cells в ваш проект. Например, добавьте ссылку на ….\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node  

### **Преобразовать лист в файл изображения**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Опции конвертации**  

Можно сохранить конкретные страницы в изображение. Следующий код преобразует первый и второй рабочие листы в книге в изображения JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **Конвертация изображения с помощью WorkbookRender**  

TIFF изображение может содержать более одного кадра. Вы можете сохранить всю книгу как один TIFF-файл с несколькими кадрами или страницами:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


