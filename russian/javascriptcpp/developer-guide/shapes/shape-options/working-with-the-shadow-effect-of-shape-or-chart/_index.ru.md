---
title: Работа с эффектом тени формы или диаграммы с помощью JavaScript через C++
linktitle: Работа с эффектом тени формы или диаграммы
type: docs
weight: 220
url: /ru/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом тени форм или диаграмм с помощью Script Aspose.Cells for Java через C++.
---

## **Возможные сценарии использования**  
Aspose.Cells for JavaScript через C++ предоставляет свойство [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) вместе с классом [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) для работы с эффектом тени формы или диаграммы. Класс [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) содержит следующие свойства, которые можно установить для получения различных результатов в соответствии с требованиями приложения.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.presetType](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.size](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [Эффект тени.прозрачность](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Работа с теневым эффектом формы или диаграммы**  
Следующий пример кода загружает исходный excel-файл (5115425.xlsx) и обращается к первой фигуре на первом листе, настраивает внутренние свойства свойства тени фигуры и сохраняет рабочую книгу в выходной excel-файл (5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
