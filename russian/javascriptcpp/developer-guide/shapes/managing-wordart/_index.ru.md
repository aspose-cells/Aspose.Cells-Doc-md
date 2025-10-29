---
title: Добавление WordArt Watermark в лист с помощью JavaScript через C++
linktitle: Управление WordArt
type: docs
weight: 180
url: /ru/javascript-cpp/add-wordart-watermark-to-worksheet/
description: Узнайте, как добавить WordArt в качестве фона водяного знака на лист с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}} 

Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок сверху файла, украсьте текст или сделайте его соответствующим предварительно заданной форме или примените текст к листу Excel в качестве фонового водяного знака. WordArt становится объектом, который можно перемещать или позиционировать на листе, добавляя украшения.

{{% /alert %}} 

Приведенный ниже пример показывает, как добавить форму WordArt, чтобы установить водяной знак на фон для листа.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Добавление словесного искусства текста с встроенными стилями](/cells/ru/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [Блокировка водяного знака WordArt](/cells/ru/javascript-cpp/locking-wordart-watermark/)
- [Установить предварительный стиль WordArt для текста формы](/cells/ru/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
