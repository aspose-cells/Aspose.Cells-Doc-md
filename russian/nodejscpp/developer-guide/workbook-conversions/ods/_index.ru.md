---
title: Конвертация книги Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice calc) через Node.js
linktitle: Ods
type: docs
weight: 20
url: /ru/nodejs-cpp/convert-excel-to-ods/
description: Как конвертировать Excel в Ods (OpenOffice / LibreOffice Calc) или конвертировать Ods (OpenOffice / LibreOffice Calc) в Excel с помощью Aspose.Cells for Node.js via C++.
---

## **Об OpenDocument**
[Формат OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) - бесплатный и открытый формат файла для электронных офисных документов, изначально разработанный Sun для пакета Open Office. OpenDocument Spreadsheet (ODS) - это формат файла для документов Excel. OpenDocument в настоящее время является стандартом OASIS и ISO.

## **Преобразовать Ods (OpenOffice / LibreOffice Calc) в Excel**
Aspose.Cells for Node.js via C++ поддерживает загрузку Ods, Sxc и Fods, которые поддерживаются OpenOffice / LibreOffice Calc, и преобразует [Ods](book1.ods), [Sxc](book1.sxc) и [Fods](book1.fods) в файлы Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **Конвертировать Excel в Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Node.js via C++ поддерживает преобразование файлов Excel в файлы Ods, Sxc и Fods. Ниже приведен пример кода, показывающий, как преобразовать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Продвинутые темы**
- [Сохранить файл ODS в спецификациях ODF 1.1 и 1.2](/cells/ru/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Работа с фоном в файлах ODS](/cells/ru/nodejs-cpp/working-with-background-in-ods-files/)
