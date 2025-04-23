---
title: Определить, является ли размер бумаги листа автоматическим, с помощью Node.js через C++
linktitle: Определение автоматического размера бумаги листа
type: docs
weight: 90
url: /ru/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Этот пример показывает, как использовать API Node.js с C++ дополнениями для определения, автоматически ли установлен размер бумаги листа программным путем.
keywords: определить, является ли размер бумаги листа автоматическим с помощью Node.js через C++
---

## **Возможные сценарии использования**

Часто размер бумаги листа устанавливается автоматически. Когда он автоматический, он обычно задан как *Letter*. Иногда пользователь устанавливает размер бумаги по своим требованиям. В этом случае размер бумаги не является автоматическим. Вы можете определить, автоматический ли размер бумаги листа, используя свойство [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--).

## **Определение автоматического размера бумаги листа**

В приведенном ниже образце кода загружаются следующие два файлы Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

и определяется, является ли размер бумаги их первого листа автоматическим или нет. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим или нет, через окно настройки страницы, как показано на этом скриншоте.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **Вывод в консоль**

Вот вывод в консоль приведенного выше образца кода при выполнении с данными образцами файлов Excel.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
