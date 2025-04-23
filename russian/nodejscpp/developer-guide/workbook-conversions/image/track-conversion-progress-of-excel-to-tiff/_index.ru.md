---
title: Отслеживание прогресса преобразования Excel в TIFF с помощью Node.js через C++
linktitle: Отслеживание процесса преобразования Excel в TIFF
type: docs
weight: 190
url: /ru/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Узнайте, как отслеживать прогресс преобразования файлов Excel в TIFF с помощью Aspose.Cells for Node.js via C++. Улучшите пользовательский опыт во время процесса преобразования.
---

## **Возможные сценарии использования**

Иногда преобразование больших файлов Excel может занять некоторое время. Во время этого процесса вы можете отображать прогресс преобразования документа вместо просто экрана загрузки, чтобы повысить удобство использования вашего приложения. Aspose.Cells for Node.js via C++ поддерживает отслеживание процесса преобразования документа, предоставляя интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) предоставляет методы [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) и [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-), которые вы можете реализовать в вашем собственном классе. Также вы можете контролировать, какие страницы рендерятся, как показано в пользовательском классе *TestPageSavingCallback*.

## **Отслеживание процесса преобразования Excel в TIFF**

Следующий пример кода загружает [исходный файл excel](95584311.xlsx) и выводит прогресс его преобразования в консоль с помощью пользовательского класса *TestPageSavingCallback*, реализующего интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Генерируемый выходной файл приложен для справки.

[Output File](95584312.tiff)

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

Следующий — код пользовательского класса *TestTiffPageSavingCallback*.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **Вывод в консоль**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
