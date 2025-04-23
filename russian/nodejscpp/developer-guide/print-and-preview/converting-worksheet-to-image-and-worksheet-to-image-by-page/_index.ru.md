---  
title: Конвертация листа в изображение и листа по страницам с помощью Node.js через C++  
linktitle: Преобразование листа в изображение и Лист в изображение по странице  
type: docs  
weight: 80  
url: /ru/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Этот документ предназначен для предоставления разработчикам подробного понимания процесса преобразования листа в файл изображений и листов с несколькими страницами — в отдельные файлы изображений для каждой страницы.  

Иногда может потребоваться представить рабочие листы в виде изображений, например, для использования их в приложениях или веб-страницах. Возможно, вам понадобится вставить изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вам нужно отобразить рабочий лист в виде изображения. Aspose.Cells поддерживает преобразование рабочих листов в файлы изображений Microsoft Excel. Также Aspose.Cells поддерживает преобразование рабочей книги в несколько файлов изображений, по одному на страницу.  

Вы можете использовать автоматизацию Office для достижения этой цели, но у автоматизации Office есть свои недостатки. Существует несколько причин и проблем, например, безопасность, стабильность, масштабируемость/скорость, цена и функции. Короче говоря, есть много причин, но основная заключается в том, что сама компания Microsoft настоятельно рекомендует отказаться от автоматизации Office.  
{{% /alert %}}  

## **Использование Aspose.Cells for Node.js via C++ для преобразования листа в файл изображения**  

В этой статье объясняется, как создать консольное приложение, преобразовать лист в изображение и осуществить конвертацию листа в один образ для каждого листа с помощью API Aspose.Cells.  

Для этого необходимо импортировать в программу или проект несколько важных классов, связанных с функциями рендеринга, таких как [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/) и так далее. Класс [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) представляет лист, для которого создаются изображения, и имеет перегруженный метод [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-), который позволяет преобразовать лист напрямую в файлы изображений с любыми атрибутами или параметрами. Этот метод возвращает объект изображения, который можно сохранить на диск/в поток. Поддерживаются различные форматы изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF и другие.  

В этой статье объясняется, как:  

- Преобразовать рабочий лист в изображение  
- Преобразовать каждую страницу в рабочем листе в изображение  

Это задача показывает, как использовать Aspose.Cells для преобразования рабочего листа из шаблонной рабочей книги в файл изображения.  

### **Установка проекта**  

1. Сначала [скачайте Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Установите его на ваш компьютер для разработки. Все компоненты [Aspose](http://www.aspose.com/), при установке, работают в режиме оценки. Режим оценки не ограничен по времени и только накладывает водяные знаки на создаваемые документы. Теперь запустите среду разработки и создайте новое консольное приложение. В этом примере используется консольное приложение Node.js, но вы можете использовать любую платформу, интегрируемую с Node.js. Добавьте ссылку на Aspose.Cells в созданный проект.  

### **Преобразовать рабочий лист в файл изображения**  

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook.xlsx** (1 рабочий лист). Затем преобразуйте рабочий лист шаблона в файл изображения под названием SheetImage.jpg.  

Ниже приведен используемый компонентом код для выполнения этой задачи. Он преобразует Sheet1 в **Testbook.xlsx** в файл изображения, чтобы показать, насколько легко осуществляется это преобразование.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Использование Aspose.Cells for Node.js via C++ для преобразования листа в файл изображения по страницам**  

В этом примере показано, как использовать Aspose.Cells для преобразования листа из шаблонной книги, которая содержит несколько страниц, в один файл изображения на каждой странице.  

### **Конвертация листа в изображение по страницам**  

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook2.xlsx** (1 рабочий лист).  

Теперь преобразуйте рабочий лист шаблона Sheet1 в файлы изображений (по одному файлу на страницу). Поскольку я уже создал консольное приложение для выполнения этой задачи, я пропущу шаги создания этого консольного приложения и перейду непосредственно к шагам преобразования рабочего листа.  

Следующий код используется компонентом для выполнения задачи. Он конвертирует Sheet1 из Testbook2.xlsx в файлы изображений по страницам.  

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
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


