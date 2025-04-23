---  
title: Защитить паролем проект VBA книги Excel с помощью Node.js через C++  
linktitle: Защита паролем проекта VBA книги Excel  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Узнайте, как защитить паролем проект VBA книги Excel, используя Aspose.Cells for Node.js via C++.  
---  

## **Защитите паролем проект VBA книги Excel в Node.js**  

Вы можете защитить паролем проект VBA (Visual Basic for Applications) книги с помощью Aspose.Cells, используя метод [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-).  

## **Образец кода**  

Следующий пример кода загружает [пример файла Excel](43352067.xlsm), получает доступ к его проекту VBA и защищает его паролем. В конце он сохраняет его как [выходной файл Excel](43352068.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

