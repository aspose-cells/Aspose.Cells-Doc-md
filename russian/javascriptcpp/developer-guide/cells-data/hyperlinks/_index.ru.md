---
title: Вставка гиперссылок в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/javascript-cpp/insert-hyperlinks-to-excel/
description: Как вставлять гиперссылки в файл Excel с помощью библиотеки Aspose.Cells без MS Excel, используя JavaScript для C++.
keywords: Вставляйте гиперссылки в Excel с помощью JavaScript для C++, Добавлять или вставлять гиперссылки через JavaScript для C++, Добавлять или вставлять ссылку на URL через JavaScript для C++, Добавлять или вставлять ссылку в ячейку через JavaScript для C++, Добавлять ссылку на внешний файл через JavaScript для C++
---

{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 

## **Добавление гиперссылок**
 Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо через дизайнерские таблицы (таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие таблицы).

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), которая позволяет получить доступ к каждому листу Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет различные методы для добавления гиперссылок в файлы Excel.
## **Добавление ссылки на URL**
Класс [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) содержит коллекцию [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--). Каждый элемент в коллекции [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) представляет [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink). Добавляйте гиперссылки на URL, вызывая метод [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) коллекции [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). Метод [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL-адрес, адрес URL.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется в URL в пустую ячейку **A1**. В таких случаях, если ячейка пустая, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пустая и в нее добавляется гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие настройки форматирования к этой ячейке.

{{% /alert %}} 
## **Добавление ссылки на ячейку в том же файле**
Можно добавлять гиперссылки в ячейки того же файла Excel, вызывая метод [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) коллекции [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). Метод [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) работает как для внутренних, так и для внешних гиперссылок. Одна из перегрузок метода принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **Добавление ссылки на внешний файл**
Можно добавлять гиперссылки на внешние файлы Excel, вызывая метод [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-). Он принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/javascript-cpp/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/javascript-cpp/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/javascript-cpp/get-hyperlinks-in-range/)
