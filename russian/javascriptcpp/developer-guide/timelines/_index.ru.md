---
title: Вставить TimeLine
linktitle: Линии времени
type: docs
weight: 170
url: /ru/javascript-cpp/create-timeline/
description: Узнайте, как создать временную шкалу с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Вместо настройки фильтров для отображения дат, вы можете использовать временную шкалу сводной таблицы — динамический фильтр, который позволяет легко фильтровать по дате/времени и увеличивать нужный период с помощью ползунка. Microsoft Excel позволяет создать временную шкалу, выбрав сводную таблицу и щелкнув *Вставка > Временная шкала*. Aspose.Cells for JavaScript через C++ также позволяет создавать временные шкалы с помощью метода [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Создать временную линию для сводной таблицы**

Смотрите следующий пример кода. Он загружает [пример файла Excel](input.xlsx), содержащий сводную таблицу. Затем он создает временную шкалу на основе первого базового поля сводной таблицы. В конце он сохраняет книгу в формате [выходного XLSX](output.xlsx). Следующее изображение показывает созданную временную шкалу в выходном файле Excel с помощью Aspose.Cells for JavaScript через C++.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
