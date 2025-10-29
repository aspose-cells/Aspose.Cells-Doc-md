---  
title: Построение временной шкалы при преобразовании Excel в PDF с Node.js через C++  
linktitle: Отображение временной шкалы при преобразовании Excel в PDF  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Управление временными шкалами Excel файлов с Aspose.Cells for Node.js via C++.  
keywords: Отрисовка временной шкалы в PDF без Office 2013, Office 2016, Office 2019 и Office 365 с Node.js через C++  
---  

## **Отображение временной шкалы при преобразовании Excel в PDF**  
 Если у вас есть Excel-файл с примененной к нему временной шкалой, и вы хотите экспортировать его в PDF с сохранением настроек временной шкалы, Aspose.Cells for Node.js via C++ теперь поддерживает это по умолчанию. Просто экспортируйте Excel с временной шкалой в PDF, и созданный PDF отображает временную шкалу.  

Приведенный ниже образец кода загружает [образец Excel-файла](input.xlsx), содержащий существующую временную шкалу. Затем он сохраняет книгу как [файл PDF на выходе](out.pdf). На следующем снимке экрана сравниваются исходный файл Excel и сгенерированный PDF-файл.  

<img src="out.png" width="60%">  

## **Образец кода**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
