---
title: Чтение подписей осей после вычисления диаграммы с помощью JavaScript через C++
linktitle: Чтение меток оси после вычисления диаграммы
description: Узнайте, как читать подписи осей в Aspose.Cells for JavaScript через C++ после выполнения расчетов диаграммы. Наше руководство покажет, как получать и извлекать подписи осей, включая их форматирование и расположение.
keywords: Aspose.Cells for JavaScript, диаграмма, подписи осей, расчет, чтение, доступ, извлечение, форматирование, расположение, JavaScript через C++
type: docs
weight: 90
url: /ru/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Возможные сценарии использования**

Вы можете читать подписи осей вашей диаграммы после вычисления ее значений с помощью метода [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--). Пожалуйста, используйте свойство [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) для этой цели, которое вернет список подписей осей.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, см. следующий образец кода, который загружает [образец файла Excel](ReadAxisLabels.xlsx) и читает подписи осей категорий диаграммы на первом листе. Затем выводятся значения подписей осей на консоль. См. пример вывода на консоль приведенный ниже в качестве справки.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Вывод в консоль**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
