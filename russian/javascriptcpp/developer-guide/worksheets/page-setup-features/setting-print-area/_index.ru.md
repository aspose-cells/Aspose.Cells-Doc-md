---
title: Как установить область печати с помощью JavaScript через C++
linktitle: Как установить область печати
type: docs
weight: 200
url: /ru/javascript-cpp/how-to-set-print-area/
description: В этой статье показан код, объясняющий, как установить область печати с помощью библиотеки Aspose.Cells для JavaScript через C++.
keywords: Ограничение диапазона печати, установка диапазона печати, очистка диапазона печати, установка и очистка диапазона печати с помощью JavaScript через C++, JavaScript через C++ Как установить область печати, установить и очистить область печати с помощью JavaScript через C++, Как очистить область печати в JavaScript, Как добавить область печати с помощью JavaScript через C++, Как удалить область печати с помощью JavaScript через C++, Как установить область печати в Excel, Как очистить область печати в Excel.
---

## **Возможные сценарии использования**

Настройка области печати в документе, таком как таблица Excel, помогает контролировать, какое содержимое будет включено при печати. Вот некоторые причины установить область печати:

1. Фокус на конкретных данных: вы можете распечатывать только наиболее важные разделы, избегая нежелательного содержимого.
1. Улучшенная раскладка: помогает организовать и разместить содержимое аккуратно на печатных страницах, избегая разрывов или нежелательных переносов страниц.
1. Экономия ресурсов: ограничивая область печати, вы можете сократить расход бумаги и чернил.
1. Профессиональное представление: обеспечивает печать лишь финальной и отредактированной версии данных, что особенно важно для отчетов или презентаций.
1. Последовательность: при повторной печати одного и того же документа наличие заданной области печати гарантирует равномерность результата.

<br>
Настройка области печати особенно полезна в больших документах, где необходимо поделиться или просмотреть только часть документа в печатном виде.

## **Как установить область печати в Excel**

Чтобы установить область печати в Excel, выполните следующие шаги:

1. Выберите ячейки: щелкните и перетащите, чтобы выбрать диапазон ячеек, который хотите установить как область печати.
1. Откройте вкладку Макет страницы: перейдите во вкладку "Макет страницы" на ленте в верхней части окна Excel.
1. Установить область печати: в группе "Настройка страницы" нажмите "Область печати". В выпадающем меню выберите "Установить область печати".
<br>
<img src="3.png" width=60% />

1. Добавление к области печати: если вы хотите добавить больше ячеек к существующей области печати, выберите дополнительные ячейки, перейдите в "Область печати" во вкладке "Макет страницы" и выберите "Добавить к области печати".

<br>
Это действие установит выбранные ячейки как область печати. При печати листа будет напечатана только эта определенная область.

## **Как очистить область печати в Excel**

Чтобы очистить область печати в Excel, выполните следующие шаги:

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.
1. Очистить область печати: В группе "Параметры страницы" нажмите "Область печати". В выпадающем меню выберите "Очистить область печати".
<br>
<img src="4.png" width=60% />

<br>
Это действие удалит любую ранее установленную область печати, позволив напечатать весь лист.

## **Что происходит после очистки области печати**

Очистка области печати в приложении Excel с помощью Aspose.Cells приведет к тому, что при печати будет включен весь лист. Если область печати установлена, будет напечатан только указанный диапазон ячеек. Очистив область печати, вы гарантируете, что не будет задан конкретный диапазон, и по умолчанию будет напечатан весь лист.

1. Поведение по умолчанию при печати: будет учитываться весь лист. Это означает, что все ячейки с данными или форматированием будут напечатаны.
1. Нет ограничений области печати: ранее заданные ограничения области печати будут удалены. Если были указаны конкретные строки и столбцы для печати, они больше не будут ограничены этими ограничениями.
1. Печать полного содержимого: весь содержимое, включая заголовки, колонтитулы и любые другие данные внутри листа, будет включено в задание на печать.

## **Как установить область печати с помощью Aspose.Cells for JavaScript через C++**

Для установки области печати в определённом листе: сначала загрузите [пример файла](input.xlsx), затем необходимо изменить свойство [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) объекта [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) для нужного листа. Установка этого свойства в диапазонную строку задаст область печати.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как очистить область печати с помощью Aspose.Cells for JavaScript через C++**

Чтобы очистить область печати в указанном листе: сначала загрузите [пример файла](input.xlsx), затем необходимо изменить свойство [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) объекта [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) для нужного листа. Присвоение этому свойству пустой строки очистит область печати.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Результат вывода:
<br>
<img src="2.png" width=60% />
