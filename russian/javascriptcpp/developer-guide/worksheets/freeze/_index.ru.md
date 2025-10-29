---
title: Заморозить области листа Excel с помощью JavaScript через C++
linktitle: Замораживание областей
type: docs
weight: 190
url: /ru/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: В этой статье вы узнаете, как программно заморозить области листов Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: Зафиксировать панели, зафиксировать окно.
---

## **Введение**  

 В этой статье мы расскажем, как зафиксировать панели. Когда у вас есть большой объем данных с общей заголовком, вы не сможете видеть заголовки при прокрутке листа. Каждый запис содержит много данных. Вы можете зафиксировать панели, чтобы видеть зафиксированную часть, даже когда остальная часть данных прокручивается. Вы легко сможете видеть заголовки в верхних строках или первых столбцах. Зафиксировать и разблокировать панели — это лишь изменение вида данных, без изменения самих данных.  

## **В Excel**  

**![Замораживание областей в Excel](Freeze-panes.png)**  

1. Если хотите зафиксировать панели, закрепите строки и столбцы, сначала выберите ячейку (например, B2).  
2. Нажмите Вид > Заморозка областей.  
3. В выпадающем меню выберите Заморозить области.  
4. При прокрутке вниз или вправо первая строка и первый столбец останутся зафиксированными.  

**![Зафиксированные панели](Frozen-Panes.png)**  

Как видно, первая строка и столбец A заморожены, вторая строка — 32, а вторая видимая колонка — D.  

Заморозка панелей позволяет просматривать большие данные, не теряя из виду метки строк или столбцов.  

## **Заморозка областей с помощью Aspose.Cells for JavaScript через C++**  
Это просто — заморозить области с помощью Aspose.Cells for JavaScript через C++. Пожалуйста, используйте метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) для заморозки областей в выбранной ячейке.  
1. Создать рабочую книгу для открытия файла или создать пустой файл.  
2. Заморозка панелей с помощью метода Worksheet.freezePanes().  
3. Сохранить файл.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

Прикреплен файл [образец исходного файла Excel](Freeze.xlsx).
