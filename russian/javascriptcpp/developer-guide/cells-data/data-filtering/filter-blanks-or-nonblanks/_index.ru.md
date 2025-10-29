---
title: Как фильтровать пустые или непустые ячейки
type: docs
weight: 85
url: /ru/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: Узнайте, как фильтровать пустые и непустые значения с помощью скрипта Aspose.Cells for Java через API C++.
keywords: Отфильтровать пустые, отфильтровать непустые, отфильтровать пустые в листе, отфильтровать непустые в листе, отфильтровать пустые в Excel, отфильтровать непустые в Excel, отфильтровать пустые и непустые в Excel
---

## **Возможные сценарии использования**
Фильтрация данных в Excel – это ценный инструмент, который улучшает анализ, исследование и презентацию данных, позволяя пользователям сосредоточиться на конкретных подмножествах данных в соответствии с их критериями, что делает общий процесс манипулирования данными и их интерпретации более эффективным и эффективным.

## **Как фильтровать пустые или непустые ячейки в Excel**
В Excel вы можете легко фильтровать пустые или непустые ячейки с помощью опций фильтрации. Вот как это можно сделать:

### **Как фильтровать пустые ячейки в Excel**
1. Выберите диапазон: Щелкните на букве заголовка столбца, чтобы выбрать весь столбец или выберите диапазон, в котором хотите отфильтровать пустые ячейки.
1. Откройте меню Фильтр: перейдите на вкладку "Данные" на ленте.
<br>
<image src="1.png" width="70%" />
1. Варианты фильтра: нажмите кнопку "Фильтр". Это добавит стрелки фильтрации к выбранному диапазону.
1. Отфильтруйте пустые ячейки: Щелкните на стрелке фильтра в столбце, который вы хотите отфильтровать пустыми. Снимите все параметры, кроме «Пустые», и нажмите OK. Это отобразит только пустые ячейки в этом столбце.
<br>
<image src="2.png" width="70%" />
1. Результат следующий:
<br>
<image src="3.png" width="70%" />

### **Как фильтровать непустые ячейки в Excel**
1. Выберите диапазон: нажмите на букву заголовка столбца, чтобы выбрать весь столбец, или выберите диапазон, в котором хотите отфильтровать непустые ячейки.
1. Откройте меню Фильтр: перейдите на вкладку "Данные" на ленте.
<br>
<image src="1.png" width="70%" />
1. Варианты фильтра: нажмите кнопку "Фильтр". Это добавит стрелки фильтрации к выбранному диапазону.
1. Фильтрация непустых ячеек: нажмите на стрелку фильтра в столбце, который хотите отфильтровать по непустоте. Снимите выбор со всех вариантов, кроме "Непустые" или "Пользовательский", и установите условия соответственно. Нажмите ОК. Это отобразит только ячейки, которые не пустые в этом столбце.
<br>
<image src="4.png" width="70%" />
1. Результат следующий:
<br>
<image src="5.png" width="70%" />

## **Как фильтровать пустые значения с помощью скрипта Aspose.Cells for Java через C++**
Если столбец содержит текст, например, некоторые ячейки пусты, и требуется фильтр, чтобы выбрать только те строки, где есть пустые ячейки, функции [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) и [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) можно использовать, как показано ниже. 

Пожалуйста, ознакомьтесь с примерным кодом, загружающим [образец Excel-файла](sample.xlsx), который содержит некоторые фиктивные данные. Примерный код использует три метода для фильтрации пустот. Затем он сохраняет книгу как [выходной Excel-файл](FilteredBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **Как фильтровать непустые значения с помощью скрипта Aspose.Cells for Java через C++**

Посмотрите следующий пример кода, который загружает [пример Excel файла](sample.xlsx), содержащий некоторые фиктивные данные. После загрузки файла вызовите функцию [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-) для фильтрации непустых данных и сохраните рабочую книгу как [выходной Excel файл](FilteredNonBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
