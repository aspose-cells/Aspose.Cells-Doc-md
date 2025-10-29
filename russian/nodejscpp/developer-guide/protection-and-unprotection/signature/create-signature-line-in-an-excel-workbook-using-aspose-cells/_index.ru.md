---  
title: Создать линию подписи в рабочей книге Excel с помощью Aspose.Cells for Node.js via C++  
linktitle: Создать строку подписи в книге Excel с помощью Aspose.Cells  
type: docs  
weight: 150  
url: /ru/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: В этой статье описывается, как создать линию подписи в рабочей книге Excel с помощью Node.js и Aspose.Cells for Node.js via C++.  
keywords: Создать линию подписи в рабочей книге Excel с помощью Node.js через C++, как создать линию подписи в рабочей книге Excel, как добавить линию подписи, как добавить линию подписи в файл Excel.  
---  

## **Введение**  

Microsoft Excel предоставляет возможность добавлять **Строку подписи** в рабочие книги Excel. Вы можете добавить строку подписи, нажав на вкладку **Вставка** и затем выбрав **Строка подписи** из группы **Текст**.  

## **Как создать строку подписи для Excel**  

Aspose.Cells for Node.js via C++ также предоставляет эту функцию и реализовало свойство [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) для этой цели. В этой статье объясняется, как использовать это свойство для добавления линии подписи в документ с помощью Aspose.Cells.  

Следующий пример кода добавляет линию подписи с использованием свойства [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) и сохраняет рабочую книгу.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
