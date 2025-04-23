---  
title: Преобразовать Excel в Pdf, изображение и другие форматы  
linktitle: Преобразования рабочих книг  
type: docs  
weight: 65  
url: /ru/nodejs-cpp/convert-workbook-to-different-formats/  
description: Конвертируйте файлы Excel в Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML и другие с помощью Node.js через C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells поддерживает конвертацию между множеством форматов. Технически, конвертация означает загрузку книги в одном формате файла и сохранение ее в другом.  
{{% /alert %}}  

## **Конвертировать книгу Excel в PDF**  
Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.  

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Преобразовать рабочую книгу Excel в JPG**  
Aspose.Cells поддерживает конвертацию файлов Excel в JPG. Ниже показан пример кода, как сохранить книгу в JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Преобразование рабочей книги Excel в изображение**  
Aspose.Cells поддерживает конвертацию файлов Excel в изображения. Ниже приведён пример кода, как сохранить книгу как изображение.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Преобразование рабочей книги Excel в XPS**  
Формат документа XPS состоит из структурированной разметки XML, которая определяет макет документа и визуальное оформление каждой страницы, а также правила отображения для распределения, архивирования, отображения, обработки и печати документов.  

Язык разметки для XPS является подмножеством XAML, что позволяет ему включать элементы векторной графики в документы, используя XAML для разметки примитивов Windows Presentation Foundation (WPF). Используемые элементы описаны в терминах путей и других геометрических примитивов.  

Файл XPS, на самом деле, является файлом UNICODE ZIP-архива с использованием упаковочных соглашений Open Packaging Conventions, содержащий файлы, из которых состоит документ. Эти включают XML-файл разметки для каждой страницы, текст, встроенные шрифты, растровые изображения, 2D векторную графику, а также информацию о цифровом управлении правами. Содержимое файла XPS можно изучить, просто открыв его в приложении, которое поддерживает ZIP-файлы.  

Начиная с Aspose.Cells 6.0.0, поддерживается преобразование Microsoft Excel в XPS.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Конвертация Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc)**  
Aspose.Cells поддерживает конвертацию файлов Excel в Ods, Sxc и Fods. Ниже показан пример, как конвертировать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Преобразование книги Excel в файлы MHTML**  
MHTML объединяет обычный HTML с внешними ресурсами (то есть контентом, который обычно ссылается, таким как изображения, анимации, звук и т. д.) в один файл. Они используются для электронных писем с расширением файла .mht.  

Aspose.Cells поддерживает чтение и запись файлов MHTML.  

В приведенном ниже примере кода показано, как сохранить книгу в формате MHTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Преобразование книги Excel в HTML**  
API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions), чтобы дать возможность управлять несколькими аспектами итогового HTML.  

Приведенный ниже пример кода демонстрирует, как сохранить рабочую книгу в файл HTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **Установка параметров изображения для HTML**  
Начиная с версии 8.0.2, Aspose.Cells предоставил [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) для класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions), что позволяет разработчикам задавать предпочтения по изображениям при сохранении таблиц в HTML.  

Ниже приведены подробности некоторых настроек изображения, которые могут быть применены,  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): указывает тип изображения. Обратите внимание, что все формы, включая диаграммы, отображаются как изображения в выходном HTML.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): Определяет качество изображения от 0 до 100, когда [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) указан как Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): получает или задает вертикальное разрешение изображения в точках на дюйм.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): получает или задает горизонтальное разрешение изображения в точках на дюйм.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): получайте или задавайте тип сжатия изображений, когда [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) указан как Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): указывает, должен ли фон изображения быть прозрачным, когда указан формат изображения как Png.  

## **Преобразование электронной таблицы Excel в Markdown**  
API Aspose.Cells поддерживает экспорт таблиц в формат Markdown. Чтобы экспортировать активный лист в Markdown, передайте [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) для указания дополнительных настроек экспорта листа в Markdown.  

Следующий пример кода демонстрирует экспорт активного листа в Markdown с помощью перечисления [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Пожалуйста, посмотрите сгенерированный [файл Markdown](md_sample.txt) как пример.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Конвертировать книгу Excel в JSON**  
API Aspose.Cells поддерживает преобразование книги в Json (JavaScript Object Notation).  

Следующий пример кода демонстрирует экспорт активного листа в Json с помощью перечисления [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Посмотрите код, чтобы увидеть преобразование [исходного файла](Book1.xlsx) в [выходной Json](Book1.Json).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Преобразовать Excel в XML**  
Aspose.Cells поддерживает преобразование книги Excel в XML документ электронной таблицы Excel 2003 и обычные данные XML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Преобразовать книгу Excel в TIFF**  
Aspose.Cells поддерживает конвертацию книги в файл TIFF.  

Ниже приведен фрагмент кода, показывающий, как преобразовать Excel в TIFF:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Преобразовать книгу Excel в DOCX**  
API Aspose.Cells поддерживает преобразование таблиц в формат DOCX. Чтобы экспортировать книгу в DOCX, передайте [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) для указания дополнительных настроек экспорта листа в DOCX.  

Следующий пример кода демонстрирует экспорт активного листа в DOCX с помощью перечисления [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Посмотрите сгенерированный [файл DOCX](Book1.docx) как пример.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Преобразовать книгу Excel в PPTX**  
API Aspose.Cells поддерживает преобразование таблиц в формат PPTX. Чтобы экспортировать книгу в PPTX, передайте [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) для указания дополнительных настроек экспорта листа в PPTX.  

Следующий пример кода демонстрирует экспорт активного листа в PPTX с помощью перечисления [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Посмотрите сгенерированный [файл PPTX](Book1.pptx) как пример.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Преобразовать рабочую книгу Excel в EPUB**  
API Aspose.Cells поддерживает преобразование таблиц в формат EPUB. Чтобы экспортировать книгу в EPUB, передайте [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) для указания дополнительных настроек экспорта листа в Epub.  

Следующий пример кода демонстрирует экспорт активного листа в EPUB с помощью перечисления [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Преобразовать рабочую книгу Excel в AZW3**  
API Aspose.Cells поддерживает преобразование таблиц в формат AZW3. Чтобы экспортировать книгу в AZW3, передайте [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) для указания дополнительных настроек экспорта листа в AZW3.  

Следующий пример кода демонстрирует экспорт активного листа в AZW3 с помощью перечисления [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Продвинутые темы**  
- [Преобразование версии XLSB в XLSM](/cells/ru/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/ru/nodejs-cpp/convert-excel-to-html/)  
- [Изображение](/cells/ru/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/ru/nodejs-cpp/convert-workbook-to-json/)  
- [Преобразование Excel-книги в Ods, Sxc и Fods (OpenOffice / LibreOffice calc).](/cells/ru/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/ru/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Преобразование Excel в CSV, TSV и Txt](/cells/ru/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Отслеживание прогресса конвертации документов](/cells/ru/nodejs-cpp/track-document-conversion-progress/)  
- [Преобразование CSV, TSV и TXT в Excel](/cells/ru/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

