---
title: Избегайте пустых страниц в итоговом PDF, если нечего распечатывать, с помощью Node.js через C++
linktitle: Избегание пустой страницы в выходном PDF, когда нет ничего для печати
type: docs
weight: 30
url: /ru/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Узнайте, как избегать пустых страниц в выводном PDF, когда нечего печатать, с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Когда Excel-файл пустой, а пользователь сохраняет его как PDF с помощью Aspose.Cells for Node.js via C++, в итоговом PDF появляется пустая страница. Иногда это нежелательно. В Aspose.Cells есть свойство [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) для решения этой проблемы. Если установить его в значение **false**, то при отсутствии данных для печати возникнет исключение.

## **Избегание пустой страницы в выходном PDF, когда нет ничего для печати**

Следующий пример создает пустую рабочую книгу и сохраняет ее как PDF после установки свойства [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) в значение **false**. Так как для печати нечего, возникнет исключение, как показано ниже.

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **Исключение**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
