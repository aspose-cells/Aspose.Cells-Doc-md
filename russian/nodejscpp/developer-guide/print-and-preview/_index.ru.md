---  
title: Просмотр рабочей книги с помощью Node.js через C++  
linktitle: Просмотр рабочей книги 
type: docs  
weight: 70  
url: /ru/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells поддерживает печать и просмотр предварительного просмотра файлов Excel без установки Microsoft Excel с помощью Node.js через C++.  
---  

## **Предварительный просмотр печати**  

В некоторых случаях необходимо конвертировать Excel-файлы с миллионами страниц в PDF или изображения. Обработка таких файлов занимает много времени и ресурсов. В таких случаях функция предварительного просмотра печати книги и листа может оказаться полезной. Перед конвертацией таких файлов пользователь может проверить общее количество страниц и принять решение о необходимости конвертации. В этой статье рассматривается использование классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) для определения общего количества страниц.  

Aspose.Cells предоставляет функцию предварительного просмотра печати. Для этого API предоставляет классы [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/). Чтобы создать предварительный просмотр всей книги, создайте экземпляр класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/), передав в конструктор объекты [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Класс [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) предоставляет метод [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--), который возвращает количество страниц в сгенерированном предварительном просмотре. Аналогично классу [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/), класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) используется для создания предварительного просмотра печати для определенного листа. Для этого создайте экземпляр класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/), передав в конструктор [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) также предоставляет метод [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--), возвращающий количество страниц в предварительном просмотре.  

Следующий фрагмент кода демонстрирует использование классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) на примере [пример Excel-файла](94896177.xlsx).  

### **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

Следующим выводом является результат выполнения вышеприведенного кода.  

### **Вывод в консоль**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Продвинутые темы**  
- [Настройка шрифтов для отображения электронных таблиц](/cells/ru/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Преобразование рабочего листа в изображение - Удаление пустого места вокруг данных](/cells/ru/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Преобразование Рабочего листа в изображение и Рабочего листа в изображение по странице](/cells/ru/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Преобразование рабочего листа в изображение с использованием параметров ImageOrPrint](/cells/ru/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Экспорт диапазона ячеек листа в изображение](/cells/ru/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Извлечение изображений из листов с использованием параметров ImageOrPrintOptions](/cells/ru/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Генерация миниатюры листа](/cells/ru/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Вывод пустой страницы, когда нечего печатать](/cells/ru/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Настройки страницы и опции печати](/cells/ru/nodejs-cpp/page-setup-and-printing-options/)  
- [Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions](/cells/ru/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Отобразить Рабочий лист на графический контекст](/cells/ru/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Указание индивидуального или частного набора шрифтов для рендеринга книги](/cells/ru/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

