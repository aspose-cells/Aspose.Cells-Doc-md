---
title: Установка свойств ScaleCrop и LinksUpToDate встроенных свойств документа с помощью Node.js через C++
linktitle: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа
type: docs
weight: 320
url: /ru/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Узнайте, как устанавливать свойства ScaleCrop и LinksUpToDate встроенных свойств документа с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) и [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) — это два расширенных встроенных свойства документа, определённых внутри формата OpenXml. Их назначения:

## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **TRUE**, чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в **FALSE**, чтобы обрезать миниатюру документа и показать только секции, которые помещаются на экране.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **TRUE**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **FALSE**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
Следующий пример кода устанавливает расширенные встроенные свойства документа [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) и [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) у книги. Пожалуйста, проверьте сгенерированный файл Excel [выходной файл](5115500.xlsx), измените его расширение на .zip, распакуйте содержимое и просмотрите app.xml, как показано на скриншоте выше.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
