---
title: Настройка страницы и параметры печати с помощью JavaScript через C++
linktitle: Настройка страницы и параметры печати
type: docs
weight: 60
url: /ru/javascript-cpp/page-setup-and-printing-options/
---

{{% alert color="primary" %}}  
Иногда разработчики нуждаются в настройке страницы и параметров печати для управления процессом печати. Настройки страницы и параметры печати предлагают различные варианты и полностью поддерживаются в Aspose.Cells.  

В этой статье показывается, как создать консольное приложение на JavaScript через C++ и применить настройки страниц и параметры печати к листу с помощью нескольких простых строк кода с использованием API Aspose.Cells.  
{{% /alert %}}  

## **Работа с настройками страницы и печати**  

Для этого примера мы создали рабочую книгу в Microsoft Excel и использовали Aspose.Cells для установки настроек страницы и параметров печати.  

### **Использование Aspose.Cells для установки параметров настройки страницы**  

Сначала создайте простой лист в Microsoft Excel. Затем примените к нему настройки страницы. При выполнении кода настройки страницы изменяются, как показано на скриншоте ниже.  

|**Выходной файл.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Создайте лист с данными в Microsoft Excel:  
   1. Откройте новую книгу в Microsoft Excel.  
   1. Добавьте некоторые данные.  
1. Установите параметры настройки страницы:  
   Примените параметры настройки страницы к файлу. Ниже приведено скриншоты параметров по умолчанию, до применения новых параметров.  

|**Параметры настройки страницы по умолчанию.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Скачайте и установите Aspose.Cells:  
   1. [Скачать](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript на C++.  
   1. Установите его на вашем компьютере для разработки.  
      Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.  
1. Создайте проект:  
   1. Запустите вашу среду JavaScript.  
   1. Создайте новое консольное приложение.  
      Этот пример покажет консольное приложение на JavaScript, но также можно использовать привязки C++.  
1. Добавьте ссылки:  
   1. В этом примере используется Aspose.Cells, поэтому добавьте ссылку на этот компонент в проект. Например:  
      …\Program Files\Aspose\Aspose.Cells\Bin\JavaScript-Cpp\Aspose.Cells.node  
1. Напишите приложение, которое вызывает API:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType, PaperSizeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access page setup as a property
            const pageSetup = worksheet.pageSetup;

            // Setting the orientation to Portrait
            pageSetup.orientation = PageOrientationType.Portrait;

            // Setting the number of pages to which the length of the worksheet will be spanned
            pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            pageSetup.fitToPagesWide = 1;

            // Setting the paper size to A4
            pageSetup.paperSize = PaperSizeType.PaperA4;

            // Setting the print quality of the worksheet to 1200 dpi
            pageSetup.printQuality = 1200;

            // Setting the first page number of the worksheet pages
            pageSetup.firstPageNumber = 2;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Настройка параметров печати**  

Настройки настройки страницы также предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать печать страниц листа. Они позволяют пользователям:  

- Выбирать конкретную область печати листа.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.  

Приведенный ниже пример применяет параметры печати к файлу, созданному в приведенном выше примере (PageSetup.xls). Снимок экрана ниже показывает параметры печати по умолчанию до применения новых параметров.  

|**Входной документ**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Выполнение кода изменяет параметры печати.  

|**Выходной файл**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            const pageSetup = worksheet.pageSetup;

            // Specifying the cells range (from A1 cell to E30 cell) of the print area
            pageSetup.printArea = "A1:E30";

            // Defining column numbers A & E as title columns
            pageSetup.printTitleColumns = "$A:$E";

            // Defining row numbers 1 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = AsposeCells.PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = AsposeCells.PrintErrorsType.PrintErrorsNA;

            // Setting the printing order of the pages to over then down
            pageSetup.order = AsposeCells.PrintOrderType.OverThenDown;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_Print_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
