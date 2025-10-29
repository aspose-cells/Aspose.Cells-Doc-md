---
title: Работа с эффектом отражения фигуры или диаграммы с помощью JavaScript через C++
linktitle: Работа с эффектом отражения формы или диаграммы
type: docs
weight: 210
url: /ru/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом отражения форм или диаграмм с помощью Script Aspose.Cells for Java через C++. Установите различные свойства отражения для достижения нужных результатов.
---

## **Возможные сценарии использования**
Aspose.Cells for JavaScript через C++ предоставляет свойство [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) вместе с классом [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) для работы с эффектом отражения формы или диаграммы. Класс [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) содержит следующие свойства, которые можно установить для получения различных результатов в соответствии с требованиями приложения.

- [ReflectionEffect.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflectionEffect.direction](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflectionEffect.distance](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflectionEffect.fadeDirection](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflectionEffect.rotWithShape](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflectionEffect.size](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflectionEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [ReflectionEffect.type](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **Работа с эффектом отражения формы или диаграммы**
Следующий пример кода загружает [исходный Excel-файл](5115424.xlsx) и получает доступ к первой форме на листе по умолчанию. Он устанавливает разные свойства [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) и затем сохраняет книгу в [выходной Excel-файл](5115423.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
