---
title: Расфиксировать строки или столбцы с помощью JavaScript через C++
linktitle: Снять замораживание панелей
type: docs
weight: 190
url: /ru/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно разморозить строки, столбцы или области Excel с помощью JavaScript API на C++.
keywords: Разморозить области, строки, столбцы, разморозить окно JavaScript через C++.
---

## **Введение**

В этой статье мы узнаем, как разморозить строки, столбцы и области. Если в файлах Excel листы заморожены, иногда необходимо разморозить их или отрегулировать замороженные строки, столбцы или области.


## **В Excel**

1. Нажмите вкладку Просмотр > Заморозить панели > Снять заморозку панелей.

**![снять замораживание панелей в Excel](Unfreeze-Panes.png)**




## **Разморозить строки, столбцы или области с помощью Script Aspose.Cells for Java через C++**
Просто разморозить области с помощью Script Aspose.Cells for Java через C++. Пожалуйста, используйте метод [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) для разморозки областей.

1. Создать Рабочую книгу для открытия замороженного файла.
2. Разморозить области с помощью метода Worksheet.unFreezePanes().
3. Сохранить файл.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Прикреплен [образец исходного файла Excel](Frozen.xlsx).
