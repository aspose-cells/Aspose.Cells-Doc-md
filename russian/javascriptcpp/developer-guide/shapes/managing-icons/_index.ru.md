---
title: Добавление значков на лист с помощью JavaScript через C++
linktitle: Управление значками
type: docs
weight: 100
url: /ru/javascript-cpp/insert-svg-to-excel/
---

## Добавление значков на лист в Aspose.Cells for JavaScript через C++

Если вам нужно использовать [Aspose.Cells](https://products.aspose.com/cells/) для добавления 'значков' в файл Excel, то этот документ может предоставить вам некоторую помощь.

Интерфейс Excel, соответствующий операции вставки значка, выглядит следующим образом:

![](1.png)

- Выберите позицию для вставки значка на лист
- Левый щелчок *Вставка*->*Значки*
- В открывшемся окне выберите значок в красном прямоугольнике на рисунке выше
- Левый щелчок *Вставить*, он вставится в файл Excel.

Эффект будет следующий:

![](2.png)

Здесь мы подготовили *пример кода*, чтобы помочь вставить иконки с помощью [Aspose.Cells](https://products.aspose.com/cells/). Также есть необходимый [пример файла](sample.xlsx) и [ресурсный файл иконок](icon.zip). Мы использовали интерфейс Excel для вставки иконки с таким же визуальным эффектом, как у [ресурсного файла](icon.zip) в [примерном файле](sample.xlsx).

### JavaScript

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Когда вы выполните вышеуказанный код в своем проекте, вы получите следующие результаты:

![](3.png)
