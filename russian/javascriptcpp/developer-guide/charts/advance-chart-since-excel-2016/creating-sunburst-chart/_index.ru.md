---
title: Как создать круговую диаграмму Sunburst с помощью JavaScript через C++
linktitle: Как создать диаграмму солнце
description: Узнайте, как создать диаграмму Sunburst в Aspose.Cells for JavaScript через C++, которая отображает данные в виде круга. Наше руководство поможет настроить различные свойства и форматирование вашей диаграммы, включая метки данных, легенды, цвета и многое другое.
keywords: Aspose.Cells for JavaScript через C++, Sunburst, создание, установка свойств, метки данных, легенда, формат, цвет, круг, визуализация данных.
type: docs
weight: 162
url: /ru/javascript-cpp/creating-sunburst-chart/
---

## **Возможные сценарии использования**
Круговые диаграммы хороши для сравнения пропорций внутри иерархии; однако круговые диаграммы не очень подходят для отображения уровней внутри иерархии между крупнейшими категориями и отдельными точками данных. Солнечная диаграмма значительно лучше показывает это. Солнечная диаграмма идеально подходит для отображения иерархических данных. Каждый уровень иерархии представлен одним кольцом или кругом, при этом внутреннее кольцо — вершина иерархии. Солнечная диаграмма без иерархических данных (один уровень категорий) выглядит похожей на кольцевую диаграмму. Однако солнечная диаграмма с несколькими уровнями категорий показывает, как внешние кольца связаны с внутренними. Эффективность солнечной диаграммы заключается в показе того, как одно кольцо делится на его составные части, в то время как другой тип иерархической диаграммы, график-дерево, отлично подходит для сравнения относительных размеров.

![todo:image_alt_text](sample.png)
## **Диаграмма созвездия**
После выполнения приведенного ниже кода вы увидите диаграмму созвездия, как показано ниже.

![todo:image_alt_text](result.png)
## **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](sunburst.xlsx) и генерирует [выходной файл Excel](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
