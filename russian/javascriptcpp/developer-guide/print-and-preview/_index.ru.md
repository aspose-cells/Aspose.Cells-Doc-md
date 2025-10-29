---
title: Предварительный просмотр книги с помощью JavaScript через C++
linktitle: Просмотр рабочей книги 
type: docs
weight: 70
url: /ru/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells поддерживает печать и предварительный просмотр файлов Excel без установки Microsoft Excel, через JavaScript с помощью C++.
---

## **Предварительный просмотр печати**  

В некоторых случаях необходимо конвертировать Excel-файлы с миллионами страниц в PDF или изображения. Обработка таких файлов занимает много времени и ресурсов. В таких случаях функция предварительного просмотра печати книги и листа может оказаться полезной. Перед конвертацией таких файлов пользователь может проверить общее количество страниц и принять решение о необходимости конвертации. В этой статье рассматривается использование классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) для определения общего количества страниц.  

Aspose.Cells предоставляет функцию предварительного просмотра печати. Для этого API предоставляет классы [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/). Чтобы создать предварительный просмотр всей книги, создайте экземпляр класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/), передав в конструктор объекты [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). Класс [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) предоставляет метод [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--), который возвращает количество страниц в сгенерированном предварительном просмотре. Аналогично классу [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/), класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) используется для создания предварительного просмотра печати для определенного листа. Для этого создайте экземпляр класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/), передав в конструктор [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). Класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) также предоставляет метод [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--), возвращающий количество страниц в предварительном просмотре.  

Следующий фрагмент кода демонстрирует использование классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) на примере [пример Excel-файла](94896177.xlsx).  

### **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

Следующим выводом является результат выполнения вышеприведенного кода.  

### **Вывод в консоль**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Продвинутые темы**  
- [Настройка шрифтов для отображения электронных таблиц](/cells/ru/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Преобразование рабочего листа в изображение - Удаление пустого места вокруг данных](/cells/ru/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Преобразование Рабочего листа в изображение и Рабочего листа в изображение по странице](/cells/ru/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Преобразование рабочего листа в изображение с использованием параметров ImageOrPrint](/cells/ru/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Экспорт диапазона ячеек листа в изображение](/cells/ru/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Извлечение изображений из листов с использованием параметров ImageOrPrintOptions](/cells/ru/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Генерация миниатюры листа](/cells/ru/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Вывод пустой страницы, когда нечего печатать](/cells/ru/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Настройки страницы и опции печати](/cells/ru/javascript-cpp/page-setup-and-printing-options/)  
- [Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions](/cells/ru/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Отобразить Рабочий лист на графический контекст](/cells/ru/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Указание индивидуального или частного набора шрифтов для рендеринга книги](/cells/ru/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
