---
title: Зафиксировать верхний ряд(ы) листа Excel с помощью JavaScript через C++
linktitle: Заморозить строки
type: docs
weight: 190
url: /ru/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: В этой статье вы узнаете, как программно зафиксировать верхние строки листов Excel, используя библиотеку JavaScript с API C++.
keywords: Зафиксировать верхние строки, зафиксировать верхнюю строку с помощью JavaScript через C++.
---

## **Введение**

В этой статье мы научимся, как зафиксировать верхнюю строку(и). Когда у вас есть огромное количество данных под общим заголовком, вы не можете видеть заголовок при прокрутке вниз по листу. Вы можете зафиксировать верхний(е) строку(и), чтобы видеть зафиксированную часть даже при прокрутке остальной части данных. Вы легко сможете видеть заголовки в верхних строках.

## **Заморозить строки в Excel**

**![Заморозить верхнюю строку(и) в Excel](Freeze-Rows.png)**

1. Если хотите заморозить верхнюю(ие) строку(и), сначала выберите строку под строкой, которую нужно зафиксировать.
2. Нажмите Вид > Заморозка областей.
3. В выпадающем меню нажмите "Заморозить верхнюю строку".
4. Если вы прокрутите вниз, первая строка всегда останется сверху.

**![Замороженная строка](Frozen-Row.png)**

Как видите, 1-я строка зафиксирована; первая строка всегда остаётся вверху при прокрутке.

Фиксация строк позволяет вам просматривать большие данные без отслеживания ярлыка строки.

## **Зафиксировать строки с помощью Aspose.Cells for JavaScript через C++**
Легко зафиксировать строку(и) с помощью Aspose.Cells for JavaScript через C++. 
Пожалуйста, используйте метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) для фиксации строки(и) в выбранной строке.
1. Создать рабочую книгу для открытия файла или создать пустой файл.
2. Зафиксируйте первую строку с помощью метода Worksheet.freezePanes().
3. Сохранить файл.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Приложен [образец исходного файла Excel](../Freeze.xlsx).
