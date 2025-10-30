---
title: Gestionar títulos de gráficos de Excel con JavaScript vía C++
description: Aprenda cómo usar Aspose.Cells for JavaScript vía C++ para agregar y formatear títulos de gráficos y ejes en Microsoft Excel. Nuestra guía demostrará cómo establecer diferentes tipos de títulos, ajustar su apariencia y modificar los títulos de los ejes para una mejor representación y claridad de los datos.
keywords: Aspose.Cells for JavaScript vía C++, títulos de gráficos, títulos de ejes, Microsoft Excel, representación de datos, apariencia.
linktitle: Títulos
type: docs
weight: 50
url: /es/javascript-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

En los gráficos de Excel, hay 2 tipos de títulos:
1. Título del Gráfico 
1. Títulos de Ejes

{{% /alert %}}

## **Opciones de Títulos**
Aspose.Cells for JavaScript vía C++ también permite gestionar los títulos del gráfico en tiempo de ejecución. Con el objeto [Title](https://reference.aspose.com/cells/javascript-cpp/title/) puedes cambiar el texto, la fuente y el formato de relleno de los títulos.

|![todo:image_alt_text](chart_title.png)|

## **Configuración de los Títulos de Gráficos o Ejes**
Puedes usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells for JavaScript vía C++ también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una propiedad [Title](https://reference.aspose.com/cells/javascript-cpp/title/) que puede usarse para establecer sus títulos como se muestra a continuación en un ejemplo.

El siguiente fragmento de código demuestra cómo establecer títulos a gráficos y ejes.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 60;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = AsposeCells.Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Leer subtítulo del gráfico desde un archivo ODS](/cells/es/javascript-cpp/read-chart-subtitle-from-ods-file/)
