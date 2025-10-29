---
title: Блокировка водяного знака WordArt с помощью JavaScript через C++
linktitle: Блокировка водяного знака WordArt
type: docs
weight: 170
url: /ru/javascript-cpp/locking-wordart-watermark/
description: Узнайте, как блокировать водяные знаки WordArt с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  

API Aspose.Cells позволяют добавлять водяные знаки WordArt на лист так, что WordArt становится объектом, который можно перемещать и позиционировать на листе. Также возможно заблокировать объект WordArt для взаимодействия, такого как редактирование, перемещение и выбор. Эта статья объясняет использование метода [**Shape.lockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/javascript-cpp/shape/#lockedProperty-shapelocktype-boolean-) для блокировки некоторых аспектов водяного знака.

{{% /alert %}}  

API Aspose.Cells позволяют блокировать определённые аспекты водяного знака, чтобы ограничить или полностью заблокировать взаимодействие пользователя. Следующий пример кода демонстрирует использование Aspose.Cells for JavaScript через C++ для блокировки выделения, перемещения, редактирования и изменения размера водяного знака путём создания таблицы с нуля.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Watermark Example</h1>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Instantiate a new Workbook (empty)
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(
                AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL",
                "Arial Black",
                50,
                false,
                true,
                18,
                8,
                1,
                1,
                130,
                800
            );

            // Lock Shape Aspects
            wordart.isLocked = true;
            wordart.lockedProperty = {
                [AsposeCells.ShapeLockType.Selection]: true,
                [AsposeCells.ShapeLockType.ShapeType]: true,
                [AsposeCells.ShapeLockType.Move]: true,
                [AsposeCells.ShapeLockType.Resize]: true,
                [AsposeCells.ShapeLockType.Text]: true
            };

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;

            // Set the color (converted to property assignment with args object)
            wordArtFormat.oneColorGradient = {
                color: AsposeCells.Color.Red,
                variant: 0.2,
                style: AsposeCells.GradientStyleType.Horizontal,
                variant2: 2
            };

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            wordart.hasLine = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
