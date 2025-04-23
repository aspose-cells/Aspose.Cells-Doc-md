---  
title: Отрисовка градиентной заливки WordArt при преобразовании таблиц в HTML с помощью Node.js через C++  
linktitle: Отображение градиентной заливки для WordArt при преобразовании электронных таблиц в HTML  
type: docs  
weight: 90  
url: /ru/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Узнайте, как отрисовать градиентную заливку WordArt при преобразовании таблиц в HTML с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  
До версии Aspose.Cells 17.1 Aspose.Cells не отображал градиентную заливку WordArt при конвертации Excel файла в формат HTML. Начиная с версии Aspose.Cells 17.1, эта поддержка добавлена. Следующий скриншот показывает сравнение влияния градиентной заливки при конвертации файла с помощью Aspose.Cells 17.1 и более старой версии.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Отображение градиентного заполнения для WordArt при конвертации электронных таблиц в HTML**  
Следующий пример конвертирует [исходный файл Excel](22774111.xlsx) в [выходной HTML](22774109.zip). В исходном файле Excel есть объект WordArt с градиентной заливкой, как показано на скриншоте выше.  

## **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

