---  
title: Отслеживание прогресса преобразования документа с помощью Node.js через C++  
linktitle: Отслеживание процесса конвертации документа  
type: docs  
weight: 970  
url: /ru/nodejs-cpp/track-document-conversion-progress/  
description: Узнайте, как отслеживать прогресс преобразования документа в файлах Excel с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Иногда преобразование больших файлов Excel может занять некоторое время. Во время этого процесса вы можете отображать прогресс преобразования документа вместо просто экрана загрузки, чтобы повысить удобство использования вашего приложения. Aspose.Cells for Node.js via C++ поддерживает отслеживание процесса преобразования документа, предоставляя интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) предоставляет методы [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) и [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-), которые вы можете реализовать в вашем собственном классе. Также вы можете контролировать, какие страницы рендерятся, как показано в пользовательском классе *TestPageSavingCallback*.  

## **Отслеживание прогресса конвертации документов**  

Следующий пример кода загружает [исходный файл excel](94896151.xlsx) и выводит его прогресс преобразования в консоль с помощью пользовательского класса *TestPageSavingCallback*, реализующего интерфейс [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback).  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Define TestPageSavingCallback class
class TestPageSavingCallback {
// Implement the required methods of this callback as needed
onPageSaving(pageIndex, fileName) {
console.log(`Saving page ${pageIndex} to ${fileName}`);
}
}

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "PagesBook1.xlsx"));

const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setPageSavingCallback(new TestPageSavingCallback());

workbook.save(path.join(outputDir, "DocumentConversionProgress.pdf"), pdfSaveOptions);
```  

Следующий код для пользовательского класса *TestPageSavingCallback*.  

```javascript
const AsposeCells = require("aspose.cells.node");

class TestPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages before page index 2.
if (args.getPageIndex() < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages after page index 8.
if (args.getPageIndex() >= 8) {
args.setHasMorePages(false);
}
}
}
```  

## **Вывод в консоль**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
