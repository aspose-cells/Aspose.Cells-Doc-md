---
title: Получить текст уравнения трендлайна диаграммы с помощью JavaScript через C++
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++, чтобы получить текст уравнения трендлайна на диаграмме, созданной в Microsoft Excel. Наш гид покажет, как получить и извлечь уравнение трендлайна для дальнейшего анализа или отображения.
keywords: Aspose.Cells for JavaScript через C++, Трендлайн диаграммы, Текст уравнения, Microsoft Excel, Анализ данных, Отображение.
linktitle: Трендовые линии
type: docs
weight: 110
url: /ru/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендлайна диаграммы с помощью Aspose.Cells for JavaScript через C++. Aspose.Cells предоставляет свойство [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--), которое возвращает текст уравнения трендлайна диаграммы. Для использования этого свойства вам сначала нужно вызвать метод [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--).

{{% /alert %}}

Следующий скриншот показывает диаграмму с трендлайном и его текст уравнения, выделенный красным цветом. Мы получим этот текст, используя свойство [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) в следующем примере.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## JavaScript код для получения текста уравнения трендлайна диаграммы

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
