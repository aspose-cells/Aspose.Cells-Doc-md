---
title: Преобразовать текстовые числовые данные в число
type: docs
weight: 900
url: /ru/javascript-cpp/convert-text-numeric-data-to-number/
description: Узнайте, как преобразовать числа, сохранённые как текст в Excel, в числа с помощью API Aspose.Cells for JavaScript через C++.
keywords: преобразование текста в число в Excel, JavaScript код для преобразования текста в число в Excel, преобразование числовых данных в Excel из текста в число, JavaScript код для преобразования числовых данных в Excel из текста в число, преобразование числового текста в число в Excel, JavaScript код для преобразования числового текста в число в Excel, преобразование числового текста в число с помощью JavaScript, преобразование числового текста в число в Excel с помощью JavaScript, преобразование числовых строк в числа в Excel с помощью JavaScript, преобразование числовых данных в Excel из текста в число с помощью JavaScript, преобразование числовых строк в число с помощью JavaScript
---

## **Возможные сценарии использования**
Иногда вам нужно преобразовать числовые данные, введённые как текст, в числа. Вы можете вводить числа как текст в Microsoft Excel, поставив апостроф перед числом, например **'12345**. Excel затем рассматривает число как строку. Aspose.Cells for JavaScript через C++ позволяет преобразовать строки в числа.


## Как преобразовать числа, хранящиеся как текст, в числа в Excel
Вы можете преобразовать числа, хранящиеся как текст, в числа, следуя нескольким простым шагам.
1. Выберите любую одиночную ячейку или диапазон ячеек, у которых есть индикатор ошибки в верхнем левом углу.
1. Рядом с выбранной ячейкой или диапазоном ячеек нажмите кнопку ошибки, которая появляется. В меню щелкните Преобразовать в число. 
<br>
<img src="4.png" width=70% />
1. Если кнопка предупреждения недоступна, выберите столбец с этой проблемой. Если вы не хотите преобразовать весь столбец, вы можете выбрать одну или несколько ячеек. Убедитесь, что выбранные вами ячейки находятся в одном столбце, иначе этот процесс не сработает. Кнопка Текст в столбцах обычно используется для разделения столбца, но ее также можно использовать для преобразования одного столбца текста в числа. На вкладке Данные щелкните Текст в столбцах.
<br>
<img src="1.png" width=70% />
1. Щелкните кнопку Завершить во всплывающем окне.
<br>
<img src="2.png" width=70% />
1. Числа, сохраненные как текст, преобразуются в числа.
<br>
<img src="3.png" width=70% />

## Как преобразовать числа, сохранённые как текст, в числа с помощью Aspose.Cells for JavaScript через C++
Aspose.Cells for JavaScript через C++ предоставляет метод [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--), который можно использовать для преобразования всех строковых или текстовых числовых данных в числа.

На следующем снимке экрана показаны строковые числа в ячейках **A1:A17**. Строковые числа выровнены влево.
<br>
<img src="5.png" width=70% />

Эти строковые числа были преобразованы в числа с использованием [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) на следующем скриншоте. Как вы можете видеть, они теперь выровнены по правому краю.
<br>
<img src="6.png" width=70% />

## JavaScript-код для преобразования строковых числовых данных в числа

Следующий образец кода показывает, как преобразовать все строковые числовые данные в фактические числа во всех листах книги.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
