---
title: Как преобразовать HTML в PDF с помощью Node.js через C++
linktitle: Как конвертировать HTML в PDF
type: docs
weight: 80
url: /ru/nodejs-cpp/convert-html-to-pdf/
description: Этот раздел показывает, как преобразовать HTML в PDF и MHTML в PDF с помощью Aspose.Cells for Node.js via C++.
keywords: Конвертация HTML и MHTML в PDF через Node.js и C++. 
---

## **Обзор**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>конвертировать HTML в PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML в PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Конвертация HTML в PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Как конвертировать HTML в PDF</a></li>
</ul>

## **Преобразование HTML в PDF в Node.js**
Как конвертировать HTML в PDF? С помощью библиотеки [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) вы легко сможете программно преобразовать HTML в PDF несколькими строками кода. Aspose.Cells for Node.js via C++ способен создавать кроссплатформенные приложения с возможностью генерировать, изменять, конвертировать, рендерить и печатать все файлы Excel.

## **JavaScript Конвертация HTML в PDF**
Пример кода JavaScript показывает, как конвертировать HTML-документ в PDF с помощью [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/).
1. Инициализируйте объект [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/).
1. Сохранить выходной PDF-документ, вызвав метод Workbook.save().

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.html");

// Loads the workbook which contains hidden external links
const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
const book = new AsposeCells.Workbook(filePath, options);
book.save("out.pdf");
```

## **Попробуйте конвертировать HTML в PDF онлайн**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">«HTML в PDF»</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
