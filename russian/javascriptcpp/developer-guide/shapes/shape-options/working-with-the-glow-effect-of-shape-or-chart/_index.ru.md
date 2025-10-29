---
title: Работа с эффектом свечения фигуры или диаграммы с помощью JavaScript через C++
linktitle: Работа с эффектом свечения формы или диаграммы
type: docs
weight: 240
url: /ru/javascript-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом свечения фигур или диаграмм в JavaScript с использованием Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  
Aspose.Cells предоставляет свойство [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) вместе с классом [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) для работы с эффектом свечения фигуры или диаграммы. Класс [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) содержит следующие свойства, которые можно установить, чтобы добиться разных результатов согласно требованиям приложения.  

- [GlowEffect.size](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#size--)  
- [GlowEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#transparency--)  
- [GlowEffect.color](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)  

## **Работа с эффектом свечения формы или диаграммы**  
Следующий пример кода загружает [исходный excel-файл](5115407.xlsx) и получает первую фигуру в первом листе, устанавливает подполя свойства [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) и затем сохраняет рабочую книгу в [выходной excel-файл](5115414.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Glow Effect</title>
    </head>
    <body>
        <h1>Apply Glow Effect to First Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Apply Glow Effect</button>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the glow effect of the shape, Set its Size and Transparency properties
            const glowEffect = shape.glow;
            glowEffect.size = 30;
            glowEffect.transparency = 0.4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Glow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
