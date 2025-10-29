---
title: Заморозьте первый(е) столбец(цы) листа Excel с помощью JavaScript на C++
linktitle: Заморозить столбцы
type: docs
weight: 190
url: /ru/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: Узнайте, как программно зафиксировать левую колонку(и) в Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: Заморозить левый столбцы, Заморозить первые столбцы, Заблокировать столбец(ы)
---

## **Введение**  

В этой статье мы узнаем, как зафиксировать левый(е) столбец(ы). Когда у вас есть большое количество данных в строке, вы можете не видеть левы�� столбцы при горизонтальной прокрутке листа. Вы можете зафиксировать и заблокировать первый(е) столбец(ы), чтобы видеть зафиксированную часть даже при прокрутке остальной части данных. Вы легко сможете видеть заголовки в левых столбцах.  

## **Заморозить столбцы в Excel**  

**![Заморозить левые столбцы в Excel](freeze-columns.png)**  

1. Если хотите заморозить левый(е) столбец(ы), сначала выберите столбец под столбцом, который необходимо зафиксировать.
2. Нажмите Вид > Заморозка областей.
3. В раскрывающемся меню нажмите "Заморозить первый столбец".
4. Если вы прокрутите вниз, первый столбец всегда останется слева.

**![Замороженный столбец](frozen-columns.png)**  

Как видите, первый столбец зафиксирован, и он всегда закреплён вверху при горизонтальной прокрутке.

Фиксация столбцов позволяет вам просматривать ваши длинные данные без необходимости отслеживать первый столбец.

## **Зафиксировать колонки с помощью Aspose.Cells for JavaScript через C++**  
Простое решение — зафиксировать первую(е) колонку(и) с помощью Aspose.Cells for JavaScript через C++.  
Пожалуйста, используйте метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) для заморозки столбцов в выбранном столбце.  
1. Создать рабочую книгу для открытия файла или создать пустой файл.
2. Зафиксируйте первый столбец с помощью метода Worksheet.freezePanes().
3. Сохранить файл.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
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

Прикреплен файл [образец исходного файла Excel](Freeze.xlsx).
