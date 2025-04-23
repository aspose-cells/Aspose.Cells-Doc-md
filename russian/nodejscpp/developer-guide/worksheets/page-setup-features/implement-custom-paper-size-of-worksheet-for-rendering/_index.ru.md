---  
title: Реализовать пользовательский размер бумаги листа для отображения с помощью Node.js через C++  
linktitle: Реализация пользовательского размера бумаги для рендеринга листа  
type: docs  
weight: 70  
url: /ru/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Эта статья объясняет, как использовать API Node.js через C++, чтобы установить пользовательский размер бумаги для нужных вам листов при программной конвертации файла Excel в PDF.  
keywords: установить пользовательский размер бумаги при преобразовании Excel в PDF с помощью Node.js через C++  
---  

## **Возможные сценарии использования**  

В MS Excel нет прямой опции для создания пользовательских размеров бумаги, однако вы можете установить пользовательский размер бумаги для нужных листов при преобразовании файла Excel в PDF. В этом документе объясняется, как задать пользовательский размер бумаги листа с помощью API Aspose.Cells.  

## **Настройка пользовательского размера бумаги для отображения на листе**  

Aspose.Cells позволяет реализовать желаемый размер бумаги листа. Вы можете использовать метод [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) класса [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/), чтобы задать пользовательский размер страницы. В следующем примере кода показано, как задать пользовательский размер бумаги для первого листа книги. Также смотрите [выходной PDF](45056028.pdf), созданный этим кодом, для справки.  

## **Снимок экрана**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

