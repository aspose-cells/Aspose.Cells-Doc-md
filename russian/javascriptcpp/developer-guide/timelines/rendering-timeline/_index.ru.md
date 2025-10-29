---
title: Отображение временной шкалы
type: docs
weight: 40
url: /ru/javascript-cpp/rendering-timeline/
description: Управление временными шкалами Excel файлов с помощью Aspose.Cells for JavaScript через C++.
keywords: Преобразование временной шкалы без использования Office 2013, Office 2016, Office 2019 и Office 365
---

## **Возможные сценарии использования**
Aspose.Cells for JavaScript через C++ поддерживает отображение фигуры временной шкалы без использования Office 2013, Office 2016, Office 2019 и Office 365. Если преобразовать ваш лист в изображение или сохранить рабочую книгу в формате PDF или HTML, вы увидите, что временные шкалы отображаются правильно.

## **Визуализация временной шкалы**
Следующий пример кода загружает [пример Excel-файла](input.xlsx), содержащего существующую временную шкалу. Получите объект фигуры по названию временной шкалы, а затем отрисуйте его в изображение с помощью метода Shape.ToImage(). Следующее изображение — это [выходное изображение](out.png), показывающее отрисованную временную шкалу. Как видно, временная шкала была правильно отображена и выглядит так же, как в примере Excel-файла.

![todo:image_alt_text](out.png)
### **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
