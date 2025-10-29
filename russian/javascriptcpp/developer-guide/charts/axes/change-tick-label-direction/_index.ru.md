---
title: Изменение направления меток деления с помощью JavaScript через C++
linktitle: Изменение направления меток делений
description: Узнайте, как изменить направление меток деления в Aspose.Cells for JavaScript через C++. Наше руководство поможет вам понять, как регулировать ориентацию меток деления на осях, включая горизонтальную, вертикальную и наклонную.
keywords: Aspose.Cells for JavaScript через C++, метки деления, направление, ориентация, оси, горизонтальная, вертикальная, наклонная.
type: docs
weight: 170
url: /ru/javascript-cpp/change-tick-label-direction/
---

## **Изменение направления меток делений**

Aspose.Cells позволяет изменять направление меток осей, используя свойство [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--). Свойство [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) принимает значение перечисления [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype). Перечисление [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) включает следующие члены:

- Горизонтальное
- Вертикальное
- Повернуть90
- Повернуть270
- Стековое

На следующем изображении приведено сравнение исходного и выходного файлов

### **Изображение исходного файла**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Изображение выходного файла**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Следующий фрагмент кода изменяет направление меток делений с Повернуть90 на Горизонтальное.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Исходные и выходные файлы можно загрузить по следующим ссылкам.

[Исходный файл](105480221.xlsx)

[Выходной файл](105480223.xlsx)
