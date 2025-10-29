---
title: Чтение и управление графиками Excel 2016 с помощью JavaScript через C++
linktitle: Чтение и манипулирование диаграммами Excel 2016
description: Узнайте, как читать и управлять графиками Excel 2016 с помощью Script Aspose.Cells for Java через C++. Это руководство покажет, как получить доступ и изменять различные свойства диаграмм.
keywords: Script Aspose.Cells for Java через C++, графики Excel 2016, чтение, управление, метки данных, цвета серии, макеты, иерархическая визуализация, круговые диаграммы.
type: docs
weight: 48
url: /ru/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Возможные сценарии использования**  
Aspose.Cells теперь поддерживает чтение и изменение диаграмм Microsoft Excel 2016, которые отсутствуют в Microsoft Excel 2013 и более ранних версиях.  
## **Чтение и манипулирование диаграммами Excel 2016**  
Следующий пример кода загружает [исходный файл Excel](22774101.xlsx), содержащий графики Excel 2016 на первом листе. Он по очереди читает все графики и изменяет их заголовки в соответствии с типом графика. На следующем скриншоте показан исходный файл Excel до выполнения кода. Как видно, заголовок графика одинаков для всех графиков.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Ниже показан скриншот [выходного файла Excel](22774104.xlsx) после выполнения кода. Как видно, заголовок диаграммы изменен в соответствии с их типом диаграммы.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Образец кода**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Вывод в консоль**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Продвинутые темы**  
- [Создание водопадной диаграммы](/cells/ru/javascript-cpp/creating-waterfall-chart/)  
- [Создание диаграммы дерева](/cells/ru/javascript-cpp/creating-treemap-chart/)  
- [Создание диаграммы Sunburst](/cells/ru/javascript-cpp/creating-sunburst-chart/)
